# Publicar no Cloudflare — c/txt. / Humano Biônico

Esta pasta contém uma implantação **Cloudflare Workers + Static Assets + D1 + Turnstile**, sem servidor Python. **O armazenamento só começa a funcionar depois da configuração do banco, da verificação e da política de privacidade.** O HTML isolado do diretório pai continua sendo uma demonstração local sem envio de dados.

## Solução para o mapa que não aparecia (v3)

A versão anterior desabilitava a ação final quando `GET /api/config` indicava que a Cloudflare ainda não tinha D1/Turnstile/política configurados. A v3 mostra explicitamente um **modo de prévia**, no qual a matriz é apresentada após o formulário **sem gravar nem enviar nenhum dado**. Ao configurar a API, o site muda automaticamente para o modo de coleta real, que continua exigindo consentimento, Turnstile, envio e confirmação de gravação em D1 para liberar o resultado.

Diagnóstico rápido:

- Se o botão diz **"visualizar meu mapa (prévia)"**: o site não está recebendo contatos. Verifique o deploy, o endpoint `/api/config`, os bindings D1 e os secrets.
- Se diz **"revelar meu mapa"**: o site está no modo de coleta. Em caso de falha ao enviar, confira a mensagem sob o botão, a configuração do Turnstile para o hostname correto e os logs do Worker.
- Acesse `https://SEU_DOMINIO/api/config` para conferir `ready`. A API não expõe os dados pessoais nessa rota.

## 1 · O que acontece com os dados

```text
20 respostas → identificação (nome, empresa, e-mail, IAs usadas)
             → aceite para processar dados
             → Cloudflare Turnstile (antibot)
             → POST /api/lead (Worker)
             → validação e recálculo dos dois eixos no Worker
             → gravação em D1
             → resposta HTTP 201 com pontuação
             → apresentação do resultado no navegador
```

O Worker **não possui rota pública de exportação ou listagem**. O acesso a registros ocorre apenas pela conta Cloudflare autorizada. A configuração traz expiração padrão de 90 dias (`RETENTION_DAYS`, tarefa diária). Antes de publicar, defina retenção e a política real aplicável ao projeto. A base contém dados pessoais e respostas individuais.

## 2 · Crie o banco D1

Instale Node.js 20+ (ou versão LTS atual), abra o terminal nesta pasta `cloudflare/` e faça login:

```bash
npx wrangler login
npx wrangler d1 create ctxt-humano-bionico --binding DB --update-config
```

Este comando cria o banco e adiciona automaticamente o vínculo `DB` (com o UUID real) ao `wrangler.jsonc`. Confira que a entrada `d1_databases` foi criada antes de continuar. Se a opção de atualização automática não funcionar, copie o trecho `d1_databases` exibido no terminal e acrescente-o manualmente ao arquivo, mantendo o binding com o nome `DB`.

Crie as tabelas na base remota:

```bash
npx wrangler d1 execute ctxt-humano-bionico --remote --file=./schema.sql
```

Para testes sem armazenar dados reais, crie a tabela localmente:

```bash
npx wrangler d1 execute ctxt-humano-bionico --local --file=./schema.sql
```

## 3 · Configure o Turnstile

No painel Cloudflare, acesse **Turnstile**, crie um widget para seu domínio (e, se necessário, o domínio de testes `*.workers.dev`). Você receberá um **Site Key**, público, e um **Secret Key**, privado. O frontend obtém o Site Key de `/api/config`; o Secret Key fica somente no ambiente do Worker. O Worker valida todos os tokens em `siteverify` e confere o hostname da resposta.

Configure quatro valores no Worker com os comandos abaixo (o terminal solicitará cada valor, que **não deve** ir para o HTML nem para o Git):

```bash
npx wrangler secret put TURNSTILE_SITE_KEY
npx wrangler secret put TURNSTILE_SECRET_KEY
npx wrangler secret put DATA_CONTROLLER
npx wrangler secret put PRIVACY_POLICY_URL
```

