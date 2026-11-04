# Diagnóstico do Humano Biônico — implantação sem Terminal

Este pacote é para upload em um repositório privado no GitHub, via navegador, e publicação automática com **Cloudflare Workers Builds**. Nenhum comando precisa ser digitado no seu computador. O serviço de build da Cloudflare executará o deploy automaticamente.

## Estrutura correta no GitHub

Na raiz do repositório devem estar **worker.js**, **wrangler.jsonc**, **schema.sql** e a pasta **public** contendo **index.html**.

```
worker.js
wrangler.jsonc
schema.sql
public/index.html
```

## 1. Criar banco Cloudflare D1

Cloudflare → Storage & databases → D1 SQL database → Create Database. Nome: `ctxt-humano-bionico`. Na página do banco, copie o **Database ID** (UUID).

## 2. Criar tabela

No banco, abra **Console** e cole o conteúdo do arquivo `schema.sql`; clique **Execute**. Verifique em **Tables** se existe a tabela `submissions`.

## 3. Criar repositório no GitHub

GitHub → New repository → nome `ctxt-humano-bionico` → **Private**. Acesse **Add file → Upload files** e arraste o conteúdo desta pasta para o navegador (não o arquivo ZIP). Faça commit. Confira a estrutura acima.

## 4. Trocar ID do D1

No GitHub, abra `wrangler.jsonc` → Edit (ícone de lápis) → troque **somente** `SUBSTITUA_PELO_ID_D1_NA_CLOUDFLARE` pelo identificador do banco D1. Mantenha as aspas. Clique **Commit changes**.

## 5. Conectar Cloudflare ao GitHub

Cloudflare → Workers & Pages → Create application → GitHub → autorize acesso somente ao repositório necessário → selecione `ctxt-humano-bionico`. Root directory: raiz do repositório; Build command: vazio; Deploy command: o valor padrão do Cloudflare (executado pela Cloudflare automaticamente). Salve e publique. Uma URL `.workers.dev` será criada.

## 6. Configurar Turnstile

Cloudflare → Turnstile → Add widget. Nome `ctxt-diagnostico`; escolha Managed; cadastre seu hostname final (por exemplo `diagnostico.seudominio.com`) e gere **Site Key** e **Secret Key**. Adicione esse hostname em Workers & Pages → Worker → Settings → Domains & Routes, de acordo com sua zona. Se usar `.workers.dev`, configure também o hostname exato que aparece na URL de teste, se aceito no widget. O backend confere o hostname retornado pelo Turnstile.

## 7. Configurar quatro valores do Worker

Workers & Pages → `ctxt-humano-bionico` → Settings → Variables and Secrets → Add:
- `TURNSTILE_SITE_KEY`: site key do widget; pode ser texto público.
- `TURNSTILE_SECRET_KEY`: tipo **Secret**; nunca compartilhar.
- `DATA_CONTROLLER`: nome da entidade responsável pelo tratamento de dados.
- `PRIVACY_POLICY_URL`: URL HTTPS real e pública de sua política de privacidade.
Clique Deploy/Save conforme a tela. O consentimento de dados do formulário é separado da opção de marketing.

## 8. Testar

Abra `https://SEU-SITE/api/config`. `ready:true` significa apenas que as configurações existem; ainda é preciso testar o envio. Conclua as 20 perguntas com dados fictícios, cadastre-se e confirme o mapa. Em D1 → Console, verifique a linha usando:

```sql
SELECT created_at, name, email, company, score_x, score_y, quadrant
FROM submissions ORDER BY created_at DESC LIMIT 10;
```

Se a interface mostrar *visualizar meu mapa (prévia)*, não há coleta real. Verifique banco, ID, variáveis e segredos. Se o envio falhar, confira hostname Turnstile e mensagens em Workers → Logs.

## Segurança e privacidade

Os dados pessoais ficam em D1, não são expostos por rotas de listagem. Configure HTTPS, política de privacidade e controle de acesso. O Worker apaga registros antigos automaticamente após 90 dias por padrão (o prazo deve ser revisado antes de coletar dados reais). **Não coloque chaves secretas no GitHub**, não crie consultas públicas e não apresente a autoavaliação como teste clínico ou medida objetiva de competência.

Documentação: https://developers.cloudflare.com/workers/ci-cd/builds/ · https://developers.cloudflare.com/d1/get-started/ · https://developers.cloudflare.com/turnstile/get-started/widget-management/dashboard/
