# Diagnóstico do Humano Biônico · c/txt.

Site responsivo de autoavaliação, adaptado a partir do **Maia Oazem Design System v10.1** e do método do **c/txt. · Clube de Contexto**.

## Correção do acesso ao mapa — versão 3

A visualização da matriz e dos quadrantes foi conferida em teste de navegador percorrendo todas as 20 perguntas e o formulário de identificação. Em **modo demonstração**, o resultado aparece após preencher os campos e não há envio de dados. O mapa é mostrado na seção "seu jeito de pensar", abaixo do perfil e dos indicadores.

Na versão `cloudflare/public/index.html`, o site verifica `GET /api/config`:

- **`ready: true`:** pede aceite de privacidade e Turnstile, envia `POST /api/lead` e só libera o mapa após confirmação de gravação no D1. Erros do servidor aparecem no próprio formulário, sem liberar o mapa.
- **`ready: false` ou API indisponível:** muda explicitamente para **prévia local**, habilita "visualizar meu mapa (prévia)" e exibe aviso de que nome, e-mail, empresa e respostas não são coletados. Este comportamento serve apenas para avaliação da interface antes da configuração da Cloudflare.

**Importante:** visualizar o mapa em prévia não confirma que você está captando contatos. Para receber dados reais, conclua D1, Turnstile, política de privacidade e implantação na Cloudflare. Atualize o arquivo publicado com esta versão 3, pois a versão anterior bloqueava o botão quando `/api/config` retornava `ready: false`.

## Começar

Abra `index.html` em um navegador. O instrumento funciona sem build, sem instalar pacotes e sem servidor. Os dados preenchidos e as respostas ficam **somente na memória da aba** e são descartados ao recarregar ou fechar a página. O resultado é exibido após a validação dos quatro campos: nome, empresa, e-mail corporativo e ferramentas de IA utilizadas.

### O que está implementado

- 20 questões, apresentadas uma por vez, com 1–5 na horizontal; avanço automático ao escolher uma opção, navegação de retorno e atalhos de teclado. Tempo estimado de 5–7 minutos na abertura.
- Dois eixos com 10 itens cada. Somente o item 10 é invertido (`6 - resposta`); o item 14 agora é afirmativo e não é invertido. Cada eixo soma de 10 a 50, normalizado visualmente para 0–100: `(soma - 10) / 40 * 100`.
- Quatro quadrantes para pontuações abaixo/acima do ponto médio aritmético **30/50**. Os limiares não foram validados cientificamente.
- Recomendações práticas a partir das duas menores pontuações ajustadas (uma em cada eixo) e um exercício de contexto coletivo.
- Formulário obrigatório, validação de e-mail corporativo, seleção de múltiplas IAs, opção de não uso e campo para outras IAs.
- Resultado com matriz e marcador, pontuações, descrição de quadrante e três práticas. Botões de impressão / salvar em PDF pelo navegador e copiar resumo.
- Layout editorial e responsivo com os tokens, fontes e linhas do design system, sem inventar ou redesenhar o logo Maia Oazem.

## Publicação recomendada: Cloudflare Workers + D1

Há uma implementação de produção na pasta [`cloudflare/`](cloudflare/README.md), com API `/api/lead`, banco D1, Turnstile e configuração de domínio. Siga o README específico para configurar as credenciais, o banco e a política de privacidade antes de publicar. O site estático na raiz permanece em modo de demonstração.

## Importante: captação real de cadastros

**Ao abrir `index.html` diretamente, você está em modo demonstração.** Por padrão, nenhum dado é transmitido a servidor, CRM ou e-mail. Mostrar um campo de e-mail não significa que ele esteja sendo coletado por você.

O pacote também inclui **`server.py`**, um servidor opcional com armazenamento real em SQLite, testes de validação no servidor e exportação CSV. Ele pode ser usado em ambientes controlados e preparado para implantação com HTTPS, mas não substitui uma revisão técnica, segurança operacional e política de privacidade para uso público.

### Opção A · servidor próprio com captura real (Python + SQLite)

O backend roda apenas com Python 3.10+; não precisa instalar dependências. Abra um terminal na pasta do pacote, configure as variáveis abaixo e inicie:

```bash
export CTXT_CONTROLLER='Nome legal da empresa controladora'
export CTXT_PRIVACY_URL='https://seu-dominio.com/privacidade'
export CTXT_PUBLIC_ORIGIN='http://127.0.0.1:8080'
python server.py
```

