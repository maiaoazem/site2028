/**
 * c/txt. · Diagnóstico do Humano Biônico — Cloudflare Worker + D1.
 * Apenas grava avaliações; não disponibiliza endpoints públicos de leitura/exportação.
 * Configure D1, Turnstile e a política de privacidade antes de receber dados reais.
 */
const PERSONAL_DOMAINS = new Set([
  'gmail.com','googlemail.com','hotmail.com','hotmail.com.br','outlook.com','outlook.com.br',
  'live.com','live.com.br','yahoo.com','yahoo.com.br','yahoo.com.ar','icloud.com',
  'me.com','mac.com','aol.com','proton.me','protonmail.com','pm.me','bol.com.br',
  'uol.com.br','terra.com.br','ig.com.br','msn.com','mail.com','gmx.com','gmx.net',
  'zoho.com','yandex.com','yandex.ru','qq.com','163.com'
]);
const TOOLS = new Set(['ChatGPT','Microsoft Copilot','Google Gemini','Claude','Perplexity',
  'GitHub Copilot','Notion AI','Grok','Outras','Não utilizo IA no trabalho']);
const headers = {
  'Cache-Control':'no-store',
  'X-Content-Type-Options':'nosniff',
  'Referrer-Policy':'no-referrer',
  'X-Frame-Options':'DENY'
};
function json(data,status=200){
  return new Response(JSON.stringify(data), {status,headers:{...headers,'Content-Type':'application/json; charset=utf-8'}});
}
function isReady(env){
  return Boolean(env.DB && env.DATA_CONTROLLER?.trim() && env.PRIVACY_POLICY_URL?.trim() &&
    env.TURNSTILE_SITE_KEY?.trim() && env.TURNSTILE_SECRET_KEY?.trim());
}
function str(v,max){return typeof v==='string' ? v.trim().slice(0,max+1):'';}
function validate(payload){
  if(!payload || typeof payload!=='object' || Array.isArray(payload)) throw Error('Dados inválidos.');
  if(payload.schemaVersion!=='1.1') throw Error('Versão da avaliação incompatível.');
  const name=str(payload.name,120),company=str(payload.company,120),email=str(payload.email,254).toLowerCase();
  if(name.length<2||name.length>120||company.length<2||company.length>120) throw Error('Informe nome e empresa.');
  if(email.length>254||! /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(email) || PERSONAL_DOMAINS.has(email.split('@')[1]))
    throw Error('Informe um e-mail corporativo válido.');
  if(payload.privacyConsent!==true) throw Error('Aceite as informações de privacidade.');
  const tools=payload.aiTools;
  if(!Array.isArray(tools)||tools.length<1||tools.length>11 ||
    tools.some(t=>typeof t!=='string'||t.length>160||(!TOOLS.has(t)&&!t.startsWith('Outras: '))) ||
    new Set(tools).size!==tools.length||
    (tools.includes('Não utilizo IA no trabalho')&&tools.length!==1)) throw Error('Seleção de ferramentas inválida.');
  const answers=payload.answers;
  if(!Array.isArray(answers)||answers.length!==20) throw Error('As 20 respostas são obrigatórias.');
  const raw=answers.map((a,i)=>{
    if(!a||a.number!==i+1 || !Number.isInteger(a.raw)||a.raw<1||a.raw>5) throw Error('Respostas inválidas.');
    return a.raw;
  });
  // Apenas a pergunta 10 é invertida: a pergunta 14 foi reformulada positivamente.
  const scored=raw.map((n,i)=>i===9?6-n:n);
  const xRaw=scored.slice(0,10).reduce((a,b)=>a+b,0);
  const yRaw=scored.slice(10).reduce((a,b)=>a+b,0);
  const x=Math.round((xRaw-10)*2.5),y=Math.round((yRaw-10)*2.5);
  const quadrant=`${xRaw>=30?'high':'low'}-${yRaw>=30?'high':'low'}`;
  return {name,company,email,tools,raw,marketingConsent:payload.marketingConsent===true,
    scores:{x,y,xRaw,yRaw,quadrant}};
}
async function verifyTurnstile(env,token,host){
  if(typeof token!=='string'||token.length<1||token.length>2048) return false;
  let response;
  try{
    response=await fetch('https://challenges.cloudflare.com/turnstile/v0/siteverify',{
      method:'POST',headers:{'Content-Type':'application/json'},
      body:JSON.stringify({secret:env.TURNSTILE_SECRET_KEY,response:token})
    });
    if(!response.ok)return false;
    const data=await response.json();
    // A resposta deve ter sido emitida para o próprio domínio da avaliação.
    return data.success===true && data.hostname===host;
  }catch{return false;}
}
async function submit(request,env){
  if(!isReady(env))return json({ok:false,error:'Coleta ainda não configurada.'},503);
  const origin=request.headers.get('Origin');
  if(origin!==new URL(request.url).origin) return json({ok:false,error:'Origem não autorizada.'},403);
  if(!request.headers.get('Content-Type')?.toLowerCase().startsWith('application/json'))
    return json({ok:false,error:'Envie JSON.'},415);
  const contentLength=Number(request.headers.get('Content-Length'));
  if(Number.isFinite(contentLength)&&contentLength>24576)return json({ok:false,error:'Conteúdo muito grande.'},413);
  let payload;
  try{
    const text=await request.text();
    if(text.length>24576)return json({ok:false,error:'Conteúdo muito grande.'},413);
    payload=JSON.parse(text);
  }catch{return json({ok:false,error:'JSON inválido.'},400);}
  let validated;
  try{validated=validate(payload);}catch(e){return json({ok:false,error:e.message},400);}
  if(!await verifyTurnstile(env,payload.turnstileToken,new URL(request.url).hostname))
    return json({ok:false,error:'Verificação de segurança inválida ou expirada.'},403);
  const {name,company,email,tools,raw,marketingConsent,scores}=validated;
  const id=crypto.randomUUID();
  const createdAt=new Date().toISOString();
  try{
    await env.DB.prepare(`INSERT INTO submissions
      (id,created_at,name,email,company,ai_tools_json,answers_json,
       x_raw,y_raw,score_x,score_y,quadrant,privacy_consent,marketing_consent)
      VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)`)
      .bind(id,createdAt,name,email,company,JSON.stringify(tools),JSON.stringify(raw),
        scores.xRaw,scores.yRaw,scores.x,scores.y,scores.quadrant,1,marketingConsent?1:0)
      .run();
  }catch(error){
    console.error('Falha ao salvar avaliação no D1',String(error));
    return json({ok:false,error:'Não foi possível registrar sua avaliação.'},500);
  }
  return json({ok:true,id,scores},201);
}
export default {
  async fetch(request,env){
    const url=new URL(request.url);
    if(url.pathname==='/api/config' && request.method==='GET'){
      return json({ready:isReady(env),siteKey:env.TURNSTILE_SITE_KEY||'',
        privacyPolicyUrl:env.PRIVACY_POLICY_URL||'',dataController:env.DATA_CONTROLLER||''});
    }
    if(url.pathname==='/api/lead'){
      if(request.method!=='POST')return json({ok:false,error:'Método não permitido.'},405);
      return submit(request,env);
    }
    if(url.pathname.startsWith('/api/'))return json({ok:false,error:'Não encontrado.'},404);
    return env.ASSETS.fetch(request);
  },
  async scheduled(_event,env,ctx){
    if(!env.DB)return;
    const days=Number.parseInt(env.RETENTION_DAYS||'90',10);
    if(!Number.isSafeInteger(days)||days<1||days>3650)return;
    const cutoff=new Date(Date.now()-days*86400000).toISOString();
    ctx.waitUntil(env.DB.prepare('DELETE FROM submissions WHERE created_at < ?').bind(cutoff).run());
  }
};
