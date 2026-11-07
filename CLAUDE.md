# Site Maia Oazem (gira.guru)

Site estático publicado pelo Cloudflare (Worker "maia-oazem") a partir deste repositório. Cada push na `main` vai ao ar.

## Lab aberto (`/lab`)

Toda ferramenta do lab mora em `lab/<nome>/index.html`.

Ao criar uma página nova no lab, sempre:

1. **Menu superior.** Colar o bloco abaixo logo depois da tag `<body>`, trocando `NOME-DA-FERRAMENTA` pelo nome da pasta. Ele leva à home (`/`) e ao lab (`/lab/`). Não mudar o estilo: é o mesmo em todas as ferramentas.
2. **Cartão no lab.** Adicionar um `<li class="ferramenta">` em `lab/index.html`, seguindo os cartões existentes: próximo número, uma cor do Design System, um desenho de formas primárias (linhas + uma interseção preenchida), data, descrição em PT e EN (`data-en`). Atualizar a contagem de ferramentas no topo.
3. **Links internos** sempre com o caminho completo: `/lab/<nome>/`.

```html
<nav class="lab-nav" aria-label="Navegação">
<style>
.lab-nav{position:relative;z-index:1000;display:flex;align-items:center;justify-content:space-between;gap:8px 18px;flex-wrap:wrap;margin:0;padding:10px max(16px,env(safe-area-inset-left,0px));background:#fbf8f4;color:#141414;border-bottom:1px solid #141414;font:12px/1.2 "Instrument Sans","Helvetica Neue",Arial,sans-serif;letter-spacing:.09em;text-transform:uppercase;box-sizing:border-box;width:100%}
.lab-nav a{color:inherit;text-decoration:none;border:0;display:inline-flex;align-items:center;gap:8px}
.lab-nav a:hover{opacity:.6}
.lab-nav .lab-nav-trilha{display:flex;align-items:center;gap:10px;flex-wrap:wrap}
.lab-nav .lab-nav-sep{opacity:.45}
.lab-nav .lab-nav-atual{color:#5b5754}
</style>
<span class="lab-nav-trilha">
<a href="/"><svg width="14" height="14" viewBox="0 0 100 100" aria-hidden="true"><path fill="currentColor" d="M53 8L91 72H15Z"/><path fill="currentColor" d="M43 94L9 36H77Z"/></svg>Maia Oazem</a>
<span class="lab-nav-sep" aria-hidden="true">/</span>
<a href="/lab/">lab aberto</a>
<span class="lab-nav-sep" aria-hidden="true">/</span>
<span class="lab-nav-atual" aria-current="page">NOME-DA-FERRAMENTA</span>
</span>
</nav>
```

## Design systems gerados por IA (`/lab/design-systems`)

Categoria própria no lab aberto, com contador próprio, logo depois de "ferramentas abertas". Cada design system mora em `lab/design-systems/<nome>/` e **sempre** tem:

1. **Página `index.html` com prévias ao vivo** do sistema (cenas, componentes e tokens funcionando, troca de temas/estados), escrita na linguagem do próprio design system, com o menu superior do lab (`NOME-DA-FERRAMENTA` = nome da pasta).
2. **O `.md` do sistema** na mesma pasta (`<nome>-design-system.md`): instruções para IA, princípios, tokens, CSS pronto, tipografia, componentes e ícones, num arquivo só.
3. **Cartão no `lab/index.html`** na seção "design systems gerados por IA": o cartão (capa) leva à página; o botão "baixar o .md para sua IA" baixa o arquivo (`download`). Atualizar o contador da seção.
4. Fontes do sistema servidas da própria pasta (`fonts/`, com a licença).

## Subdomínios

`_worker.js` entrega uma pasta do repositório num subdomínio (hoje: `contexto.gira.guru` → `contexto/`). Para um subdomínio novo: acrescentar a linha em `SUBDOMINIOS` dentro de `_worker.js` e adicionar o domínio no Cloudflare (Workers & Pages → maia-oazem → Settings → Domains & Routes → Add → Custom domain). Links internos dessas páginas podem ser relativos (`#secao`) ou começar pela pasta (`/contexto/...`).