Acesse `http://127.0.0.1:8080`. Quando servido por `server.py`, o HTML é automaticamente configurado para `POST /api/lead`: a coleta passa a ser real e o resultado é liberado após o backend registrar a resposta. O endereço de política de privacidade **precisa corresponder a uma página real e atualizada**.

O banco fica, por padrão, em `~/.ctxt-dados/avaliacoes.sqlite3`, com pasta protegida e fora das rotas públicas. Altere a localização com a variável `CTXT_DATA_DIR`. Para obter uma planilha CSV de cadastros e scores:

```bash
python server.py export --output ./cadastros-ctxt.csv
```

O arquivo exportado contém dados pessoais: não o coloque em um diretório público. O backend não possui painel de acesso, recuperação de senha, sistema de e-mails ou TLS nativo. **Para uso real na internet, execute atrás de um proxy HTTPS**, configure `CTXT_HOST`, `CTXT_PORT` e `CTXT_PUBLIC_ORIGIN` conforme o domínio publicado, revise controles anti-spam e adote política de retenção e exclusão dos dados. O limite de taxa em memória é básico e não substitui proteção de produção.

### Opção B · conectar a serviço externo (CRM, webhook, API)

Se preferir publicar o `index.html` num serviço estático, configure o envio nele diretamente. Edite no final do `index.html`:

```js
const CONFIG = {
  leadEndpoint: 'https://SEU-DOMINIO.example/api/lead',
  privacyPolicyUrl: 'https://SEU-DOMINIO.example/privacidade',
  dataController: 'NOME DA ENTIDADE CONTROLADORA'
};
```

O endpoint deverá aceitar uma requisição HTTPS `POST` com `Content-Type: application/json`, responder com status `2xx` **apenas quando os dados estiverem devidamente salvos**, permitir a origem do domínio do site (se em outro domínio) e cumprir as responsabilidades da LGPD. A interface só exibe o resultado após a resposta de sucesso do endpoint. Se houver falha no envio, mantém o formulário e exibe erro.

### Estrutura do JSON enviado ao endpoint

```json
{
  "schemaVersion": "1.1",
  "submittedAt": "2026-11-04T13:00:00.000Z",
  "name": "Pessoa Exemplo",
  "company": "Empresa Exemplo",
  "email": "pessoa@empresa.com",
  "aiTools": ["ChatGPT", "Microsoft Copilot"],
  "marketingConsent": false,
  "answers": [{ "number": 1, "dimension": "x", "tag": "Leitura", "raw": 4, "adjusted": 4 }],
  "scores": { "xRaw": 35, "yRaw": 39, "x": 63, "y": 73, "quadrant": "high-high" }
}
```

O exemplo acima é ilustrativo (a submissão real contém as 20 respostas). Ao configurar o endpoint, a interface mostra aceite obrigatório para processar a avaliação e opt-in separado para comunicações. É preciso publicar política de privacidade verdadeira e definir a finalidade, retenção, contato, exclusão e segurança dos dados antes de receber cadastros reais. **Não publique o site com dados pessoais em armazenamento improvisado ou sem controles de acesso.**

### Segurança e limitação do instrumento

- Validação de e-mail corporativo funciona por lista de provedores pessoais comuns. Ela não prova vínculo empregatício ou propriedade do domínio. Confirmar endereços com envio de e-mail exige um serviço próprio.
- A interface controla a ordem das telas, mas o conteúdo de uma aplicação front-end é inspecionável. Se o resultado precisa ser protegido contra acesso direto ou manipulação, o cálculo e a liberação devem ocorrer no servidor.
- O instrumento **não mede capacidade cognitiva objetiva**, não comprova causalidade ou dano por IA, e não é um teste psicométrico validado. O uso para avaliação individual de desempenho ou seleção profissional não é recomendado.
- Sem backend configurado, nenhuma informação é guardada. Impressão em PDF ocorre localmente no navegador.

## Notas de design

O DS original é um sistema de zines, impressos e apresentações, não uma biblioteca de componentes web. Sua linguagem foi transposta para interação: papel `#fbf8f4`, rosa `#f6b4d0`, tinta `#141414`; Cormorant Garamond, Instrument Sans e fios 1 px; zero arredondamento ou sombras (exceto os marcadores circulares da própria matriz). Ausentes os arquivos SVG oficiais, a assinatura Maia Oazem aparece em texto, como prescreve o DS.

## Arquivos

- `index.html` — site completo (funciona também de forma independente, sem servidor).
- `server.py` — servidor opcional de captação via API, gravação privada em SQLite e exportação CSV.
- `README.md` — documentação da entrega e implantação.