- `DATA_CONTROLLER`: identificação correta da entidade controladora, por exemplo a razão social que responde pelo cadastro; não use uma pessoa ou empresa sem autorização.
- `PRIVACY_POLICY_URL`: **URL HTTPS pública e válida** de uma política que explique finalidades, base legal apropriada, retenção, hospedagem/transferências, contato, direitos dos titulares e, quando houver, comunicações de marketing. Não aponte para uma página provisória sem conteúdo.
- `TURNSTILE_SITE_KEY` e `TURNSTILE_SECRET_KEY`: chaves do mesmo widget.

**Antes de receber cadastros reais**, publique a política de privacidade, verifique seu enquadramento na LGPD e revise os controles de acesso à conta Cloudflare. Não use o questionário como instrumento de seleção, classificação profissional ou avaliação individual compulsória.

## 4 · Publique o site e a API juntos

```bash
npx wrangler deploy
```

Isso publica `public/index.html` como site e `worker.js` como API **no mesmo domínio**. O formulário envia para `POST /api/lead`. A rota `GET /api/config` informa o Site Key, o link da política e se a coleta está configurada.

Para conectar domínio próprio: **Cloudflare → Workers & Pages → ctxt-humano-bionico → Settings → Domains & Routes** (o nome da seção pode mudar). Adicione o domínio/subdomínio de sua zona Cloudflare. Lembre de autorizar este domínio no widget Turnstile.

**Fluxo antes de publicar:** teste primeiro em um domínio temporário com informações fictícias. A criação do banco remoto e o deploy precisam ocorrer em sua própria conta Cloudflare; este pacote não executa essas ações automaticamente.

## 5 · Como ver os cadastros

No painel: **Cloudflare → D1 → ctxt-humano-bionico → Console**. Exemplo de consulta:

```sql
SELECT created_at, name, email, company, score_x, score_y, quadrant
FROM submissions
ORDER BY created_at DESC LIMIT 30;
```

Ou pelo terminal:

```bash
npx wrangler d1 execute ctxt-humano-bionico --remote \
  --command="SELECT created_at, name, email, company, score_x, score_y, quadrant FROM submissions ORDER BY created_at DESC LIMIT 30"
```

Para backup/exportação privada (dados pessoais: **não coloque no diretório `public/`**):

```bash
npx wrangler d1 export ctxt-humano-bionico --remote --output=./export-privado.sql
```

Considere agregar relatórios por equipe apenas com grupos suficientemente grandes para preservar o anonimato; não exponha dados individuais a gestores.

## 6 · Testar sem publicar

```bash
npx wrangler dev
```

O site mostra o resultado em prévia local se a API e o Turnstile ainda não estiverem configurados; nesse modo não grava cadastros. Para testar armazenamento real, configure um Turnstile válido e o D1. Para testes funcionais automatizados da API em ambiente de mock, execute `node tests/worker.test.mjs` na pasta `cloudflare/`; isso **não toca o D1 real**.

## 7 · Estrutura

- `public/index.html`: site publicado, com `/api/lead` e configuração dinâmica via `/api/config`.
- `worker.js`: API, validações, Turnstile, armazenamento e limpeza automática.
- `schema.sql`: tabela D1 e índices.
- `wrangler.jsonc`: deploy de Worker, assets, D1, retenção.
- `tests/worker.test.mjs`: testes locais de validação e recálculo.

**Observação metodológica:** Q14 agora é afirmativa e **não é invertida**. Apenas Q10 tem pontuação reversa. São duas pontuações exploratórias, não medidas clínicas nem capacidades cognitivas objetivas.

## Documentação oficial

- Static Assets: https://developers.cloudflare.com/workers/static-assets/
- D1: https://developers.cloudflare.com/d1/get-started/
- Wrangler D1: https://developers.cloudflare.com/d1/wrangler-commands/
- Turnstile: https://developers.cloudflare.com/turnstile/get-started/server-side-validation/
