#!/usr/bin/env python3
"""Servidor opcional para o Diagnóstico do Humano Biônico.

Sem bibliotecas externas. Salva leads num SQLite fora da árvore pública
(este servidor só serve rotas explicitamente autorizadas).

Antes de hospedar publicamente: configure HTTPS, política LGPD,
backups/segurança e revisão técnica do backend.
"""
from __future__ import annotations

import argparse
import csv
from collections import defaultdict, deque
from datetime import datetime, timezone
import html
import json
import os
from pathlib import Path
import re
import sqlite3
import stat
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parent
DATA_DIR = Path(os.environ.get('CTXT_DATA_DIR', str(Path.home() / '.ctxt-dados'))).expanduser().resolve()
DB_PATH = DATA_DIR / 'avaliacoes.sqlite3'
INDEX_PATH = ROOT / 'index.html'
NAME_LIMIT = 120
EMAIL_RX = re.compile(r'^[^\s@]+@[^\s@]+\.[^\s@]{2,}$')
PERSONAL_DOMAINS = {
    'gmail.com','googlemail.com','hotmail.com','hotmail.com.br',
    'outlook.com','outlook.com.br','live.com','live.com.br',
    'yahoo.com','yahoo.com.br','icloud.com','me.com','mac.com',
    'aol.com','proton.me','protonmail.com','pm.me','bol.com.br',
    'uol.com.br','terra.com.br','ig.com.br','msn.com','mail.com',
    'gmx.com','gmx.net','zoho.com','yandex.com','yandex.ru','qq.com','163.com'
}
TOOL_NAMES = {'ChatGPT','Microsoft Copilot','Google Gemini','Claude','Perplexity',
              'GitHub Copilot','Notion AI','Grok','Não utilizo IA no trabalho'}
LOCK = threading.Lock()
RATE_LOCK = threading.Lock()
RECENT = defaultdict(deque)


def now_iso():
    return datetime.now(timezone.utc).isoformat(timespec='seconds')


def init_db():
    DATA_DIR.mkdir(mode=0o700, parents=True, exist_ok=True)
    if os.name == 'posix':
        try: os.chmod(DATA_DIR, 0o700)
        except PermissionError: pass
    with sqlite3.connect(DB_PATH, timeout=10) as con:
        con.execute('''CREATE TABLE IF NOT EXISTS submissions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            created_at TEXT NOT NULL,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            company TEXT NOT NULL,
            ai_tools_json TEXT NOT NULL,
            answers_json TEXT NOT NULL,
            score_x INTEGER NOT NULL,
            score_y INTEGER NOT NULL,
            x_raw INTEGER NOT NULL,
            y_raw INTEGER NOT NULL,
            quadrant TEXT NOT NULL,
            marketing_consent INTEGER NOT NULL,
            privacy_consent INTEGER NOT NULL
        )''')
        con.execute('CREATE INDEX IF NOT EXISTS idx_submissions_email ON submissions(email)')
        con.commit()
    if os.name == 'posix':
        try: os.chmod(DB_PATH, 0o600)
        except PermissionError: pass


def validate_submission(obj):
    if not isinstance(obj, dict):
        raise ValueError('Formato inválido.')
    name = obj.get('name','')
    company = obj.get('company','')
    email = obj.get('email','')
    if not all(isinstance(x,str) for x in (name,company,email)):
        raise ValueError('Campos profissionais inválidos.')
    name, company, email = name.strip(),company.strip(),email.strip().lower()
    if not (2 <= len(name) <= NAME_LIMIT and 2 <= len(company) <= NAME_LIMIT):
        raise ValueError('Nome e empresa são obrigatórios.')
    if len(email)>254 or not EMAIL_RX.fullmatch(email) or email.rsplit('@',1)[1] in PERSONAL_DOMAINS:
        raise ValueError('Informe um e-mail corporativo válido.')
    if obj.get('privacyConsent') is not True:
        raise ValueError('Consentimento para processamento não informado.')
    selected = obj.get('aiTools')
    if not isinstance(selected,list) or not 1<=len(selected)<=11:
        raise ValueError('Informe as IAs utilizadas.')
    if any(not isinstance(t,str) or len(t)>160 or (t not in TOOL_NAMES and not t.startswith('Outras: ')) for t in selected):
        raise ValueError('Ferramenta inválida.')
    if len(set(selected))!=len(selected):
        raise ValueError('Ferramentas duplicadas.')
    if 'Não utilizo IA no trabalho' in selected and len(selected)>1:
        raise ValueError('Escolha "não utilizo" isoladamente.')
    answers = obj.get('answers')
    if not isinstance(answers,list) or len(answers)!=20:
        raise ValueError('Responda às 20 questões.')
    raw=[]
    for i,answer in enumerate(answers):
        if not isinstance(answer,dict) or answer.get('number')!=i+1 or type(answer.get('raw')) is not int or not 1<=answer['raw']<=5:
            raise ValueError('Respostas incompletas ou inválidas.')
        raw.append(answer['raw'])
    adjusted=[6-v if i in (9,) else v for i,v in enumerate(raw)]
    x_raw=sum(adjusted[:10]); y_raw=sum(adjusted[10:])
    x=int((x_raw-10)/40*100+0.5);y=int((y_raw-10)/40*100+0.5)
    quadrant=f"{'high' if x_raw>=30 else 'low'}-{'high' if y_raw>=30 else 'low'}"
    return {'created_at':now_iso(),'name':name,'company':company,'email':email,
            'ai_tools':selected,'answers':raw,'x_raw':x_raw,'y_raw':y_raw,
            'x':x,'y':y,'quadrant':quadrant,
            'marketing_consent':1 if obj.get('marketingConsent') is True else 0,'privacy_consent':1}


