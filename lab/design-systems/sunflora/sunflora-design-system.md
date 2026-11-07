# SUN//FLORA — Design System (AI-ready)

> Design system generativo solarpunk Y3K: uma base editorial com quatro modos de existência — Ar, Fogo, Água e Terra. Feito por Maia Oazem / gira. com IA. Licença CC BY-NC-SA 4.0 (cite a gira., sem revenda). Fontes: SIL OFL 1.1.

## Como usar este arquivo com a sua IA

Cole ou anexe este .md inteiro na conversa e peça, por exemplo: *"Use o design system SUN//FLORA deste arquivo para criar uma landing page no elemento Água."* Regras para a IA:

1. Os quatro elementos são temas. Defina `data-theme="air|fire|water|earth"` no elemento raiz e use só as variáveis CSS abaixo — nunca valores soltos.
2. `ink` para texto, `ink-muted` para texto secundário, `accent-strong` para tudo que precisa ser percebido (bordas de estado, ícones, pontos), `accent` só para luz (halos, gradientes).
3. Superfície sempre quase branca; cor é luz transmitida, nunca superfície chapada dominante.
4. Três vozes tipográficas: Bodoni Moda (display), Alegreya Sans (texto), IBM Plex Mono (rótulos em CAIXA ALTA numerados "NN /").
5. Sem plantas, sem imagens estáticas: matéria é vidro, órbitas e luz desenhadas por código.

---


**Light is a living material.** SUN//FLORA é um design system generativo solarpunk Y3K: uma única base editorial com quatro modos de existência — Ar, Fogo, Água e Terra. Grid, vidro, tipografia, UI e composição são fixos; luz, cor, física e linguagem mudam em tempo real, inteiramente por código. Zero imagens estáticas, zero bibliotecas externas.

Fonte: `index.html` da V4.2 "Órbitas & Azul" (atualização da V4.0). Este sistema traduz os valores exatos do código.

## A equação

> **FIXO** — GRID + VIDRO + TIPOGRAFIA + UI + COMPOSIÇÃO
> **+ VARIÁVEL** — o elemento ativo

A identidade não é trocada por quatro estilos independentes: cada elemento executa o mesmo sistema com parâmetros próprios. Por isso os quatro elementos são **temas** de cor (`air`, `fire`, `water`, `earth`), e todo componente lê os mesmos tokens. Trocar de elemento = trocar `data-theme` no elemento raiz.

| # | Elemento | Tema | Assinatura | Fundação variável | Verbo |
|---|---|---|---|---|---|
| 01 | Ar / Air | `air` | WHITE + BLUE / LEVITY | Azul / branco + suspensão | OPEN — CREATE SPACE |
| 02 | Fogo / Fire | `fire` | PINK + YELLOW / RADIANCE | Rosa / amarelo + irradiação | IGNITE — SET INTENT |
| 03 | Água / Water | `water` | BLUE + GREEN / FLUIDITY | Azul / verde + fluidez | FLOW — ENABLE CIRCULATION |
| 04 | Terra / Earth | `earth` | GREEN + YELLOW / GROWTH | Verde / amarelo + crescimento | GROUND — BUILD A BASE |

## Princípios (gramática comum)

1. **Superfície — quase branco.** Interfaces claras e respiro. O elemento pinta a luz, não o fundo inteiro: `surface` é sempre quase branco.
2. **Matéria — vidro vivo.** Transparência, bordas especulares, gel e cromado líquido. Volume se desenha com borda, reflexo e sombra interna.
3. **Grafismo — editorial + digital.** Serifa monumental, microtexto técnico em mono, retículas, cruzes de enquadramento e filetes finos.
4. **Movimento — natureza procedural.** Órbitas, partículas e luz produzidas em Canvas. Nenhuma imagem. **Sem plantas** desde a V4.2: a ideia de crescimento existe como estado abstrato, nunca como ilustração botânica.

## Transformações por elemento (V4.2)

| Elemento | Núcleo | Anéis | Bolhas | Cor e luz |
|---|---|---|---|---|
| Ar | Sem globo | Anéis orbitais brilhantes, mesmo material da Água | Direita → esquerda | Azul-celeste reforçado com branco e prata |
| Fogo | Sem globo | Anéis orbitais brilhantes, mesmo material da Água | Baixo → cima, deriva leve à esquerda | Rosa e amarelo |
| Água | Globo translúcido | Órbitas refrativas | Suspensas e orbitais | Azul e verde |
| Terra | Apenas um globo | Surgem e desaparecem por opacidade | Sem enxame independente | Verde e amarelo |

## Cor: não cores, estados de luz

Base branca ou quase branca, cor ambiente difusa e pequenos acentos saturados. **O neon aparece nas refrações, nunca como superfície chapada dominante.**

- Seis tokens semânticos exportáveis por elemento: `surface`, `surface2` (SOFT FIELD), `diffuse`, `accent`, `highlight`, `spectrum`. No export CSS do gerador viram `--sf-surface`, `--sf-soft-field`, `--sf-diffuse`, `--sf-accent`, `--sf-highlight`, `--sf-spectrum`.
- Mais `ink` e `ink-muted` (texto), `accent-strong` (sinais de interface), `ambient-a` / `ambient-b` (halos de fundo), `art-accent`, os filetes `line` / `line-soft` / `line-strong` e os brancos de vidro `glass-fill` / `glass-tile` / `glass-edge`.
- `canvas-*`: as seis cores RGB do motor generativo (base, haze, secondary, line, glow, life).
- `element-air` / `element-fire` / `element-water` / `element-earth`: a cor de cada elemento, fixa em qualquer tema, para identificá-lo fora do próprio modo.

**Contraste (resolvido).** Cada nível de cor tem um papel, e cada papel passa no seu limite em **todos** os elementos:

| Papel | Token | Limite | Ar | Fogo | Água | Terra |
|---|---|---|---|---|---|---|
| Texto principal | `ink` sobre `surface` | 4.5:1 | 6.82 | 6.42 | 5.90 | 6.18 |
| Texto principal | `ink` sobre `surface2` | 4.5:1 | 5.66 | 5.39 | 5.20 | 5.25 |
| Texto secundário | `ink-muted` sobre `surface2` | 4.5:1 | 4.67 | 4.61 | 4.66 | 4.67 |
| Texto em botão | `white` sobre `ink` | 4.5:1 | 7.48 | 6.69 | 5.98 | 6.26 |
| Sinal de interface | `accent-strong` sobre `surface2` | 3:1 | 3.24 | 3.23 | 3.23 | 3.24 |
| Luz decorativa | `accent` | — | 3.16 | 3.06 | 2.38 | 2.65 |