def accept_rate(ip):
    """Basic in-memory rate limit: max 10 submissions per hour per peer IP."""
    current=time.monotonic()
    with RATE_LOCK:
        slots=RECENT[ip]
        while slots and slots[0]<current-3600:
            slots.popleft()
        if len(slots)>=10:
            return False
        slots.append(current)
        # Bound stored keys to guard against long-running memory growth.
        if len(RECENT)>10000:
            for key in list(RECENT)[:1000]:
                if not RECENT[key] or RECENT[key][-1]<current-3600:
                    del RECENT[key]
        return True


def save_submission(row):
    with LOCK:
        with sqlite3.connect(DB_PATH,timeout=10) as con:
            con.execute('''INSERT INTO submissions
                (created_at,name,email,company,ai_tools_json,answers_json,
                 score_x,score_y,x_raw,y_raw,quadrant,marketing_consent,privacy_consent)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)''', (
                    row['created_at'],row['name'],row['email'],row['company'],
                    json.dumps(row['ai_tools'],ensure_ascii=False),
                    json.dumps(row['answers'],ensure_ascii=False),
                    row['x'],row['y'],row['x_raw'],row['y_raw'],row['quadrant'],
                    row['marketing_consent'],row['privacy_consent']))
            con.commit()


def js_quoted(s):
    return json.dumps(s,ensure_ascii=False).replace('<','\\u003c').replace('>','\\u003e').replace('&','\\u0026')


class Handler(BaseHTTPRequestHandler):
    server_version='CTXT/1.0'
    sys_version=''

    def security_headers(self):
        self.send_header('X-Content-Type-Options','nosniff')
        self.send_header('Referrer-Policy','no-referrer')
        self.send_header('X-Frame-Options','DENY')
        self.send_header('Cache-Control','no-store')
        self.send_header('Permissions-Policy','camera=(), microphone=(), geolocation=()')
        self.send_header('Content-Security-Policy',
            "default-src 'none'; script-src 'self' 'unsafe-inline'; "
            "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; "
            "font-src https://fonts.gstatic.com; connect-src 'self'; "
            "img-src 'self' data:; base-uri 'none'; form-action 'self'; frame-ancestors 'none'")

    def send_response_bytes(self,status,content,typ='application/json; charset=utf-8'):
        self.send_response(status)
        self.security_headers()
        self.send_header('Content-Type',typ)
        self.send_header('Content-Length',str(len(content)))
        self.end_headers()
        self.wfile.write(content)

    def send_json(self,status,obj):
        self.send_response_bytes(status,json.dumps(obj,ensure_ascii=False).encode('utf-8'))

    def do_GET(self):
        path=urlsplit(self.path).path
        if path not in ('/','/index.html','/health'):
            self.send_json(404,{'ok':False,'error':'Não encontrado.'});return
        if path=='/health':
            self.send_json(200,{'ok':True});return
        html_text=INDEX_PATH.read_text(encoding='utf-8')
        marker="leadEndpoint: '',"
        if html_text.count(marker)!=1:
            self.send_json(500,{'ok':False,'error':'Configuração HTML incompatível.'});return
        html_text=html_text.replace(marker,"leadEndpoint: '/api/lead',")
        html_text=html_text.replace("privacyPolicyUrl: '',",f"privacyPolicyUrl: {js_quoted(self.server.privacy_url)},")
        html_text=html_text.replace("dataController: 'Clube de Contexto · gira. laboratório de futuros'",f"dataController: {js_quoted(self.server.controller)}")
        self.send_response_bytes(200,html_text.encode('utf-8'),'text/html; charset=utf-8')

    def do_POST(self):
        if urlsplit(self.path).path!='/api/lead':
            self.send_json(404,{'ok':False,'error':'Não encontrado.'});return
        origin=self.headers.get('Origin')
        if origin and origin!=self.server.public_origin:
            self.send_json(403,{'ok':False,'error':'Origem não autorizada.'});return
        if not self.headers.get('Content-Type','').lower().startswith('application/json'):
            self.send_json(415,{'ok':False,'error':'Envie JSON.'});return
        try:
            length=int(self.headers.get('Content-Length','0'))
        except ValueError:
            self.send_json(400,{'ok':False,'error':'Tamanho inválido.'});return
        if not 1<=length<=32*1024:
            self.send_json(413,{'ok':False,'error':'Conteúdo excede o limite.'});return
        try:
            data=json.loads(self.rfile.read(length))
            row=validate_submission(data)
        except (UnicodeError,ValueError,TypeError,json.JSONDecodeError) as exc:
            self.send_json(400,{'ok':False,'error':str(exc)[:140]});return
        if not accept_rate(self.client_address[0]):
            self.send_json(429,{'ok':False,'error':'Limite de envios atingido.'});return
        try:
            save_submission(row)
        except sqlite3.Error:
            self.send_json(503,{'ok':False,'error':'Falha ao salvar dados.'});return
        self.send_json(201,{'ok':True})

    def log_message(self,format,*args):
        # Never log payload, email, name, query data or arbitrary request content.
        if os.environ.get('CTXT_DEBUG_LOGS')=='1':
            print('[ctxt]',format % args)