- **`ink-muted`** substitui as opacidades .65–.8 da V4.2, que deixavam números e sublabels em ~2.7:1. Hierarquia agora vem de tamanho, peso e família — não de transparência.
- **`accent-strong`** (#3b7ad1 / #d64e7b / #3a9193 / #688d3c) é o mesmo matiz do accent, mais denso: vai em tudo que precisa ser *percebido* — borda de estado ativo, status-dot, thumb do slider, pílula de passo, filete do terminal, "//" da marca, contorno da tipografia de vidro.
- **`accent`** continua luminoso e livre para a luz: halos, glows, gradientes, refrações. Nunca é a única pista de nada.
- Filetes (`line*`) são decorativos: todo controle tem rótulo de texto, então a borda não é a única forma de identificá-lo. Foco é sempre um anel de 2px em `ink`.

### Gradientes (três famílias)

- **G01 Horizon** — linear 136°: branco → `surface2` → `diffuse`. Atmosfera e fundos.
- **G02 Sunfield** — radial: núcleo `highlight` + halo `ambient-b` sobre `surface2`. Radiância.
- **G03 Iridescence** — cônico: `surface2`, `ambient-a`, `highlight`, `spectrum`, `ambient-b`. Bordas prismáticas.
- Luz de fundo da página: dois halos elípticos (`ambient-a` em 5%/20%, `ambient-b` em 89%/5%), `blur-ambient` 55px, opacidade .4.
- Export prismático do gerador: `conic-gradient(from 55deg, diffuse, spectrum, #FFFFFF, highlight, diffuse)`.

## Tipografia: tecnoancestral

Palavras também são matéria — e cada voz carrega um tempo. As três famílias juntas fazem a ponte entre o que é ancestral e o que é tecnológico: a prensa de tipos móveis, a pena caligráfica e a máquina de escrever elétrica, todas renascidas como fontes variáveis e livres (SIL OFL), servidas pelo próprio sistema em `fonts/`.

**Display — Bodoni Moda** · *o ancestral*
A Didone de Giambattista Bodoni (Parma, fim do séc. XVIII) — o contraste extremo entre hastes e filetes que a V4.2 já pedia ao chamar Didot. Redesenhada por indestructible type\* como fonte variável com eixo de **tamanho óptico** (opsz 6–96) e peso (400–900): o navegador ajusta o desenho ao tamanho sozinho (`font-optical-sizing: auto`). Em 148px os filetes ficam fios de luz; em 25px engrossam para continuar legíveis. É a tipografia de vidro: a forma mais antiga do sistema, desenhada por uma máquina que a recalcula a cada tamanho. Itálico real para a segunda linha dos títulos ("Light is a *living material.*").

**Texto — Alegreya Sans** · *a ponte*
Sem serifa humanista de Juan Pablo del Peral, da Huerta Tipográfica (Argentina, 2013). Carrega o ritmo da pena caligráfica para dentro de uma letra sem serifa — terminais que afinam como bico de pena, hastes que respiram. Latino-americana, orgânica, feita para ler. Também desenha a marca, em ExtraBold 800. Usa algarismos alinhados na interface (`lining-nums`), porque os de estilo antigo transformam "M01" em "Mo1".

**Mono — IBM Plex Mono** · *o tecnológico*
De Mike Abbink com a Bold Monday (2017), desenhada em torno da relação entre ser humano e máquina e herdeira das letras da IBM Selectric, a máquina de escrever elétrica de esfera. É a voz dos comandos, dos rótulos numerados e dos microdados. Mais densa que a Courier New, mantém 9–10px legíveis e por isso usa tracking menor (.04–.14em em vez de .065–.19em).

**Ajustes de escala** com as novas fontes: tracking do display de −0.066 → −0.035em (a Bodoni Moda já é justa), texto de leitura +1px (lead 16, corpo 14, pequeno 13) para compensar o x-height menor da Alegreya. Títulos usam `clamp()` no código (ex.: hero 66–148px); os tamanhos nos tokens são o máximo. Arquivos: subconjunto Latin (todos os acentos do português), ~270 KB no total.

**Tipografia de vidro**: a Bodoni com preenchimento transparente, contorno 1px `accent-strong` e sombras brancas — só em escala display, sempre com `aria-hidden` e o texto real em outro lugar.

## Conteúdo e voz

- **Bilíngue, com papéis definidos.** Títulos editoriais em inglês ("Four ways of *becoming.*", "Useful *magic.*", "Install *the light.*"); explicações em português; rótulos técnicos em inglês caixa alta. Nomes dos elementos em PT com EN de apoio (AR / AIR).
- **Numeração em tudo.** Seções "00 / GRAMÁTICA COMUM" → "07 / DESIGN HANDOFF"; elementos 01–04; materiais M01–M03; gradientes G01–G03; tipos T01. Formato "NN / NOME".
- **Pares "BASE FIXA / … " × "TRANSFORMAÇÃO ELEMENTAL / …"** explicam cada seção.
- **Verbos de comando**: "VERBO — AÇÃO" (OPEN — CREATE SPACE, IGNITE — SET INTENT, FLOW — ENABLE CIRCULATION, NURTURE — FEED GROWTH). Quatro palavras por elemento na arte: Ar CIRCULATE / BREATHE / ELEVATE / CONNECT; Fogo IGNITE / RADIATE / TRANSFORM / CREATE; Água FLOW / PURIFY / NOURISH / REGENERATE; Terra GROUND / NURTURE / CULTIVATE / REGENERATE.
- **Glifos**: ↗ (abrir, gerar), ↓ (baixar), ↑ (voltar), ✦ spark (separador e marca), "+" cruzes de enquadramento, "//" e "∆".
- **Status de terminal**: "> AÇÃO / DETALHE" em caixa alta.

## Forma, espaço e matéria

- **Raios pequenos e precisos** (`radius-4` … `radius-8`) para a estrutura editorial; **pílula** (`radius-pill`) para navegação e badges; **20px** (`radius-glass`) só para o card de vidro.
- **Grid**: container de 1360px com gutter de 42px; laboratório em 1.6fr / 1fr; grades de 4 (elementos, fundação), 6 (paleta) e 3 (materiais, painéis). Gaps de 5–12px.
- **Filetes, não caixas pesadas**: bordas de 1px em `ink` a 17–35%.
- **Vidro**: `glass-fill` + `glass-edge` + `blur-glass` com saturate; sempre sobre luz, nunca sobre `surface` chapado.
- **Sombras** suaves e tingidas (`shadow-*`): ink a 4–8%, accent a 14%.
- **Movimento**: transição de tema .7s; órbitas 13s / 21s; gel 6–8s; respiração do título 7s. Tudo para com o botão PAUSE (`data-playing=false`) e com `prefers-reduced-motion`.

## Iconografia

Cinco ícones de traço em grade 24×24, `stroke-width` 1.8, pontas e junções arredondadas, sem preenchimento: **spark** (marca e separador) e um por elemento — **air** (três círculos concêntricos com opacidade decrescente), **fire** (chama dupla), **water** (três ondas), **earth** (broto de duas folhas; o único traço botânico que permanece, como símbolo de interface). No código os ícones são SVG inline em `currentColor`, então herdam `ink` ou `accent`. Ver o grupo de assets **Icones**.

## Motor generativo

A cena principal e as quatro miniaturas são desenhadas em Canvas 2D por seed: gradientes, fitas Bézier, esferas refrativas, anéis orbitais, partículas e reflexos. Parâmetros (`generator`): GLASS / REFRACTION .72, LIGHT / BLOOM .68, LIFE / DENSITY .54, MOTION / PULSE .40. Exporta PNG e CSS.

## Componentes

Marca (Wordmark), Navegação (ModeSwitch, ModeButton), Ações (Button), Controles (RangeControl, TerminalStatus), Vidro (InstructionCard), Matéria (Orbit, Materials), Cor & luz (LightPanel, Swatch), Editorial (RulePair, FoundationTile, SectionIdentity), Tipografia (GlassType). As prévias usam `components/bundle.css`, portado 1:1 do `index.html`; envolva qualquer superfície em `.sf`.

---

# Tokens

## Cores por elemento

| Token | 01 Ar | 02 Fogo | 03 Água | 04 Terra | Uso |
|---|---|---|---|---|---|
| `surface` | `#eef5ff` | `#fff9f9` | `#f7ffff` | `#fbfff5` | Fundo da página. Quase branco: o elemento pinta a luz, não o fundo inteiro. Export: --sf-surface. |
| `surface2` | `#cce2ff` | `#ffdeef` | `#d8f4fa` | `#e1f1c8` | Campo suave (SOFT FIELD): estado ativo de botões, cards de elemento, fundo de painéis de luz. Ink passa 4.5:1 sobre ele em todos os elementos. Export: --sf-soft-field. |
| `diffuse` | `#90bfff` | `#ffd1b5` | `#baf0dd` | `#ecf6b1` | Cor ambiente difusa: fim de gradientes de atmosfera e trilho do slider. Nunca superfície chapada, nunca texto. Export: --sf-diffuse. |
| `accent` | `#548bd7` | `#dd6b91` | `#4cb6b9` | `#7eab49` | Acento luminoso: halos, glows, gradientes, trilho do slider, refrações. Decorativo — fica abaixo de 3:1 em Água (2.38) e Terra (2.65). Tudo que precisa ser percebido (borda de estado, ícone, ponto, traço de marca) usa accent-strong. Export: --sf-accent. |
| `accent-strong` | `#3b7ad1` | `#d64e7b` | `#3a9193` | `#688d3c` | Accent com contraste de interface: bordas de estado ativo, status-dot, thumb do slider, pílula de passo, filete do terminal, "//" da marca, contorno da tipografia de vidro. Mesmo matiz do accent, mais escuro: ≥3.2:1 sobre surface2, ≥3.6:1 sobre surface e branco em todos os elementos. Não é cor de texto corrido. |
| `highlight` | `#e0efff` | `#fff1a9` | `#dcfff0` | `#fff3ab` | Núcleo de brilho: centro do gradiente Sunfield e reflexos. Export: --sf-highlight. |
| `spectrum` | `#9cc7ff` | `#ffbad8` | `#8cdbef` | `#bde690` | Tom espectral das refrações: corpo do gel, orbe e gradiente prismático. Export: --sf-spectrum. |
| `ink` | `#36577b` | `#894762` | `#296c78` | `#4b6841` | Texto, ícones, linhas e fundo do botão principal. Contraste sobre surface: 6.82 / 6.42 / 5.90 / 6.18; sobre surface2 ≥5.2 em todos. |
| `ink-muted` | `#456486` | `#91536d` | `#33737f` | `#54704a` | Texto secundário (números de tile, sublabels EN, rótulos de regra). Substitui as opacidades .65–.8 da V4.2, que caíam para ~2.7:1. Passa ≥4.6:1 sobre surface2 e ≥5.3:1 sobre surface em todos os elementos. Não usar sobre vidro em Ar (use ink). |
| `ambient-a` | `#80b6ff` | `#ffc5d9` | `#b7e9ff` | `#ccebab` | Halo ambiente A: luz difusa de fundo (canto superior esquerdo, blur 55px, opacidade .4) e fundo do component-stage. |
| `ambient-b` | `#d1e5ff` | `#ffeab9` | `#c9ffe3` | `#fff3b3` | Halo ambiente B: segundo foco de luz difusa (canto superior direito) e reflexos internos do gel/orbe. |
| `art-accent` | `#a2c6f3` | `#ffabbc` | `#95e6d9` | `#bee875` | Acento reservado à arte generativa (canvas). |
| `line` | `#36577b3b` | `#8947623b` | `#296c783b` | `#4b68413b` | Filete padrão (ink a ~23%; no código: color-mix(ink, transparent 77%)). Bordas de botões de modo, swatches, divisórias de status. |
| `line-soft` | `#36577b2b` | `#8947622b` | `#296c782b` | `#4b68412b` | Filete discreto (ink a ~17%): bordas de tiles de material, header, footer, caption. |
| `line-strong` | `#36577b59` | `#89476259` | `#296c7859` | `#4b684159` | Filete forte (ink a ~35%): topo do laboratório, botão CTA do header. |
| `white` | `#ffffff` | `#ffffff` | `#ffffff` | `#ffffff` | Branco puro: texto sobre ink (7.48 / 6.69 / 5.98 / 6.26), thumb do slider, bordas especulares. |
| `glass-fill` | `rgba(255,255,255,0.39)` | `rgba(255,255,255,0.39)` | `rgba(255,255,255,0.39)` | `rgba(255,255,255,0.39)` | Preenchimento de vidro do card de instrução (com backdrop blur 22px + saturate 1.7). Texto ink sobre ele herda o contraste do fundo atrás. |
| `glass-tile` | `rgba(255,255,255,0.45)` | `rgba(255,255,255,0.45)` | `rgba(255,255,255,0.45)` | `rgba(255,255,255,0.45)` | Botões e tiles translúcidos em repouso (mode-button, botões secundários, step-progress). |
| `glass-edge` | `rgba(255,255,255,0.91)` | `rgba(255,255,255,0.91)` | `rgba(255,255,255,0.91)` | `rgba(255,255,255,0.91)` | Borda especular do vidro: card de instrução, painéis de luz, live preview. |
| `canvas-base` | `rgb(226,239,255)` | `rgb(255,248,249)` | `rgb(246,254,255)` | `rgb(251,255,247)` | Canvas: cor-base da cena generativa. |
| `canvas-haze` | `rgb(112,170,250)` | `rgb(255,172,199)` | `rgb(135,211,240)` | `rgb(177,221,135)` | Canvas: névoa/haze principal. |
| `canvas-secondary` | `rgb(162,204,255)` | `rgb(255,232,167)` | `rgb(182,249,206)` | `rgb(253,239,166)` | Canvas: cor secundária (segundo halo, partículas). |
| `canvas-line` | `rgb(84,139,215)` | `rgb(225,107,145)` | `rgb(76,182,185)` | `rgb(126,171,73)` | Canvas: linhas, fitas Bézier e anéis orbitais. |
| `canvas-glow` | `rgb(222,241,255)` | `rgb(255,243,182)` | `rgb(227,255,244)` | `rgb(255,250,207)` | Canvas: brilho dos reflexos e bolhas. |
| `canvas-life` | `rgb(107,178,148)` | `rgb(172,180,100)` | `rgb(74,172,115)` | `rgb(82,150,83)` | Canvas: cor de "vida" do motor (antes usada nas plantas, removidas na V4.2). Mantida no motor; sem uso visível obrigatório. |
| `element-air` | `#548bd7` | `#548bd7` | `#548bd7` | `#548bd7` | Cor fixa de identificação de Ar, igual em qualquer atmosfera ativa (= accent de Ar). Para marcar um elemento fora do seu próprio tema: seletores, legendas, capa. Nunca texto. |
| `element-fire` | `#dd6b91` | `#dd6b91` | `#dd6b91` | `#dd6b91` | Cor fixa de identificação de Fogo, igual em qualquer atmosfera ativa (= accent de Fogo). Para marcar um elemento fora do seu próprio tema: seletores, legendas, capa. Nunca texto. |
| `element-water` | `#4cb6b9` | `#4cb6b9` | `#4cb6b9` | `#4cb6b9` | Cor fixa de identificação de Água, igual em qualquer atmosfera ativa (= accent de Água). Para marcar um elemento fora do seu próprio tema: seletores, legendas, capa. Nunca texto. |
| `element-earth` | `#7eab49` | `#7eab49` | `#7eab49` | `#7eab49` | Cor fixa de identificação de Terra, igual em qualquer atmosfera ativa (= accent de Terra). Para marcar um elemento fora do seu próprio tema: seletores, legendas, capa. Nunca texto. |

## CSS pronto (copie para o seu projeto)

```css
/* Fontes — Google Fonts (mesmas famílias servidas no DS) */
@import url('https://fonts.googleapis.com/css2?family=Alegreya+Sans:ital,wght@0,400;0,500;0,700;0,800;1,400&family=Bodoni+Moda:ital,opsz,wght@0,6..96,400..900;1,6..96,400..900&family=IBM+Plex+Mono:wght@400;500;600&display=swap');

:root, [data-theme="air"] {
  --surface: #eef5ff;
  --surface2: #cce2ff;
  --diffuse: #90bfff;
  --accent: #548bd7;
  --accent-strong: #3b7ad1;
  --highlight: #e0efff;
  --spectrum: #9cc7ff;
  --ink: #36577b;
  --ink-muted: #456486;
  --ambient-a: #80b6ff;
  --ambient-b: #d1e5ff;
  --art-accent: #a2c6f3;
  --line: #36577b3b;
  --line-soft: #36577b2b;
  --line-strong: #36577b59;
  --white: #ffffff;
  --glass-fill: rgba(255,255,255,0.39);
  --glass-tile: rgba(255,255,255,0.45);
  --glass-edge: rgba(255,255,255,0.91);
  --canvas-base: rgb(226,239,255);
  --canvas-haze: rgb(112,170,250);
  --canvas-secondary: rgb(162,204,255);
  --canvas-line: rgb(84,139,215);
  --canvas-glow: rgb(222,241,255);
  --canvas-life: rgb(107,178,148);
  --element-air: #548bd7;
  --element-fire: #dd6b91;
  --element-water: #4cb6b9;
  --element-earth: #7eab49;
  --shadow-artwork: 0 18px 55px rgba(54,87,123,0.08);
  --shadow-glass-card: inset 0 1px 0 rgba(255,255,255,0.85), 0 20px 42px rgba(84,139,215,0.14);
  --shadow-nav: 0 8px 24px rgba(54,87,123,0.04);
  --shadow-active: inset 0 1px 0 rgba(255,255,255,0.8), 0 0 0 1px #3b7ad1;
  --shadow-dot: 0 0 0 4px rgba(84,139,215,0.14), 0 0 15px rgba(84,139,215,1);
  --shadow-panel: 0 9px 30px rgba(54,87,123,0.04);
}
[data-theme="fire"] {
  --surface: #fff9f9;
  --surface2: #ffdeef;
  --diffuse: #ffd1b5;
  --accent: #dd6b91;
  --accent-strong: #d64e7b;
  --highlight: #fff1a9;
  --spectrum: #ffbad8;
  --ink: #894762;
  --ink-muted: #91536d;
  --ambient-a: #ffc5d9;
  --ambient-b: #ffeab9;
  --art-accent: #ffabbc;
  --line: #8947623b;
  --line-soft: #8947622b;
  --line-strong: #89476259;
  --white: #ffffff;
  --glass-fill: rgba(255,255,255,0.39);
  --glass-tile: rgba(255,255,255,0.45);
  --glass-edge: rgba(255,255,255,0.91);
  --canvas-base: rgb(255,248,249);
  --canvas-haze: rgb(255,172,199);
  --canvas-secondary: rgb(255,232,167);
  --canvas-line: rgb(225,107,145);
  --canvas-glow: rgb(255,243,182);
  --canvas-life: rgb(172,180,100);
  --element-air: #548bd7;
  --element-fire: #dd6b91;
  --element-water: #4cb6b9;
  --element-earth: #7eab49;
  --shadow-artwork: 0 18px 55px rgba(137,71,98,0.08);
  --shadow-glass-card: inset 0 1px 0 rgba(255,255,255,0.85), 0 20px 42px rgba(221,107,145,0.14);
  --shadow-nav: 0 8px 24px rgba(137,71,98,0.04);
  --shadow-active: inset 0 1px 0 rgba(255,255,255,0.8), 0 0 0 1px #d64e7b;
  --shadow-dot: 0 0 0 4px rgba(221,107,145,0.14), 0 0 15px rgba(221,107,145,1);
  --shadow-panel: 0 9px 30px rgba(54,87,123,0.04);
}
[data-theme="water"] {
  --surface: #f7ffff;
  --surface2: #d8f4fa;
  --diffuse: #baf0dd;
  --accent: #4cb6b9;
  --accent-strong: #3a9193;
  --highlight: #dcfff0;
  --spectrum: #8cdbef;
  --ink: #296c78;
  --ink-muted: #33737f;
  --ambient-a: #b7e9ff;
  --ambient-b: #c9ffe3;
  --art-accent: #95e6d9;
  --line: #296c783b;
  --line-soft: #296c782b;
  --line-strong: #296c7859;
  --white: #ffffff;
  --glass-fill: rgba(255,255,255,0.39);
  --glass-tile: rgba(255,255,255,0.45);
  --glass-edge: rgba(255,255,255,0.91);
  --canvas-base: rgb(246,254,255);
  --canvas-haze: rgb(135,211,240);
  --canvas-secondary: rgb(182,249,206);
  --canvas-line: rgb(76,182,185);
  --canvas-glow: rgb(227,255,244);
  --canvas-life: rgb(74,172,115);
  --element-air: #548bd7;
  --element-fire: #dd6b91;
  --element-water: #4cb6b9;
  --element-earth: #7eab49;
  --shadow-artwork: 0 18px 55px rgba(41,108,120,0.08);
  --shadow-glass-card: inset 0 1px 0 rgba(255,255,255,0.85), 0 20px 42px rgba(76,182,185,0.14);
  --shadow-nav: 0 8px 24px rgba(41,108,120,0.04);
  --shadow-active: inset 0 1px 0 rgba(255,255,255,0.8), 0 0 0 1px #3a9193;
  --shadow-dot: 0 0 0 4px rgba(76,182,185,0.14), 0 0 15px rgba(76,182,185,1);
  --shadow-panel: 0 9px 30px rgba(54,87,123,0.04);
}
[data-theme="earth"] {
  --surface: #fbfff5;
  --surface2: #e1f1c8;
  --diffuse: #ecf6b1;
  --accent: #7eab49;
  --accent-strong: #688d3c;
  --highlight: #fff3ab;
  --spectrum: #bde690;
  --ink: #4b6841;
  --ink-muted: #54704a;
  --ambient-a: #ccebab;
  --ambient-b: #fff3b3;
  --art-accent: #bee875;
  --line: #4b68413b;
  --line-soft: #4b68412b;
  --line-strong: #4b684159;
  --white: #ffffff;
  --glass-fill: rgba(255,255,255,0.39);
  --glass-tile: rgba(255,255,255,0.45);
  --glass-edge: rgba(255,255,255,0.91);
  --canvas-base: rgb(251,255,247);
  --canvas-haze: rgb(177,221,135);
  --canvas-secondary: rgb(253,239,166);
  --canvas-line: rgb(126,171,73);
  --canvas-glow: rgb(255,250,207);
  --canvas-life: rgb(82,150,83);
  --element-air: #548bd7;
  --element-fire: #dd6b91;
  --element-water: #4cb6b9;
  --element-earth: #7eab49;
  --shadow-artwork: 0 18px 55px rgba(75,104,65,0.08);
  --shadow-glass-card: inset 0 1px 0 rgba(255,255,255,0.85), 0 20px 42px rgba(126,171,73,0.14);
  --shadow-nav: 0 8px 24px rgba(75,104,65,0.04);
  --shadow-active: inset 0 1px 0 rgba(255,255,255,0.8), 0 0 0 1px #688d3c;
  --shadow-dot: 0 0 0 4px rgba(126,171,73,0.14), 0 0 15px rgba(126,171,73,1);
  --shadow-panel: 0 9px 30px rgba(54,87,123,0.04);
}
:root {
  --space-5: 5px;
  --space-7: 7px;
  --space-12: 12px;
  --space-20: 20px;
  --space-24: 24px;
  --space-28: 28px;
  --space-35: 35px;
  --space-42: 42px;
  --space-98: 98px;
  --container: 1360px;
  --radius-4: 4px;
  --radius-5: 5px;
  --radius-6: 6px;
  --radius-7: 7px;
  --radius-8: 8px;
  --radius-glass: 20px;
  --radius-pill: 99px;
  --blur-glass: 22px;
  --blur-panel: 14px;
  --blur-material: 12px;
  --blur-ambient: 55px;
  --glass-refraction: 0.72;
  --light-bloom: 0.68;
  --life-density: 0.54;
  --motion-pulse: 0.40;
  --font-display: 'Bodoni Moda', Didot, 'Bodoni MT', Georgia, serif;
  --font-sans: 'Alegreya Sans', 'Segoe UI', Arial, sans-serif;
  --font-mono: 'IBM Plex Mono', 'Courier New', monospace;
}
```

## Tipografia

| Estilo | Família | Tamanho | Entrelinha | Peso | Tracking | Uso |
|---|---|---|---|---|---|---|
| `glass-title` | display | 244px | 1.2 | 400 | -0.06em | Título translúcido central da cena (clamp 115–244px). Texto transparente + stroke do accent + gradiente branco/accent. Ar 244, Fogo 200, Água/Terra 168px máx. |
| `hero` | display | 148px | 0.81 | 400 | -0.035em | H1 de abertura (clamp 66–148px). Segunda linha em itálico (em). |
| `section` | display | 110px | 0.84 | 400 | -0.035em | H2 de seção (clamp 60–110px). |
| `foundation` | display | 95px | 0.89 | 400 | -0.035em | H2 da gramática comum (clamp 55–95px). |
| `panel` | display | 70px | 0.9 | 400 | -0.035em | Título do painel de controle (clamp 48–70px). |
| `panel-word` | display | 43px | 1 | 400 | -0.03em | Nome dos painéis de luz (Horizon, Sunfield, Iridescence). |
| `tile-title` | display | 31px | 1.1 | 400 | -0.02em | Título dos tiles de fundação. |
| `micro-heading` | display | 25px | 1.2 | 400 | -0.015em | Subtítulo editorial dentro de seção. |
| `wordmark` | sans | 25px | 1 | 800 | -0.04em | Marca. "//" em accent e peso 500. |
| `lead` | sans | 16px | 1.65 | 400 | 0 | Parágrafo de abertura de seção (max 320–420px). |
| `control-value` | sans | 20px | 1.2 | 500 | -0.04em | Elemento ativo no painel de status. |
| `button-label` | sans | 16px | 1.1 | 500 | 0 | Nome do elemento no mode-button. |
| `body` | sans | 14px | 1.65 | 400 | 0 | Texto de cards e regras. |
| `small` | sans | 13px | 1.6 | 400 | 0 | Notas e descrições de tile. |
| `code` | mono | 12px | 1.95 | 400 | 0 | Prévia de tokens / handoff. |
| `button-mono` | mono | 11px | 1.2 | 400 | 0.04em | Rótulo de botões de ação (sempre CAIXA ALTA). |
| `label` | mono | 10px | 1.65 | 400 | 0.08em | Identidade de seção, mini-labels, nav. Sempre CAIXA ALTA com numeração "NN /". |
| `kicker` | mono | 10px | 1.4 | 400 | 0.14em | Kicker de abertura e header (tracking largo). |
| `micro` | mono | 9px | 1.8 | 400 | 0.1em | Notas flutuantes da arte e sublabels. Tamanho mínimo do sistema. |

## Espaçamento

| Token | Valor | Uso |
|---|---|---|
| `space-5` | `5px` | Gap dos seletores de elemento (grade 4×). |
| `space-7` | `7px` | Gap entre botões de ação. |
| `space-12` | `12px` | Gap de grades de cards (elementos, materiais, painéis). |
| `space-20` | `20px` | Padding de painéis e regra; gap do layout do laboratório. |
| `space-24` | `24px` | Padding do card de instrução de vidro. |
| `space-28` | `28px` | Padding do painel de controles. |
| `space-35` | `35px` | Margem interna da arte (cruzes, topo e rodapé); padding do code preview. |
| `space-42` | `42px` | Gutter lateral do header e do container (100% − 84px). |
| `space-98` | `98px` | Respiro vertical entre seções (66px no mobile). |
| `container` | `1360px` | Largura máxima do section-container. |

## Raios

| Token | Valor | Uso |
|---|---|---|
| `radius-4` | `4px` | Botões de handoff, demo de material. |
| `radius-5` | `5px` | Mode-button, element-card, swatch, botões de ação. |
| `radius-6` | `6px` | Tiles de material, painéis de luz, live preview, type showcase. |
| `radius-7` | `7px` | Arte principal, painel de controles, code preview. |
| `radius-8` | `8px` | Component stage. |
| `radius-glass` | `20px` | Card de instrução de vidro (19px na arte; 14px no mobile). |
| `radius-pill` | `99px` | Nav global, CTA do header, step-progress, badges. |

## Blur

| Token | Valor | Uso |
|---|---|---|
| `blur-glass` | `22px` | Card de instrução e nav global (com saturate 1.7 / 1.4). |
| `blur-panel` | `14px` | Painel de controles. |
| `blur-material` | `12px` | Material M01 Clear glass. |
| `blur-ambient` | `55px` | Halos ambientes de fundo. |

## Parâmetros do gerador

| Token | Valor | Uso |
|---|---|---|
| `glass-refraction` | `0.72` | GLASS / REFRACTION. |
| `light-bloom` | `0.68` | LIGHT / BLOOM. |
| `life-density` | `0.54` | LIFE / DENSITY. |
| `motion-pulse` | `0.40` | MOTION / PULSE. |

## Sombras

| Token | 01 Ar | 02 Fogo | 03 Água | 04 Terra | Uso |
|---|---|---|---|---|---|
| `shadow-artwork` | `0 18px 55px rgba(54,87,123,0.08)` | `0 18px 55px rgba(137,71,98,0.08)` | `0 18px 55px rgba(41,108,120,0.08)` | `0 18px 55px rgba(75,104,65,0.08)` | Painel da arte generativa (ink a 8%). |
| `shadow-glass-card` | `inset 0 1px 0 rgba(255,255,255,0.85), 0 20px 42px rgba(84,139,215,0.14)` | `inset 0 1px 0 rgba(255,255,255,0.85), 0 20px 42px rgba(221,107,145,0.14)` | `inset 0 1px 0 rgba(255,255,255,0.85), 0 20px 42px rgba(76,182,185,0.14)` | `inset 0 1px 0 rgba(255,255,255,0.85), 0 20px 42px rgba(126,171,73,0.14)` | Card de instrução de vidro: luz especular no topo + sombra tingida pelo accent. |
| `shadow-nav` | `0 8px 24px rgba(54,87,123,0.04)` | `0 8px 24px rgba(137,71,98,0.04)` | `0 8px 24px rgba(41,108,120,0.04)` | `0 8px 24px rgba(75,104,65,0.04)` | Navegação global sticky. |
| `shadow-active` | `inset 0 1px 0 rgba(255,255,255,0.8), 0 0 0 1px #3b7ad1` | `inset 0 1px 0 rgba(255,255,255,0.8), 0 0 0 1px #d64e7b` | `inset 0 1px 0 rgba(255,255,255,0.8), 0 0 0 1px #3a9193` | `inset 0 1px 0 rgba(255,255,255,0.8), 0 0 0 1px #688d3c` | Estado ativo de mode-button: anel de 1px em accent-strong, somado à borda — o ativo fica a ≥3.2:1 do fundo. |
| `shadow-dot` | `0 0 0 4px rgba(84,139,215,0.14), 0 0 15px rgba(84,139,215,1)` | `0 0 0 4px rgba(221,107,145,0.14), 0 0 15px rgba(221,107,145,1)` | `0 0 0 4px rgba(76,182,185,0.14), 0 0 15px rgba(76,182,185,1)` | `0 0 0 4px rgba(126,171,73,0.14), 0 0 15px rgba(126,171,73,1)` | Halo do status-dot (sinal LIVE). |
| `shadow-panel` | `0 9px 30px rgba(54,87,123,0.04)` | `0 9px 30px rgba(54,87,123,0.04)` | `0 9px 30px rgba(54,87,123,0.04)` | `0 9px 30px rgba(54,87,123,0.04)` | Painel de controles do laboratório. |

---

# Componentes

## Button

Botões de comando: retangulares, rótulo mono em caixa alta e um glifo direcional (↗ abrir/gerar, ↓ baixar).

- **Principal** (`action-main`): fundo `ink`, texto `white`, ícone à esquerda e seta à direita, altura 48px, `radius-5`. Um por grupo.
- **Fantasma** (`action-ghost`): transparente, borda `ink`. Para alternâncias (PAUSE/PLAY).
- **Secundário**: fundo `glass-tile`, borda `line-strong`. Exportações.
- **Handoff** (`code-buttons`): 45px, `radius-4`; o primeiro preenchido em `ink`.
- Rótulos são verbos de comando curtos: NEW GENERATION, EXPORT, COPY, DOWNLOAD.

```html
<div class="sf" style="padding:28px;display:grid;gap:16px;max-width:520px">
<div class="control-actions"><button type="button" class="action-main"><span class="icon-glyph" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M12 2.5v6.5M12 15v6.5M2.5 12H9M15 12h6.5M5.2 5.2l4.2 4.2M14.6 14.6l4.2 4.2M18.8 5.2l-4.2 4.2M9.4 14.6l-4.2 4.2"/></svg></span> NEW GENERATION <span>↗</span></button><button type="button" class="action-ghost">Ⅱ PAUSE</button></div>
<div class="control-actions secondary-actions"><button type="button">EXPORT PNG ↓</button><button type="button">EXPORT CSS ↓</button></div>
<div class="code-buttons"><button type="button">COPY CSS <span>↗</span></button><button type="button">DOWNLOAD JSON <span>↓</span></button></div>
</div>
```

## FoundationTile

Tile da gramática comum: número + domínio em mono, conceito em serifa display e uma frase de definição.

- 4 colunas (2 abaixo de 1050px, 1 abaixo de 370px); `radius-6`; gradiente branco 75→20%.
- Usado para os princípios invariantes; um tile = um princípio.

```html
<div class="sf" style="padding:20px">
<div class="foundation-grid">
<div><span>01 / SUPERFÍCIE</span><b>Quase branco</b><p>Interfaces claras e respiro. O elemento pinta a luz, não o fundo inteiro.</p></div>
<div><span>02 / MATÉRIA</span><b>Vidro vivo</b><p>Transparência, bordas especulares, gel e cromado líquido.</p></div>
<div><span>03 / GRAFISMO</span><b>Editorial + digital</b><p>Serifa monumental, microtexto técnico, retículas e linhas finas.</p></div>
<div><span>04 / MOVIMENTO</span><b>Natureza procedural</b><p>Órbitas, partículas e luz produzidas em Canvas; nenhuma imagem.</p></div>
</div></div>
```

## GlassType

Tipografia de vidro: a serifa display vira matéria — preenchimento quase transparente, contorno de 1px em `accent-strong` e sombras brancas em camadas.

- Use só em escala display (≥ 48px) e em fundo claro com luz; nunca para texto de leitura.
- Por ser decorativa e de baixo contraste, sempre tenha o mesmo texto acessível em outro lugar (`aria-hidden` na versão de vidro).
- Frases por elemento: "air / becoming", "fire / radiate", "water / flow", "earth / grow".

```html
<div class="sf" style="padding:24px 28px;background:linear-gradient(140deg,rgba(255,255,255,.8),var(--surface2))">
<span class="sf-mono" style="font-size:10px">T01 / TRANSLUCENT DISPLAY</span>
<div class="type-display">air / becoming</div>
<p class="sf-mono" style="font-size:10px;margin:8px 0 0">EDITORIAL SERIF / VIDRO ÓPTICO / BRILHO EM CAMADAS</p>
</div>
```

## InstructionCard

Digital Instruction Box: card de vidro que organiza informação sem competir com a matéria — contorno fino, fundo translúcido, numeração precisa e microinteração.

- Vidro: `glass-fill` + borda `glass-edge` + `shadow-glass-card` + `blur-glass` com saturate 1.7; `radius-glass` (20px).
- Estrutura fixa: cabeçalho (ícone do elemento · "ELEMENTO / SYSTEM INSTRUCTION" · contador "01 / 04"), frase-nota em Alegreya Sans 15px, linha de comando (passo em pílula `accent-strong` · "VERBO — AÇÃO" · ↗) e o seletor de 4 passos.
- Texto sempre em `ink` (não `ink-muted`): sobre o vidro em Ar o fundo escurece com o halo `ambient-a` e só `ink` mantém 4.8:1.
- Só funciona sobre fundo com luz (o `stage` com os halos `ambient-a`/`ambient-b`); sobre `surface` chapado o vidro desaparece.
- Os verbos mudam por elemento: Ar OPEN/BREATHE/CIRCULATE/CONNECT; Fogo IGNITE/TRANSFORM/RADIATE/CREATE; Água FLOW/PURIFY/NOURISH/REGENERATE; Terra GROUND/NURTURE/CULTIVATE/REGENERATE.

```html
<div class="sf stage">
<div class="component-card" style="max-width:420px">
<div class="component-card-head"><span class="icon-glyph" aria-hidden="true"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="5.2"/><circle cx="12" cy="12" r="8.6" opacity=".72"/><circle cx="12" cy="12" r="11" opacity=".42"/></svg></span><strong>AIR / SYSTEM INSTRUCTION</strong><span>01 / 04</span></div>
<p>A atmosfera constrói espaço e circulação.</p>
<div class="component-command"><span class="component-step">01</span><span>OPEN — CREATE SPACE</span><span aria-hidden="true">↗</span></div>
<div class="step-progress" role="group" aria-label="Escolher instrução"><button type="button" aria-pressed="true">01</button><button type="button" aria-pressed="false">02</button><button type="button" aria-pressed="false">03</button><button type="button" aria-pressed="false">04</button></div>
</div></div>
<script>(function(){var s=['OPEN — CREATE SPACE','BREATHE — RESET RHYTHM','CIRCULATE — MOVE ENERGY','CONNECT — SHARE THE FLOW'];var b=document.querySelectorAll('.step-progress button');b.forEach(function(x,i){x.addEventListener('click',function(){b.forEach(function(y){y.setAttribute('aria-pressed',String(y===x))});document.querySelector('.component-step').textContent='0'+(i+1);document.querySelector('.component-command span:nth-child(2)').textContent=s[i]})})})()</script>
```

## LightPanel

As três famílias de gradiente: a cor do sistema é luz transmitida, não superfície.

- **G01 Horizon** (linear 136°): branco → `surface2` → `diffuse`. Fundos e atmosfera.
- **G02 Sunfield** (radial): núcleo `highlight` + halo `ambient-b` sobre `surface2`. Radiância.
- **G03 Iridescence** (cônico): `surface2`, `ambient-a`, `highlight`, `spectrum`, `ambient-b`. Só em bordas e refrações.
- Todo painel leva a elipse especular branca girada −23°.
- O neon aparece nas refrações, nunca como superfície dominante.

```html
<div class="sf" style="padding:20px">
<div class="light-panels">
<article class="light-panel gradient-atmosphere"><div>G01 / DIFFUSE ATMOSPHERE</div><b>Horizon</b><span>BACKGROUND / SOFT LIGHT</span></article>
<article class="light-panel gradient-sun"><div>G02 / RADIANT BLOOM</div><b>Sunfield</b><span>RADIANCE / SOFT CORE</span></article>
<article class="light-panel gradient-prism"><div>G03 / PRISMATIC EDGES</div><b>Iridescence</b><span>REFRACTION / CHROMATIC</span></article>
</div></div>
```

## Materials

Os três materiais vítreos: volume desenhado por borda, reflexo, sombra interna e transmissividade simulada — nunca por cor chapada.

- **M01 Clear glass**: losango arredondado (radius 35%), gradiente branco 50→8→46%, `blur-material`, borda branca 94%.
- **M02 Liquid gel**: blob assimétrico em `spectrum`, brilho branco e sombra interna tingida de `accent`.
- **M03 Living chrome**: esfera prata com `spectrum`, `accent` e um ponto de `ink` na base.
- Gel e cromo flutuam (6–8s, alternate); param com o PAUSE e com `prefers-reduced-motion`.

```html
<div class="sf" style="padding:20px">
<div class="material-grid">
<div class="material-tile"><div class="material-demo clear-demo"><div class="material-glass"><span class="icon-glyph" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M12 2.5v6.5M12 15v6.5M2.5 12H9M15 12h6.5M5.2 5.2l4.2 4.2M14.6 14.6l4.2 4.2M18.8 5.2l-4.2 4.2M9.4 14.6l-4.2 4.2"/></svg></span></div></div><div><strong>M01 — Clear glass</strong><span>BLUR + EDGE LIGHT</span></div></div>
<div class="material-tile"><div class="material-demo gel-demo"><div class="material-gel"></div></div><div><strong>M02 — Liquid gel</strong><span>REFRACTION + PEARL</span></div></div>
<div class="material-tile"><div class="material-demo sphere-demo"><div class="material-sphere"></div></div><div><strong>M03 — Living chrome</strong><span>SILVER + SPECTRUM</span></div></div>
</div></div>
```

## ModeButton

Tile seletor de elemento do painel de controle: número mono, nome em português e nome em inglês.

- Grade de 4 colunas com `space-5` de gap; `radius-5`; borda `line`; fundo `glass-tile`.
- Ativo: `surface2` + borda `accent-strong` + `shadow-active` — o ativo se distingue a ≥3.2:1. Pressionado: scale .97.
- Sempre bilíngue: PT em destaque (`button-label`), EN em `micro`, ambos em `ink-muted` (nunca por opacidade).

```html
<div class="sf" style="padding:28px">
<div class="element-selector" role="group" aria-label="Selecionar um dos quatro elementos">
<button type="button" class="mode-button" aria-pressed="true"><span>01</span><b>AR</b><small>AIR</small></button>
<button type="button" class="mode-button" aria-pressed="false"><span>02</span><b>FOGO</b><small>FIRE</small></button>
<button type="button" class="mode-button" aria-pressed="false"><span>03</span><b>ÁGUA</b><small>WATER</small></button>
<button type="button" class="mode-button" aria-pressed="false"><span>04</span><b>TERRA</b><small>EARTH</small></button>
</div></div>
```

## ModeSwitch

Navegação global em pílulas que troca a atmosfera (Ar, Fogo, Água, Terra) de todas as seções ao mesmo tempo.

- Fica sticky no topo, com fundo `surface` clareado, `blur-glass` e `shadow-nav`.
- Ordem e numeração fixas: 01 AR, 02 FOGO, 03 ÁGUA, 04 TERRA. Nunca reordene.
- Estado ativo via `aria-pressed="true"`: fundo `surface2`, borda `accent-strong` (≥3.2:1) e halo de 2px.
- Trocar o modo = trocar `data-theme` (`air`, `fire`, `water`, `earth`) no elemento raiz; todos os tokens mudam juntos, com transição de .7s no fundo.
- Abaixo de 1050px os rótulos laterais ("ATMOSFERA", "01 / AR — LIVE") somem e só o grupo fica.

```html
<div class="sf" style="padding:28px">
<div class="global-mode-list" role="group" aria-label="Mudar elemento da página">
<button type="button" aria-pressed="true">01 <b>AR</b></button>
<button type="button" aria-pressed="false">02 <b>FOGO</b></button>
<button type="button" aria-pressed="false">03 <b>ÁGUA</b></button>
<button type="button" aria-pressed="false">04 <b>TERRA</b></button>
</div></div>
```

## Orbit

Órbita: o motivo central V4.2 — anéis vítreos brilhantes em rotação, com ou sem globo, conforme o elemento.

- **Ar** e **Fogo**: sem globo; só anéis orbitais brilhantes (mesmo material da Água). Ar com bolhas da direita para a esquerda; Fogo de baixo para cima com deriva leve à esquerda.
- **Água**: globo translúcido + órbitas refrativas; bolhas suspensas e orbitais.
- **Terra**: apenas um globo; anéis que surgem e desaparecem por opacidade (`.fade`); sem enxame de bolhas.
- Sem plantas: nenhum caule, folha ou broto em cena (V4.2).
- Anel: borda branca 3px (o segundo 1px) + halo `accent`. Rotação 13s / 21s reversa. Pausa com `prefers-reduced-motion`.
- Na página real, a cena é desenhada em Canvas pelo motor generativo; esta prévia é a versão CSS do componente.

```html
<div class="sf stage" style="display:grid;grid-template-columns:1fr 1fr;gap:12px">
<div><div class="orbit"><div class="orbit-ring"></div><div class="orbit-ring two"></div></div><p class="sf-mono" style="font-size:9px;letter-spacing:.16em;margin:0">AR / FOGO — ANÉIS SEM GLOBO</p></div>
<div><div class="orbit"><div class="orbit-globe"></div><div class="orbit-ring fade"></div><div class="orbit-ring two fade" style="animation-delay:0s,-2.5s"></div></div><p class="sf-mono" style="font-size:9px;letter-spacing:.16em;margin:0">ÁGUA / TERRA — GLOBO + ÓRBITAS</p></div>
</div>
```

## RangeControl

Slider dos parâmetros do motor generativo: rótulo "DOMÍNIO / PARÂMETRO" em mono e valor percentual tabular à direita.

- Trilho de 3px em gradiente `accent-strong` → `accent` → `diffuse`; thumb branco de 16px com borda `accent-strong` (≥3.2:1) e halo de 4px.
- Os quatro parâmetros e seus padrões vêm da família `generator`: GLASS / REFRACTION .72, LIGHT / BLOOM .68, LIFE / DENSITY .54, MOTION / PULSE .40.
- Sempre um `<label for>` e um `<output for>` ligados ao input.

```html
<div class="sf" style="padding:28px;max-width:420px">
<div class="range-control"><div class="range-heading"><label for="g">GLASS / REFRACTION</label><output for="g">72%</output></div><input id="g" type="range" min="0" max="100" value="72"></div>
<div class="range-control"><div class="range-heading"><label for="b">LIGHT / BLOOM</label><output for="b">68%</output></div><input id="b" type="range" min="0" max="100" value="68"></div>
<div class="range-control"><div class="range-heading"><label for="d">LIFE / DENSITY</label><output for="d">54%</output></div><input id="d" type="range" min="0" max="100" value="54"></div>
<div class="range-control" style="margin:0"><div class="range-heading"><label for="m">MOTION / PULSE</label><output for="m">40%</output></div><input id="m" type="range" min="0" max="100" value="40"></div>
</div>
<script>document.querySelectorAll('input[type=range]').forEach(function(r){r.addEventListener('input',function(){r.parentElement.querySelector('output').textContent=r.value+'%'})})</script>
```

## RulePair

Par de regras que explica a lógica do sistema em cada seção: à esquerda o que é fixo, à direita o que o elemento transforma.

- Esquerda `rule-fixed`: borda `line-soft`, branco 59%, rótulo em `ink-muted`.
- Direita `rule-changing`: borda `accent-strong`, gradiente para `surface2`, rótulo em `ink` peso 600. O texto muda com a atmosfera.
- Rótulos sempre "BASE FIXA / <DOMÍNIO>" e "TRANSFORMAÇÃO ELEMENTAL / <DOMÍNIO>"; domínios: COMPOSIÇÃO, FÍSICA, COR & LUZ, MATERIAIS, TIPOGRAFIA, INTERFACE.

```html
<div class="sf" style="padding:20px">
<div class="rule-pair"><div class="rule-fixed"><span>BASE FIXA / COMPOSIÇÃO</span><p>Canvas procedural, serifa translúcida central, linhas de enquadramento, caixa de instruções e espaço negativo.</p></div><div class="rule-changing"><span>TRANSFORMAÇÃO ELEMENTAL / COMPOSIÇÃO</span><p>Órbitas vítreas sem globo e bolhas atravessando a cena da direita para a esquerda.</p></div></div>
</div>
```

## SectionIdentity

Linhas de identidade: o kicker de abertura e a identidade de seção, em mono caixa alta com numeração "NN /".

- **Kicker**: `status-dot` (`accent-strong` com o halo luminoso `shadow-dot`) · texto `kicker` · filete curto `line` · complemento.
- **Section identity**: filete superior `line-soft`; à esquerda "NN / NOME DA SEÇÃO", à direita uma tese em inglês.
- Numeração contínua pela página (00 → 07).

```html
<div class="sf" style="padding:28px;display:grid;gap:28px">
<div class="small-kicker"><span class="status-dot"></span> 04 / LIVING ELEMENTAL ENGINE <span class="kicker-line"></span> NO STATIC ASSETS</div>
<div class="section-identity"><span>02 / ELEMENTAL GRAMMAR</span><span>ONE LANGUAGE / FOUR PHYSICS</span></div>
</div>
```

## Swatch

Amostra de cor clicável dos seis tokens semânticos exportáveis da atmosfera ativa: SURFACE, SOFT FIELD, DIFFUSE, ACCENT, HIGHLIGHT, SPECTRUM.

- Bloco de cor de 112px (75px no mobile) + rodapé mono com nome e hex.
- Clique copia o hex e escreve "COLOR COPIED / #HEX" no `TerminalStatus`.
- Grade de 6 colunas (3 abaixo de 920px).

```html
<div class="sf" style="padding:20px">
<div class="palette">
<div class="swatch"><span class="swatch-color" style="background:var(--surface)"></span><span class="swatch-bottom"><strong>SURFACE</strong></span></div>
<div class="swatch"><span class="swatch-color" style="background:var(--surface2)"></span><span class="swatch-bottom"><strong>SOFT FIELD</strong></span></div>
<div class="swatch"><span class="swatch-color" style="background:var(--diffuse)"></span><span class="swatch-bottom"><strong>DIFFUSE</strong></span></div>
<div class="swatch"><span class="swatch-color" style="background:var(--accent)"></span><span class="swatch-bottom"><strong>ACCENT</strong></span></div>
<div class="swatch"><span class="swatch-color" style="background:var(--highlight)"></span><span class="swatch-bottom"><strong>HIGHLIGHT</strong></span></div>
<div class="swatch"><span class="swatch-color" style="background:var(--spectrum)"></span><span class="swatch-bottom"><strong>SPECTRUM</strong></span></div>
</div></div>
```

## TerminalStatus

Linha de status estilo terminal que narra cada ação do sistema, com prefixo "> ".

- Fundo `surface2` a 75%, filete esquerdo de 2px em `accent-strong`, mono 10px.
- Use `role="status"` para leitores de tela.
- Mensagens em caixa alta, "AÇÃO / DETALHE": LIGHT ENGINE INITIALIZED / READY, COLOR COPIED / #HEX, INSTRUCTION / 2 / AIR.

```html
<div class="sf" style="padding:28px;display:grid;gap:10px;max-width:440px">
<div class="terminal-status" role="status">&gt; LIGHT ENGINE INITIALIZED / READY</div>
<div class="terminal-status">&gt; COLOR COPIED / #548BD7</div>
</div>
```

## Wordmark

A marca SUN//FLORA é tipográfica: "sun//flora" em minúsculas, Alegreya Sans 800 com tracking −0.04em, as barras "//" em `accent-strong` peso 500 (passa 3:1 como texto grande) e o ícone spark sobrescrito.

- Use o estilo `wordmark` (25px; 23px no mobile). Não há arquivo de logo: a marca é sempre texto vivo, para herdar o accent da atmosfera ativa.
- Em frases corridas escreva **SUN//FLORA** em caixa alta.
- Acompanha o header: centro em mono `kicker` ("SOLARPUNK Y3K ✦ LIVING DESIGN SYSTEM") e o CTA em pílula (`radius-pill`, borda `line-strong`).
- O consumidor fornece o link e o `aria-label` ("SUN//FLORA — Início").

```html
<div class="sf" style="padding:32px 28px;display:flex;align-items:center;justify-content:space-between;gap:24px;flex-wrap:wrap">
<a class="brand" href="#">sun<span>//</span>flora<i class="icon-glyph" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M12 2.5v6.5M12 15v6.5M2.5 12H9M15 12h6.5M5.2 5.2l4.2 4.2M14.6 14.6l4.2 4.2M18.8 5.2l-4.2 4.2M9.4 14.6l-4.2 4.2"/></svg></i></a>
<span class="sf-mono" style="font-size:10px;letter-spacing:.12em">SOLARPUNK Y3K <span class="icon-glyph" style="color:var(--accent-strong);margin:0 10px"><svg viewBox="0 0 24 24"><path d="M12 2.5v6.5M12 15v6.5M2.5 12H9M15 12h6.5M5.2 5.2l4.2 4.2M14.6 14.6l4.2 4.2M18.8 5.2l-4.2 4.2M9.4 14.6l-4.2 4.2"/></svg></span> LIVING DESIGN SYSTEM</span>
<a class="header-cta" href="#">OPEN LAB <span aria-hidden="true">↗</span></a>
</div>
```

## Estilos dos componentes (bundle.css)

Envolva qualquer superfície em `.sf` e carregue as variáveis acima antes deste CSS.

```css
/* SUN//FLORA V4.2 — component styles, ported 1:1 from index.html.
   Every colour, radius and shadow reads a token from tokens.css.
   Wrap any surface in .sf to get the page ground, ink and sans text. */

.sf{background:var(--surface);color:var(--ink);font-family:var(--font-sans);font-optical-sizing:auto;font-kerning:normal;font-variant-numeric:lining-nums;-webkit-font-smoothing:antialiased}
.sf *{box-sizing:border-box}
.sf button,.sf input{font:inherit}
.sf button{cursor:pointer}
.sf button:focus-visible,.sf a:focus-visible,.sf input:focus-visible{outline:2px solid var(--ink);outline-offset:3px}
.sf-mono{font-family:var(--font-mono);letter-spacing:.04em}
.sf-display{font-family:var(--font-display);font-weight:400;letter-spacing:-.035em;font-optical-sizing:auto}

/* Icon */
.icon-glyph{display:inline-flex;align-items:center;justify-content:center;width:1.15em;height:1.15em;line-height:0;vertical-align:middle;flex:0 0 auto}
.icon-glyph svg{width:100%;height:100%;stroke:currentColor;fill:none;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}

/* Wordmark */
.brand{font-family:var(--font-sans);font-size:25px;letter-spacing:-.04em;font-weight:800;white-space:nowrap;color:var(--ink);text-decoration:none}
.brand span{color:var(--accent-strong);font-weight:500}
.brand i{font-size:14px;vertical-align:top;margin-left:3px;font-style:normal;color:var(--accent-strong)}

/* Status dot */
.status-dot{display:inline-block;width:7px;height:7px;background:var(--accent-strong);border-radius:50%;box-shadow:var(--shadow-dot);flex-shrink:0}

/* Section identity + kicker */
.section-identity{display:flex;justify-content:space-between;gap:12px;align-items:center;padding-top:14px;border-top:1px solid var(--line-soft);font-family:var(--font-mono);font-size:10px;letter-spacing:.08em}
.small-kicker{display:flex;align-items:center;gap:14px;font-family:var(--font-mono);font-size:10px;letter-spacing:.14em}
.kicker-line{flex:1;border-top:1px solid var(--line);max-width:90px}

/* Global mode switch (pill segmented control) */
.global-mode-list{display:grid;grid-template-columns:repeat(4,1fr);gap:6px}
.global-mode-list button{min-height:42px;padding:10px 6px;display:flex;gap:8px;align-items:center;justify-content:center;background:var(--glass-tile);color:var(--ink);border:1px solid var(--line-soft);border-radius:var(--radius-pill);font:500 10px var(--font-mono);letter-spacing:.06em;transition:background .3s,border-color .3s,box-shadow .3s}
.global-mode-list button b{font-weight:600}
.global-mode-list button[aria-pressed=true]{border-color:var(--accent-strong);background:var(--surface2);box-shadow:0 0 0 2px color-mix(in srgb,var(--accent),transparent 85%),inset 0 1px 0 #fff}

/* Mode button (element selector tile) */
.element-selector{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:var(--space-5)}
.mode-button{border:1px solid var(--line);border-radius:var(--radius-5);background:var(--glass-tile);color:var(--ink);display:flex;flex-direction:column;min-width:0;text-align:left;padding:13px 10px;transition:background .32s,transform .25s,border .25s}
.mode-button span{font:9px var(--font-mono);letter-spacing:.04em;color:var(--ink-muted)}
.mode-button b{font-weight:500;font-size:16px;margin-top:21px;line-height:1.1}
.mode-button small{font:9px var(--font-mono);letter-spacing:.04em;color:var(--ink-muted);margin-top:8px}
.mode-button.active,.mode-button[aria-pressed=true]{background:var(--surface2);border-color:var(--accent-strong);box-shadow:var(--shadow-active)}
.mode-button:active{transform:scale(.97)}

/* Buttons */
.control-actions{display:flex;gap:var(--space-7)}
.control-actions button{min-height:48px;border-radius:var(--radius-5);border:1px solid var(--ink);font:500 11px var(--font-mono);letter-spacing:.04em;white-space:nowrap}
.action-main{flex:1;background:var(--ink);color:var(--white);display:flex;align-items:center;justify-content:space-between;padding:0 16px;gap:12px}
.action-ghost{background:transparent;color:var(--ink);padding:0 13px}
.secondary-actions button{flex:1;border-color:var(--line-strong);background:var(--glass-tile);color:var(--ink)}
.code-buttons{display:flex;gap:10px}
.code-buttons button{min-height:45px;padding:0 16px;color:var(--ink);background:transparent;border:1px solid var(--line-strong);border-radius:var(--radius-4);display:flex;align-items:center;gap:20px;font:500 11px var(--font-mono);letter-spacing:.04em}
.code-buttons button:first-child{background:var(--ink);color:var(--white)}
.header-cta{display:inline-block;font:10px var(--font-mono);letter-spacing:.12em;border:1px solid var(--line-strong);padding:12px 16px;border-radius:var(--radius-pill);color:var(--ink);text-decoration:none}
.header-cta span{margin-left:15px}

/* Range control */
.range-control{margin-bottom:23px}
.range-heading{display:flex;justify-content:space-between;align-items:center;font:10px var(--font-mono);letter-spacing:.05em;margin-bottom:12px}
.range-heading output{font-weight:600;font-variant-numeric:tabular-nums}
.sf input[type=range]{width:100%;height:3px;margin:0;cursor:pointer;-webkit-appearance:none;appearance:none;background:linear-gradient(90deg,var(--accent-strong),var(--accent) 45%,var(--diffuse));border-radius:10px}
.sf input[type=range]::-webkit-slider-thumb{appearance:none;-webkit-appearance:none;width:16px;height:16px;border-radius:50%;background:var(--white);border:2px solid var(--accent-strong);box-shadow:0 0 0 4px color-mix(in srgb,var(--accent),transparent 84%)}
.sf input[type=range]::-moz-range-thumb{width:12px;height:12px;border-radius:50%;background:var(--white);border:2px solid var(--accent-strong)}

/* Glass instruction card */
.component-card{background:var(--glass-fill);border:1px solid var(--glass-edge);box-shadow:var(--shadow-glass-card);padding:var(--space-24);border-radius:var(--radius-glass);backdrop-filter:blur(var(--blur-glass)) saturate(1.7);-webkit-backdrop-filter:blur(var(--blur-glass)) saturate(1.7);position:relative;color:var(--ink);font:10px/1.65 var(--font-mono);letter-spacing:.04em}
.component-card-head{display:flex;gap:10px;align-items:center;border-bottom:1px solid var(--line);padding-bottom:12px}
.component-card-head strong{font-weight:600}
.component-card-head>span:last-child{margin-left:auto}
.component-card p{margin:28px 0;font-family:var(--font-sans);font-size:15px;line-height:1.6;letter-spacing:0}
.component-command{display:flex;align-items:center;gap:12px;border-top:1px solid var(--line);padding-top:16px;min-height:48px;font-size:11px}
.component-command>span:last-child{margin-left:auto}
.component-step{border:1px solid var(--accent-strong);border-radius:30px;min-width:28px;text-align:center}
.step-progress{display:flex;gap:8px;margin-top:23px}
.step-progress button{width:37px;height:31px;background:var(--glass-tile);color:var(--ink);border:1px solid var(--line);border-radius:var(--radius-glass);font:10px var(--font-mono)}
.step-progress button[aria-pressed=true]{background:var(--ink);border-color:var(--ink);color:var(--white)}
.stage{padding:32px;border-radius:var(--radius-8);border:1px solid var(--glass-edge);background:radial-gradient(ellipse at 25% 36%,var(--ambient-a),transparent 48%),radial-gradient(ellipse at 75% 70%,var(--ambient-b),transparent 53%),linear-gradient(145deg,rgba(255,255,255,.76),var(--surface2))}

/* Rule pair: fixed base vs elemental transformation */
.rule-pair{display:grid;grid-template-columns:1fr 1fr;gap:var(--space-12)}
.rule-pair>div{min-height:112px;padding:20px 22px;border:1px solid var(--line-soft);background:rgba(255,255,255,.59);border-radius:var(--radius-5)}
.rule-pair .rule-changing{border-color:var(--accent-strong);background:linear-gradient(120deg,rgba(255,255,255,.69),color-mix(in srgb,var(--surface2),transparent 32%))}
.rule-pair span{display:block;font:10px/1.65 var(--font-mono);letter-spacing:.04em;color:var(--ink-muted);margin-bottom:10px}
.rule-pair .rule-changing span{color:var(--ink);font-weight:600}
.rule-pair p{margin:0;font-size:14px;line-height:1.6}

/* Foundation tile */
.foundation-grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:10px}
.foundation-grid>div{padding:23px;min-height:184px;display:flex;flex-direction:column;gap:12px;border:1px solid var(--line-soft);background:linear-gradient(140deg,rgba(255,255,255,.75),rgba(255,255,255,.2));border-radius:var(--radius-6)}
.foundation-grid span{font:10px/1.65 var(--font-mono);letter-spacing:.04em;color:var(--ink-muted)}
.foundation-grid b{font-family:var(--font-display);font-size:31px;font-weight:400;letter-spacing:-.02em;line-height:1.05}
.foundation-grid p{font-size:13px;line-height:1.6;margin:0}

/* Swatch */
.palette{display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:8px}
.swatch{border:1px solid var(--line);background:rgba(255,255,255,.58);border-radius:var(--radius-5);display:flex;flex-direction:column;overflow:hidden;min-width:0;padding:0;color:var(--ink);text-align:left}
.swatch-color{height:112px;display:block}
.swatch-bottom{padding:12px;display:flex;justify-content:space-between;flex-wrap:wrap;gap:8px;font:10px var(--font-mono)}
.swatch-bottom strong{font-weight:600}

/* Light panels (the three gradient families) */
.light-panels{display:grid;grid-template-columns:repeat(3,1fr);gap:var(--space-12)}
.light-panel{position:relative;border:1px solid var(--glass-edge);border-radius:var(--radius-6);min-height:200px;padding:20px;overflow:hidden;display:flex;flex-direction:column;align-items:start;justify-content:space-between}
.gradient-atmosphere{background:linear-gradient(136deg,#fff,var(--surface2) 53%,var(--diffuse))}
.gradient-sun{background:radial-gradient(circle at 56% 50%,var(--highlight),transparent 32%),radial-gradient(circle at 76% 24%,var(--ambient-b),transparent 68%),var(--surface2)}
.gradient-prism{background:conic-gradient(from 40deg at 55% 50%,var(--surface2),var(--ambient-a),var(--highlight),var(--spectrum),var(--surface2),var(--ambient-b),var(--surface2))}
.light-panel:after{content:'';position:absolute;width:75%;height:80%;border:1px solid rgba(255,255,255,.75);border-radius:47% 53% 37% 63%;top:27%;left:39%;transform:rotate(-23deg);box-shadow:0 0 20px rgba(255,255,255,.7),inset 0 0 23px rgba(255,255,255,.7);pointer-events:none}
.light-panel>div,.light-panel>span{font:500 9px var(--font-mono);letter-spacing:.04em;position:relative;z-index:1}
.light-panel b{font-family:var(--font-display);font-weight:400;font-size:43px;letter-spacing:-.03em;position:relative;z-index:1}

/* Materials */
.material-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:var(--space-12)}
.material-tile{border:1px solid var(--line-soft);border-radius:var(--radius-6);padding:12px;background:rgba(255,255,255,.46)}
.material-demo{height:200px;display:grid;place-items:center;overflow:hidden;border-radius:var(--radius-4);position:relative}
.clear-demo{background:radial-gradient(circle at 37% 27%,var(--ambient-b),transparent 43%),linear-gradient(120deg,var(--surface2),var(--diffuse))}
.gel-demo{background:radial-gradient(circle at 75% 27%,var(--ambient-b),transparent 45%),var(--surface2)}
.sphere-demo{background:radial-gradient(circle at 15% 80%,var(--ambient-a),transparent 50%),var(--surface2)}
.material-glass{width:53%;aspect-ratio:1;border:1px solid rgba(255,255,255,.94);background:linear-gradient(146deg,rgba(255,255,255,.5),rgba(255,255,255,.08) 43%,rgba(255,255,255,.46));backdrop-filter:blur(var(--blur-material));border-radius:35%;box-shadow:inset 0 1px 12px rgba(255,255,255,.75),inset -6px -8px 25px rgba(117,168,229,.17),0 18px 30px rgba(66,110,160,.1);display:grid;place-items:center;font-size:56px;color:rgba(255,255,255,.8);transform:rotate(-18deg)}
.material-gel{width:52%;aspect-ratio:1;border-radius:51% 49% 62% 38% / 42% 54% 46% 58%;background:radial-gradient(circle at 27% 23%,#fff 2%,transparent 24%),radial-gradient(circle at 70% 77%,var(--ambient-b),transparent 32%),radial-gradient(circle at 43% 48%,rgba(255,255,255,.04),var(--spectrum));border:2px solid rgba(255,255,255,.85);box-shadow:inset 10px 10px 20px rgba(255,255,255,.76),inset -18px -19px 25px color-mix(in srgb,var(--accent),transparent 47%),0 21px 31px color-mix(in srgb,var(--accent),transparent 78%);transform:rotate(-25deg);animation:sfGelFloat 8s ease-in-out infinite alternate}
.material-sphere{width:55%;aspect-ratio:1;border-radius:50%;background:radial-gradient(circle at 29% 22%,#fff 0%,rgba(255,255,255,.7) 8%,transparent 32%),radial-gradient(circle at 73% 82%,var(--ink),transparent 35%),radial-gradient(circle at 23% 65%,var(--ambient-b),transparent 40%),linear-gradient(135deg,rgba(255,255,255,.95),var(--spectrum),rgba(255,255,255,.46),var(--accent));box-shadow:inset -12px -13px 23px color-mix(in srgb,var(--ink),transparent 66%),inset 12px 17px 23px rgba(255,255,255,.9),0 20px 27px color-mix(in srgb,var(--ink),transparent 80%);border:1px solid rgba(255,255,255,.98);animation:sfGelFloat 6s ease-in-out infinite alternate-reverse}
.material-tile>div:last-child{padding:16px 4px 4px;display:flex;justify-content:space-between;align-items:center;gap:10px;flex-wrap:wrap}
.material-tile strong{font-size:16px;font-weight:500}
.material-tile>div:last-child span{font:9px/1.3 var(--font-mono);letter-spacing:.04em;color:var(--ink-muted)}
@keyframes sfGelFloat{0%{transform:translateY(8px) rotate(-15deg)}100%{transform:translateY(-9px) rotate(14deg)}}

/* Orbit (component-shine) — Air/Fire: rings only; Water: globe + refractive rings; Earth: globe + fading rings */
.orbit{position:relative;min-height:240px;display:grid;place-items:center}
.orbit-globe{width:min(53%,200px);aspect-ratio:1;border-radius:50%;background:radial-gradient(circle at 31% 23%,#fff 0 4%,transparent 31%),radial-gradient(circle at 68% 72%,var(--ambient-b),transparent 44%),radial-gradient(circle at 44% 54%,rgba(255,255,255,.08) 0%,var(--spectrum) 80%,var(--accent));border:2px solid rgba(255,255,255,.85);box-shadow:inset 14px 12px 35px rgba(255,255,255,.84),inset -14px -11px 32px color-mix(in srgb,var(--accent),transparent 60%),0 0 70px color-mix(in srgb,var(--accent),transparent 68%);animation:sfLivingOrb 8s ease-in-out infinite alternate}
.orbit-ring{position:absolute;width:76%;height:32%;border:3px solid rgba(255,255,255,.85);border-radius:50%;box-shadow:0 0 13px color-mix(in srgb,var(--accent),transparent 57%),inset 0 0 14px rgba(255,255,255,.9);transform:rotate(-26deg);animation:sfOrbit 13s linear infinite}
.orbit-ring.two{width:59%;height:36%;transform:rotate(55deg);border-width:1px;animation-duration:21s;animation-direction:reverse}
.orbit-ring.fade{animation:sfOrbit 13s linear infinite,sfFade 5s ease-in-out infinite alternate}
@keyframes sfLivingOrb{from{transform:translateY(-6px) scale(.96)}to{transform:translateY(9px) scale(1.04)}}
@keyframes sfOrbit{from{transform:rotate(-26deg)}to{transform:rotate(334deg)}}
@keyframes sfFade{from{opacity:.05}to{opacity:1}}

/* Terminal status + live label */
.terminal-status{padding:12px;background:color-mix(in srgb,var(--surface2),transparent 25%);border-left:2px solid var(--accent-strong);font:10px/1.4 var(--font-mono);letter-spacing:.04em;min-height:41px}
.code-preview{margin:0;overflow:auto;border:1px solid var(--line-soft);border-radius:var(--radius-7);background:rgba(255,255,255,.65);padding:24px;font:12px/1.95 var(--font-mono);color:var(--ink)}

/* Glass type */
.type-display{font-family:var(--font-display);font-size:96px;font-weight:400;letter-spacing:-.04em;line-height:1.1;color:rgba(255,255,255,.28);-webkit-text-stroke:1px var(--accent-strong);text-shadow:2px 4px 0 rgba(255,255,255,.75),2px 10px 18px rgba(102,151,201,.17);margin:0;white-space:nowrap}

@media (prefers-reduced-motion:reduce){.material-gel,.material-sphere,.orbit-globe,.orbit-ring{animation:none}}
```


# Ícones (SVG inline, herdam currentColor)

**spark**
```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2.5v6.5M12 15v6.5M2.5 12H9M15 12h6.5M5.2 5.2l4.2 4.2M14.6 14.6l4.2 4.2M18.8 5.2l-4.2 4.2M9.4 14.6l-4.2 4.2"/></svg>
```

**air**
```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5.2"/><circle cx="12" cy="12" r="8.6" opacity=".72"/><circle cx="12" cy="12" r="11" opacity=".42"/></svg>
```

**fire**
```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3.2c1.8 3.1.8 4.5 3 6.8 1.2 1.2 2.1 2.8 2.1 4.7 0 3-2.3 5.3-5.1 5.3S6.9 17.7 6.9 14.8c0-2.5 1.6-4.2 3.1-5.9 1.4-1.5 1.9-2.7 2-5.7z"/><path d="M12.4 10.3c.9 1.1 1.6 2 1.6 3.5 0 1.4-1 2.7-2.3 2.7s-2.2-1.1-2.2-2.4c0-1 .4-1.7 1.2-2.7.7-.8 1.1-1.4 1.7-3.1z" opacity=".65"/></svg>
```

**water**
```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9c2.2 1.5 4.4 1.5 6.6 0s4.4-1.5 6.6 0 4.4 1.5 4.8 0"/><path d="M3 14c2.2 1.5 4.4 1.5 6.6 0s4.4-1.5 6.6 0 4.4 1.5 4.8 0"/><path d="M3 19c2.2 1.5 4.4 1.5 6.6 0s4.4-1.5 6.6 0 4.4 1.5 4.8 0"/></svg>
```

**earth**
```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20v-7"/><path d="M12 13c0-3.6-2.4-5.7-6.4-5.7 0 3.6 2.7 5.7 6.4 5.7z"/><path d="M12 11.8c0-3.2 2.1-5.1 5.7-5.1 0 3.3-2.4 5.1-5.7 5.1z"/></svg>
```


---
SUN//FLORA · Maia Oazem / gira. · CC BY-NC-SA 4.0 · Fontes: Bodoni Moda (indestructible type*), Alegreya Sans (Juan Pablo del Peral, Huerta Tipográfica), IBM Plex Mono (Mike Abbink, Bold Monday) — SIL OFL 1.1.