def export_csv(output_path):
    if not DB_PATH.exists():
        raise SystemExit('Ainda não existe um banco de dados de respostas.')
    dest=Path(output_path).expanduser().resolve()
    if dest.exists():
        raise SystemExit('O arquivo de destino já existe; escolha outro nome para não sobrescrever dados.')
    with sqlite3.connect(DB_PATH,timeout=10) as con, open(dest,'x',newline='',encoding='utf-8-sig') as output:
        writer=csv.writer(output)
        writer.writerow(['data_utc','nome','email','empresa','ias','eixo_x_0_100','eixo_y_0_100','quadrante','aceite_marketing','respostas_1_a_20'])
        for r in con.execute('''SELECT created_at,name,email,company,ai_tools_json,
             score_x,score_y,quadrant,marketing_consent,answers_json FROM submissions ORDER BY id'''):
            # Prevent formula injection on import into Excel/Sheets.
            sanitized=[]
            for c in r:
                if isinstance(c,str) and c and c[0] in ('=','+','-','@','\t','\r'):
                    sanitized.append("'"+c)
                else:
                    sanitized.append(c)
            writer.writerow(sanitized)
    if os.name=='posix':
        os.chmod(dest,0o600)
    print(f'Exportado: {dest}')


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action',nargs='?',choices=['serve','export'],default='serve')
    parser.add_argument('--output',help='arquivo CSV de destino para a exportação')
    args=parser.parse_args()
    if args.action=='export':
        if not args.output:
            parser.error('Para exportar, use --output /caminho/leads.csv')
        export_csv(args.output);return
    privacy=os.environ.get('CTXT_PRIVACY_URL','').strip()
    controller=os.environ.get('CTXT_CONTROLLER','').strip()
    if not privacy or not controller:
        parser.error('Para ativar a captação, configure CTXT_PRIVACY_URL (URL da política de privacidade publicada) e CTXT_CONTROLLER (nome do controlador de dados).')
    if not privacy.startswith('https://') and not os.environ.get('CTXT_LOCAL_TEST')=='1':
        parser.error('CTXT_PRIVACY_URL deve começar com https:// em produção.')
    init_db()
    host=os.environ.get('CTXT_HOST','127.0.0.1')
    port=int(os.environ.get('CTXT_PORT','8080'))
    public_origin=os.environ.get('CTXT_PUBLIC_ORIGIN',f'http://{host}:{port}').rstrip('/')
    server=ThreadingHTTPServer((host,port),Handler)
    server.privacy_url=privacy;server.controller=controller;server.public_origin=public_origin
    print(f'Servidor rodando em {public_origin} (sem TLS embutido; use proxy HTTPS para produção)')
    print(f'Banco SQLite privado em {DB_PATH}')
    try:server.serve_forever()
    except KeyboardInterrupt:pass
    finally:server.server_close()

if __name__=='__main__':main()
