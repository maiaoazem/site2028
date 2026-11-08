# EF | Ética Futurante — design system

> Design system gerado por IA · Maia Oazem / laborateliê · gira. · v2.0 · CC BY-NC-SA 4.0 · fontes SIL OFL 1.1
> Para levar para a sua IA: anexe este arquivo e peça a página ou a peça que quiser. A IA deve usar só os tokens, as fontes e a estrutura abaixo.

**Sistema híbrido · v2.0 · base MAISON 04 × estrutura Maia Oazem**

O sistema da Ética Futurante do laborateliê da gira. (gira.guru/futurante). Da base MAISON 04 vêm a tipografia (Bodoni Moda, Newsreader, DM Sans), a grade, os fios de 1px, a paleta Bone e a regra de nada de sombra, gradiente ou canto redondo. Do sistema Maia Oazem vêm a lógica de demarcação: fios de ponta a ponta, a linha de assinatura do site, números grandes de seção, cor como bloco inteiro e um grande vazio por tela.

Palavras: composto · tátil · literário · arquitetônico · em movimento lento.

## 00 — Estrutura padrão da página

Toda página EF segue esta ordem por padrão. Cada parte é um componente com prévia (grupo "Página EF").

| # | Parte | Componente | Cor | O que faz |
| --- | --- | --- | --- | --- |
| 1 | Topo do site | `SiteTop` | `blue` | Fio · assinatura (M, fagulha, "Maia Oazem · laborateliê") e menu · fio · seções da página · fio. Igual à home de gira.guru, em Instrument Sans. |
| 2 | Destaque animado | `OrbitHero` | `blue` | As cartas giram em volta do título (`ef-hero`), com o subtítulo separado e menor. Gira sempre; arrastar gira. Único lugar da home com as imagens das cartas. Fecha com fio e a linha "Hope Culture · *o laborateliê da gira. é um hope lab*". |
| 3 | Abertura | `Intro07` | `paper` | Uma frase em `ef-lead` sobre o número gigante ("07") atrás de tudo. |
| 4 | Parte 1 · princípios | `StackCards` | `blue` / `red` / `white` | Título "Os 07 Princípios *de Futuração*" (`ef-big`) e as cartas que sobem com a rolagem e se empilham. Princípio em destaque, nome secundário, frase curta, carta flutuando. |
| 5 | Carta inteira | `CardDialog` | `paper` + `blue` | Janela com conceito, descrição, compromisso e a pergunta futurante num bloco azul. |
| 6 | Parte 2 · suporte | `Folders` | `red` / `blue` / `white` | Os blocos de informação como pastas empilhadas com abas escalonadas; fechadas mostram só a faixa, abertas o conteúdo em `paper`. |
| 7 | Fechamento | `DrawBlock` | `red` | "Tire uma *carta*": abre uma carta inteira ao acaso. |
| 8 | Rodapé | `FooterEF` | `blue` | Versão e créditos das imagens. |

A peça impressa e a carta das prévias é a `Carta` (70 × 120 mm).

### Regras do híbrido

1. **Cor é bloco inteiro.** O azul (`blue`, Space Indigo) e o vermelho (`red`, Cherry Rose) entram de ponta a ponta, alternados; o texto sobre eles é `on-color` (o próprio Bone). Olive e periwinkle ficam só em marcas pequenas.
2. **Um bloco de cor por vez na tela**, separado do próximo por `paper` ou `white`. Nas cartas e nas pastas, a alternância azul · vermelho · branco faz o ritmo.
3. **Fios de ponta a ponta** organizam o topo, os cabeços e as pastas; nada flutua sem um fio que o ancore (Maia Oazem).
4. **Escala com contraste:** uma coisa enorme por bloco (título, número, princípio) e o resto pequeno.
5. **Um vazio grande por tela**, como o 07 da abertura.
6. **Menos texto na página, mais na carta.** A página mostra só o princípio, o nome e a frase curta; o texto completo fica na janela da carta e nas pastas.
7. **Movimento leve e contínuo:** o anel gira (`orbit-turn`), as cartas flutuam (`card-float`) e entram com profundidade (`card-deal`); as pastas levantam no hover. Tudo respeita `prefers-reduced-motion`.
8. **Imagens das cartas** só no destaque animado, nas páginas internas e na impressão.
9. **Bodoni para títulos curtos, Newsreader para frases.** A Bodoni Moda é para títulos de até 4 palavras, nomes e números. Qualquer frase com 5 palavras ou mais (abertura, citação, pergunta, aviso, título longo) vai em Newsreader no corte de display (`statement`: peso 300, opsz 72, tracking −0.02em, entrelinha 1.04–1.12). O itálico continua marcando a palavra-chave.
10. **Pastas sem fresta.** A faixa de cada pasta fechada continua por baixo da pasta seguinte (`::after` da mesma cor), para que, ao subir no hover, nunca apareça o fundo atrás dela.

### Implementação

- `components/bundle.css` traz, depois da base MAISON 04 (classes `m-`), todo o CSS da estrutura EF, com aliases curtos (`--display`, `--s5`, `--outer`…) apontando para os tokens.
- Fontes do Google Fonts: Bodoni Moda, Newsreader, DM Sans e Instrument Sans (só no topo).
- O M de Maia Oazem é buscado da home de gira.guru (`fetch('/')`, símbolo `#m`); a fagulha vem inline.

---

*A base abaixo é o sistema MAISON 04 original, em inglês, e continua valendo para tudo o que a estrutura EF não redefine.*

## 01 — Creative principles

| Principle | Direction | Application |
| --- | --- | --- |
| Precision | Every line is placed with intent. | Exact grids, measured whitespace, aligned folios and rules. |
| Restraint | Luxury is expressed by absence. | Limit elements, flourishes and colors in each view. |
| Contrast | Emphasize hierarchy, not noise. | Monumental serif headlines against tiny utilitarian annotations; large blank fields against small framed objects. |
| Versatility | One grammar, four expressions. | Identical rules, typography and grids across all four atmospheres. |

**Default balance:** about 80% `paper` (Bone) / `white`, 15% `ink` typography and hairlines, 5% atmospheric color. A full-bleed color page is a deliberate exception, never the default.

## 02 — The four moments

Provisional experience labels; replace them when the hotel's experience architecture is defined. These are four chapters of one brand, not four brands.

| Moment | Name | Color | Token | HEX | Text on it | Sensory role |
| --- | --- | --- | --- | --- | --- | --- |
| 01 | Arrival | Space Indigo | `moment-indigo` | #1B264F | white | Orientation, anticipation, depth, threshold. |
| 02 | Stillness | Dusty Olive | `moment-olive` | #646F4B | white | Sanctuary, cultivation, rest, connection to place. |
| 03 | Discovery | Soft Periwinkle | `moment-periwinkle` | #9B7EDE | **ink** | Curiosity, culture, the unexpected. |
| 04 | Afterglow | Cherry Rose | `moment-rose` | #A4243B | white | Hospitality, gathering, ritual, evening. |

The `moment` token holds the active chapter color (Arrival by default) and `on-moment` the text color that goes with it. Set `data-moment="02"`, `"03"` or `"04"` on a section to switch both. Discovery is the one light moment: Soft Periwinkle carries ink text, never white.

### Neutral foundation

| Token | HEX | Purpose |
| --- | --- | --- |
| `paper` | #ECE2D0 | Bone. Default editorial field, digital canvas. |
| `white` | #FFFFFF | Pure contrast, reversed text, open masthead field. |
| `ink` | #191919 | Typography, critical lines, primary framing. |
| `muted` | #5F5B52 | Annotations and metadata (warmed for bone). |
| `hairline` | #B9AD96 | Fine dividers on paper. |
| `soft` | #E2D6C0 | Rare background panels, quiet grouping. |

### Color rules

1. One atmospheric color per spread, section or screen. Never pair two saturated moment colors in one composition.
2. `ink` on `paper` for long reading. `on-moment` (white, or ink on periwinkle) on a moment color for short, oversized statements.
3. The identity must remain complete in black and white, with no atmospheric color.
4. No gradients, chroma shifts, bevels, glossy overlays or decorative shadows.
5. Color is a chapter marker, not illustration.

Contrast: `ink` on `paper` 13.7:1; `muted` on `paper` 5.3:1, on `soft` 4.7:1. White on indigo 14.6:1, on rose 7.3:1, on olive 5.4:1. On periwinkle white is only 3.3:1, so text there is `ink` (5.4:1). Periwinkle and olive are too light to be text on bone (2.5:1 and 4.2:1); rose works as a short accent (5.7:1). `hairline` is decorative only (1.7:1).

Palette exchange: `a4243b, 1b264f, 9b7ede, ece2d0, 646f4b` — Cherry Rose, Space Indigo, Soft Periwinkle, Bone, Dusty Olive.

## 03 — Typography

Open-licensed families from Google Fonts (hosted; verify each license file before packaging binaries in a distributed app).

| Role | Family | Treatment |
| --- | --- | --- |
| Display / logotype direction | Bodoni Moda (`--font-display`) | 400–500, tracking −0.045em to −0.025em; large, sculptural. |
| Long-form editorial | Newsreader (`--font-reading`) | 400, normal tracking, 1.35–1.48 line-height, 17–21px. |
| Statement (sentences of 5+ words at display size) | Newsreader display cut (`--font-statement`) | 300, opsz 72, tracking −0.02em, line-height 1.04–1.12. Bodoni stays for titles up to 4 words, names and numerals. |
| Navigation, numbers, captions | DM Sans (`--font-utility`) | 400–600; uppercase sparingly, tracked +0.11em to +0.20em for metadata. |

Desktop hierarchy (the type styles carry the maximum; use the fluid value in production):

- `display-xl` — clamp(5.25rem, 10vw, 11.5rem) / 0.83–0.94
- `display-l` — clamp(3.6rem, 7vw, 7.5rem) / 0.94
- `section-heading` — clamp(2.8rem, 5vw, 5.5rem) / 1.0
- `editorial-body` — 19px / 1.42, 52–65 characters per line
- `ui-body` — 14px / 1.45
- `annotation` — 10–11px / 1.35, uppercase, +0.12em

Mix very large, fine serif forms with compact, rigorously aligned sans labels. No more than two expressive sizes in one compact panel. Never center-align reading paragraphs. Italic is a literary emphasis, not a heading style.

## 04 — Layout and whitespace

- **Desktop:** 12 columns; outer margin clamp(`outer-min`, 4.5vw, `outer-max`); `gutter` 20–28px.
- **Mobile:** 4 columns; 20px outer margins; 12–16px gutters.
- **Print:** A4 and A5; minimum 12–18mm safe margin depending on trim.
- **Measure:** `measure-min`–`measure-max` (52–65ch); never edge to edge.
- **Common splits:** 50/50 architectural diptych · 8/4 feature/sidebar · 4/8 numbered index/essay.
- Large compositions protect at least 30–45% open field (`open-field`). Blank space is an active element.

**Spacing scale:** 4 / 8 / 12 / 18 / 28 / 44 / 72 / 112 / 176px (`space-1` … `space-9`). Prefer fewer, larger vertical intervals: sections breathe as discrete printed plates (`space-8` between sections, `space-9` around chapter openers).

## 05 — Graphic grammar

**Rules and borders**

- Primary: `rule` 1px in `ink` — chapter boundary, table or grid edge.
- Secondary: `rule` 1px in `hairline` — sub-separations.
- `radius-none` everywhere. No drop shadows. Never simulate a raised interface.
- A line may stop just short of a corner to reference archival printing — intentional and consistent only.

**Blocks** — unfilled text fields or one solid field of color, never decorative panels. Color blocks are reserved for chapter-opening statements, stationery reverse and single typographic inserts. Adjacent large color blocks never compete: white is the separating material.

**Arrows** — single-weight strokes, open sharp arrowheads, never filled triangles. Horizontal progression; a four-step clockwise sequence. They mark an action, route, continuation or relationship, never filler. 1px (`rule`) in large editorial, 1.25px (`stroke-control`) in small digital controls.

**Frames and indexes** — the chapter number sits in a 1px outlined tab that slightly intersects the top page rule. Number records `01—04` or `01 / ARRIVAL` with tabular numerals. Tables use horizontal rules and occasional vertical dividers, with open space instead of heavy cells. Botanical engravings and architectural images appear as captioned, framed archival plates.

**Diagram** — a diamond / rectilinear circuit of four connected experiences: four axes, four open arrow strokes, a center field. It is an indexing device, not the logo; do not reproduce any reference mark.

## 06 — Imagery and surfaces

Subjects: architectural thresholds; long corridors and cutouts; honest materials, courtyards, botanical silhouettes; quiet still life; textural close-ups; human presence as observed gesture rather than staged lifestyle.

Treatment: natural light, low saturation, restrained shadows, full tonal range. Edge-to-edge plates held by a fine page border, or one image sharing a spread with a full page of typography.

Print: uncoated bone stock, tactile but not distressed. Natural grain and slight ink imperfection are fine; grunge, fake aged paper, heavy vignettes and filters are not.

Iconography: there is no icon set. Wayfinding and UI use oversized numerals, words and open arrows instead of pictograms.

Logo: none yet. Until a mark exists, set the name in Bodoni Moda (`display-l` or smaller) and never draw a substitute mark.

## 07 — Components

| Component | Anatomy | Rules |
| --- | --- | --- |
| Masthead | logotype + index + chapter | Open white field, bottom 1px rule. |
| Chapter opener | small folio + giant serif title + short descriptor | One moment color only; at least half the space reserved around the title. |
| Editorial diptych | body essay + image plate | Symmetric outer frame, divergent inner content. |
| Directory | number + item name + optional translation | 1px horizontal rules, slim vertical dividers, no filled rows. |
| Moment tile | 01 + title + short phrase + narrow arrow | Flat moment color; `on-moment` display text; no gradients. |
| Caption | plate number + descriptor + year/location | 10–11px sans, aligned to the image edge. |
| Quiet CTA | verb + arrow + rule | No pill buttons; underline and progression replace the box. |
| Stationery reverse | compact centered wordmark | Single dark stock with white mark; nothing else. |

EF components (group "Página EF") — see section 00: `SiteTop`, `OrbitHero`, `Intro07`, `StackCards`, `Carta`, `CardDialog`, `Folders`, `DrawBlock`, `FooterEF`.

Previews are plain HTML and CSS built on `tokens.css` and `components/bundle.css` (base classes prefixed `m-`; EF classes unprefixed, as on the page). There is no JavaScript bundle; OrbitHero and StackCards carry their small scripts in the preview.

## 08 — Interaction and motion

- Almost invisible: `duration-quick`–`duration-settle` (180–320ms) ease-out for text, lines, focus and reveals.
- A chapter transition may fade a color field over `duration-chapter` (600–900ms), only if it does not interrupt reading.
- Hover: advance an arrow 4px (`space-1`), invert ink/white for a discrete selection, or reveal a 1px underline.
- No bouncy easing, decorative cursors, parallax or perpetual ornament. Respect `prefers-reduced-motion: reduce`.
- Keyboard focus stays clearly visible (`focus-ring`); interaction never relies on color alone.

## 09 — Applications

- **Keycard sleeve:** paper-white front, tiny serial number and monogram near the edges; moment color on the reverse with one centered name.
- **Welcome booklet:** four-chapter system, 1px architectural margin frame, large Newsreader copy, occasional Bodoni chapter headings, one plate.
- **Restaurant menu:** ink on uncoated paper, rule-separated courses, widely spaced headings, a single `moment-rose` evening marker.
- **Wayfinding:** `moment-indigo` or near-black field, oversized numerals, crisp horizontal arrows, generous breathing room.
- **Website:** quiet masthead, large typographic hero, four-chapter journey, full-color interludes, editorial storytelling.
- **Amenities:** restrained microtypography, left-aligned item names, one printed line, optional full-field colored label.

## 10 — Accessibility and implementation

- Body copy is `ink` on `paper`; `muted` is for optional secondary information only.
- Visible focus indicator and meaningful link names are required.
- Touch controls at least 44×44 CSS px (`space-6`).
- Semantic HTML; CSS custom properties for moment theming.
- Never encode an actionable state with color alone: pair it with a number or label.

## 11 — System guardrails

**Do:** establish calm hierarchy; build from the frame and grid; let a single accent signal context; use typography as image; show material and culture with specificity.

**Don't:** run all four colors as a busy simultaneous palette; overfill pages; introduce rounded SaaS cards, gradients, drop shadows, neon highlights, photomontage, arbitrary arrows or generic hotel stock imagery.

---

## Tokens

| token | valor | uso |
| --- | --- | --- |
| `paper` | `#ece2d0` | Bone. Default editorial field and digital canvas, roughly 80% of every composition. Ink on paper 13.7:1. |
| `white` | `#ffffff` | Pure contrast: reversed text on indigo, olive and rose; the open masthead field and card fronts. |
| `ink` | `#191919` | Typography, primary 1px rules, framing. The only pairing for long reading (13.7:1 on paper). |
| `muted` | `#5f5b52` | Annotations and metadata, warmed to sit on bone: 5.3:1 on paper, 4.7:1 on soft, 6.8:1 on white. Never essential long reading. |
| `hairline` | `#b9ad96` | Secondary 1px dividers on paper. Decorative only (1.7:1): never text, never a control border. |
| `soft` | `#e2d6c0` | A step darker than bone, for rare quiet grouping and image placeholders. No radius, no shadow. |
| `moment-indigo` | `#1b264f` | Space Indigo · Moment 01 · Arrival. Orientation, threshold, wayfinding fields. White text 14.6:1. |
| `moment-olive` | `#646f4b` | Dusty Olive · Moment 02 · Stillness. Sanctuary, cultivation, rest. White text 5.4:1: fine for body size, best for short statements. |
| `moment-periwinkle` | `#9b7ede` | Soft Periwinkle · Moment 03 · Discovery. The one LIGHT moment: text on it is ink (5.4:1), never white (3.3:1 fails). Never periwinkle text on bone (2.5:1). |
| `moment-rose` | `#a4243b` | Cherry Rose · Moment 04 · Afterglow. Hospitality, gathering, evening; the single marker on a menu. White text 7.3:1; rose text on bone 5.7:1 for a short accent. |
| `moment` | `{moment-indigo}` | The active chapter color. Defaults to Arrival; set data-moment="02"…"04" on a section to switch (bundle.css). Always pair with a number or label. |
| `on-moment` | `{white}` | Text and strokes on the active moment field: white for 01, 02, 04; ink for 03 (periwinkle). Switched by data-moment. |
| `blue` | `{moment-indigo}` | Azul do EF (Space Indigo). Bloco de cor inteiro: topo com as cartas, cartas I, IV e VII, pastas 02 e 05, rodapé, a pergunta futurante. Texto em on-color. |
| `red` | `{moment-rose}` | Vermelho do EF (Cherry Rose). Bloco de cor inteiro: verso das cartas, cartas II e V, pastas 01 e 04, "Tire uma carta". Texto em on-color. |
| `olive` | `{moment-olive}` | Só em marcas pequenas (ex.: o verbo Cultivar da matriz). Nunca bloco grande no EF. |
| `periwinkle` | `{moment-periwinkle}` | Só em marcas pequenas com texto ink (ex.: Desnormatizar). Nunca bloco grande no EF. |
| `on-color` | `{paper}` | Texto e fios sobre blue e red: o próprio Bone (11.4:1 no azul, 5.7:1 no vermelho). |
| `on-color-muted` | `rgba(236,226,208,.72)` | Texto secundário sobre blue e red (rótulos, subtítulo do topo). Só em tamanhos de rótulo ou maiores. |
| `on-color-line` | `rgba(236,226,208,.42)` | Fios de ponta a ponta sobre blue e red. |
| `space-1` | `4px` | Optical nudges; arrow hover advance. |
| `space-2` | `8px` | Label to rule; tight inline gaps. |
| `space-3` | `12px` | Caption to plate; mobile gutter minimum. |
| `space-4` | `18px` | Directory row padding; small stacks. |
| `space-5` | `28px` | Desktop gutter maximum; paragraph groups. |
| `space-6` | `44px` | Component inner margin; touch target minimum. |
| `space-7` | `72px` | Between blocks inside a section. |
| `space-8` | `112px` | Between sections: sections breathe as printed plates. |
| `space-9` | `176px` | Chapter openers; the large open field. |
| `gutter` | `24px` | Desktop 12-column gutter (20–28px). Mobile 12–16px. |
| `outer-min` | `24px` | Lower bound of the fluid outer margin clamp(24px, 4.5vw, 84px). Mobile uses 20px. |
| `outer-max` | `84px` | Upper bound of the fluid outer margin. |
| `stack-top` | `72px` | Onde as cartas que sobem param (60px no celular). |
| `stack-step` | `14px` | Quanto cada carta empilhada desce em relação à anterior, deixando a borda de baixo à vista (8px no celular). |
| `folder-overlap` | `30px` | Quanto cada pasta sobe sobre a anterior; é a altura em que a aba se apoia. |
| `folder-tab` | `31px` | Altura da aba da pasta (1px a mais que a sobreposição, para encostar na faixa). |
| `radius-none` | `0` | The only radius. No rounded corners anywhere: tiles, buttons, images, inputs. |
| `rule` | `1px` | Primary ink rule (chapter boundary, table edge) and secondary hairline rule. Arrows in large-scale editorial. |
| `stroke-control` | `1.25px` | Arrows and strokes in small digital controls. |
| `focus-ring` | `2px` | Visible keyboard focus outline in ink (or white on moment fields), offset 3px. |
| `measure-min` | `52ch` | Shortest reading measure. |
| `measure-max` | `65ch` | Longest reading measure. |
| `open-field` | `30%` | Minimum open field in large compositions (30–45%). |
| `duration-quick` | `180ms` | Focus, underline reveal, arrow advance. |
| `duration-settle` | `320ms` | Text and line reveals. |
| `duration-chapter` | `720ms` | Chapter color-field fade (600–900ms), only if it does not interrupt reading. |
| `orbit-turn` | `70s` | Uma volta completa do anel de cartas do topo. Nunca pausa no hover; arrastar gira. |
| `card-float` | `8s` | Ciclo da flutuação leve das cartas (translate -7px, rotação abaixo de 2.5°). |
| `card-deal` | `760ms` | Entrada de uma carta com profundidade (de -60px em Z). |

### Tipografia

Fontes (Google Fonts): Bodoni Moda (display, títulos de até 4 palavras), Newsreader (leitura e, no corte de display, frases longas: `statement`), DM Sans (utilidade), Instrument Sans (topo do site).

```html
<link href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,opsz,wght@0,6..96,400..500;1,6..96,400&family=DM+Sans:opsz,wght@9..40,400..600&family=Newsreader:ital,opsz,wght@0,6..72,300..400;1,6..72,300..400&family=Instrument+Sans:wght@400;500&display=swap" rel="stylesheet">
```

| estilo | família | tamanho / entrelinha | uso |
| --- | --- | --- | --- |
| `ef-hero` | display | 106px / 0.92 | Título do topo, sobre o azul, no meio das cartas em órbita. clamp(2.8rem, 6.6vw, 6.6rem). O subtítulo vai separado e menor. |
| `ef-big` | display | 144px / 0.88 | Título que abre a parte 1 (as cartas). clamp(3.2rem, 8.4vw, 9rem), com a parte final em itálico. |
| `ef-principle` | display | 118px / 0.9 | Nome do princípio na carta que sobe: o destaque. clamp(3rem, 7vw, 7.4rem). |
| `ef-folder` | display | 90px / 0.95 | Título da pasta. clamp(2.2rem, 5.4vw, 5.6rem), uma palavra em itálico. |
| `ef-lead` | statement | 77px / 1.06 | Frase de abertura sobre o 07 gigante. clamp(2.1rem, 4.6vw, 4.8rem), até 20ch. |
| `ef-statement` | statement | 44–77px / 1.04–1.12 | Toda frase de 5 palavras ou mais em tamanho de display: citações, perguntas das cartas, avisos, títulos longos. Newsreader 300, `font-variation-settings:"opsz" 72`, tracking −0.02em. |
| `display-xl` | display | 184px / 0.88 | Chapter openers and the website hero. Desktop clamp(5.25rem, 10vw, 11.5rem); line-height 0.83–0.94. |
| `display-l` | display | 120px / 0.94 | Secondary openers, moment tiles at scale. clamp(3.6rem, 7vw, 7.5rem). |
| `section-heading` | display | 88px / 1.0 | Section headings. clamp(2.8rem, 5vw, 5.5rem). |
| `editorial-body` | reading | 19px / 1.42 | Long-form editorial. 17–21px digital, 52–65 characters per line, left-aligned. Italic only for literary emphasis. |
| `editorial-lede` | reading | 21px / 1.38 | Opening paragraph or short descriptor under a chapter title. |
| `ui-body` | utility | 14px / 1.45 | Interface copy, forms, navigation items. |
| `annotation` | utility | 11px / 1.35 | Metadata, folios, index numbers. Uppercase, tabular numerals. Tracking +0.11em to +0.20em. |
| `caption` | utility | 10px / 1.35 | Plate captions aligned to the image edge. |
| `site-sign` | site | 15px / 1.5 | Linha de assinatura do topo, igual à home de gira.guru. |
| `site-nav` | site | 12px / 1.5 | Seções do topo e botão menu, em caixa-alta, como na home de gira.guru. |

### tokens.css

```css
:root{
  --paper:#ece2d0;
  --white:#ffffff;
  --ink:#191919;
  --muted:#5f5b52;
  --hairline:#b9ad96;
  --soft:#e2d6c0;
  --moment-indigo:#1b264f;
  --moment-olive:#646f4b;
  --moment-periwinkle:#9b7ede;
  --moment-rose:#a4243b;
  --moment:var(--moment-indigo);
  --on-moment:var(--white);
  --blue:var(--moment-indigo);
  --red:var(--moment-rose);
  --olive:var(--moment-olive);
  --periwinkle:var(--moment-periwinkle);
  --on-color:var(--paper);
  --on-color-muted:rgba(236,226,208,.72);
  --on-color-line:rgba(236,226,208,.42);
  --space-1:4px;
  --space-2:8px;
  --space-3:12px;
  --space-4:18px;
  --space-5:28px;
  --space-6:44px;
  --space-7:72px;
  --space-8:112px;
  --space-9:176px;
  --gutter:24px;
  --outer-min:24px;
  --outer-max:84px;
  --stack-top:72px;
  --stack-step:14px;
  --folder-overlap:30px;
  --folder-tab:31px;
  --radius-none:0;
  --rule:1px;
  --stroke-control:1.25px;
  --focus-ring:2px;
  --measure-min:52ch;
  --measure-max:65ch;
  --open-field:30%;
  --duration-quick:180ms;
  --duration-settle:320ms;
  --duration-chapter:720ms;
  --orbit-turn:70s;
  --card-float:8s;
  --card-deal:760ms;
  --font-display:"Bodoni Moda", Georgia, serif;
  --font-reading:Newsreader, Georgia, serif;
  --font-statement:Newsreader, Georgia, serif; /* peso 300, opsz 72: frases longas em tamanho de display */
  --font-utility:"DM Sans", Arial, sans-serif;
  --font-site:"Instrument Sans", "Helvetica Neue", Arial, sans-serif;
}
```

## CSS pronto (bundle.css)

Carregue depois de `tokens.css`.

```css
/* EF | Ética Futurante — estilos compartilhados. Carrega depois de tokens.css.
   Parte 1: base MAISON 04 (classes m-). Parte 2: estrutura híbrida EF (a página gira.guru/futurante). */
[data-moment="01"] { --moment: var(--moment-indigo);     --on-moment: var(--white); }
[data-moment="02"] { --moment: var(--moment-olive);      --on-moment: var(--white); }
[data-moment="03"] { --moment: var(--moment-periwinkle); --on-moment: var(--ink); }
[data-moment="04"] { --moment: var(--moment-rose);       --on-moment: var(--white); }

.m-page { background: var(--paper); color: var(--ink); font-family: var(--font-reading); margin: 0; font-variant-numeric: tabular-nums; }
.m-label { font-family: var(--font-utility); font-size: 11px; line-height: 1.35; font-weight: 500; letter-spacing: .12em; text-transform: uppercase; }
.m-muted { color: var(--muted); }
.m-display { font-family: var(--font-display); font-weight: 400; letter-spacing: -.035em; line-height: .92; margin: 0; }
.m-body { font-family: var(--font-reading); font-size: 19px; line-height: 1.42; max-width: var(--measure-max); margin: 0; }
.m-rule { border: 0; border-top: var(--rule) solid var(--ink); margin: 0; }
.m-hair { border: 0; border-top: var(--rule) solid var(--hairline); margin: 0; }
.m-tab { display: inline-block; border: var(--rule) solid currentColor; padding: 3px 8px 2px; }
.m-field { background: var(--moment); color: var(--on-moment); }
.m-arrow { display: inline-block; vertical-align: middle; transition: transform var(--duration-quick) ease-out; }
.m-arrow path { fill: none; stroke: currentColor; stroke-width: var(--stroke-control); stroke-linecap: square; }
.m-cta { display: inline-flex; align-items: center; gap: var(--space-3); min-height: var(--space-6); color: inherit; text-decoration: none; border-bottom: var(--rule) solid currentColor; font-family: var(--font-utility); font-size: 11px; letter-spacing: .14em; text-transform: uppercase; font-weight: 500; padding-right: var(--space-1); }
.m-cta:hover .m-arrow, .m-cta:focus-visible .m-arrow { transform: translateX(var(--space-1)); }
.m-cta:focus-visible, a:focus-visible { outline: var(--focus-ring) solid currentColor; outline-offset: 3px; }
@media (prefers-reduced-motion: reduce) { .m-arrow { transition: none; } }

/* ══════════ EF · estrutura híbrida (MAISON 04 × Maia Oazem) ══════════
   Aliases curtos usados pelo código da página; todos apontam para tokens. */
:root{
  --display:var(--font-display); --reading:var(--font-reading); --utility:var(--font-utility); --site:var(--font-site);
  --outer:clamp(20px,4.5vw,var(--outer-max));
  --s2:var(--space-2); --s3:var(--space-3); --s4:var(--space-4); --s5:var(--space-5); --s6:var(--space-6); --s7:var(--space-7); --s8:var(--space-8); --s9:var(--space-9);
  --quick:var(--duration-quick); --settle:var(--duration-settle);
}
/* ── MAISON 04 · paleta Bone / Space Indigo / Cherry Rose (+ Olive, Periwinkle na matriz) ── */

*{box-sizing:border-box;}
html{scroll-behavior:smooth;scroll-padding-top:60px;}
body{margin:0;background:var(--paper);color:var(--ink);font-family:var(--reading);font-size:19px;line-height:1.42;font-variant-numeric:tabular-nums;-webkit-font-smoothing:antialiased;}
a{color:inherit;}
a:focus-visible,summary:focus-visible,button:focus-visible{outline:2px solid currentColor;outline-offset:3px;}
button{font:inherit;color:inherit;background:none;border:0;padding:0;cursor:pointer;}
.label{font-family:var(--utility);font-size:11px;line-height:1.35;font-weight:500;letter-spacing:.14em;text-transform:uppercase;}
.wrap{padding-inline:var(--outer);}
.bleed{margin-inline:calc(var(--outer) * -1);padding-inline:var(--outer);}
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap;}
.fio{border:0;border-top:1px solid currentColor;margin:0;opacity:1;}
/* blocos de cor */
.blue{background:var(--blue);color:var(--on-color);}
.red{background:var(--red);color:var(--on-color);}
.blue .muted,.red .muted{color:var(--on-color-muted);}
.muted{color:var(--muted);}
/* cabeço corrido: fio · linha · fio */
.cabeco{display:flex;justify-content:space-between;align-items:baseline;gap:var(--s4);padding-block:var(--s3);border-top:1px solid currentColor;border-bottom:1px solid currentColor;}
.blue .cabeco,.red .cabeco{border-color:var(--on-color-line);}
@media (prefers-reduced-motion: reduce){html{scroll-behavior:auto;}}

/* ── 1. header azul: moldura + cartas em órbita ── */
.hero{position:relative;min-height:max(680px,100vh);display:flex;flex-direction:column;overflow:hidden;}
/* topo no padrão do site gira.guru (Instrument Sans, fios, assinatura, seções) */
.sfio{border:0;border-top:1px solid currentColor;margin:0;}
.blue .sfio{border-color:var(--on-color-line);}
.assin{display:flex;justify-content:space-between;align-items:center;gap:10px 16px;flex-wrap:wrap;padding-block:14px;font-family:'Instrument Sans','Helvetica Neue',Arial,sans-serif;font-size:15px;}
.assin .marcas{display:flex;align-items:center;gap:14px;text-decoration:none;}
.logo-m{width:30px;height:34px;display:block;}
.logo-m:not(.ok){display:none;}
.fagulha{width:24px;height:24px;display:block;}
.menu-botao{font-family:inherit;font-size:12px;letter-spacing:.09em;text-transform:uppercase;display:flex;align-items:center;gap:10px;padding:4px 0;min-height:44px;}
.menu-botao:hover{opacity:.6;}
.tracos{display:flex;flex-direction:column;gap:4px;width:20px;}
.tracos i{display:block;height:1px;background:currentColor;}
.tracos.fechar{position:relative;height:12px;}
.tracos.fechar i{position:absolute;left:0;right:0;top:6px;}
.tracos.fechar i:first-child{transform:rotate(45deg);} .tracos.fechar i:last-child{transform:rotate(-45deg);}
.secoes{display:flex;flex-wrap:wrap;gap:6px 28px;padding-block:12px;font-family:'Instrument Sans','Helvetica Neue',Arial,sans-serif;font-size:12px;letter-spacing:.09em;text-transform:uppercase;}
.secoes a{text-decoration:none;}
.secoes a:hover,.secoes a:focus-visible{text-decoration:underline;text-underline-offset:4px;}
.assin.meta{font-size:12px;}
.assin.meta b{font-weight:500;} .assin.meta i{color:var(--on-color-muted);}
.menu-painel{position:fixed;inset:0;z-index:50;overflow-y:auto;}
.menu-painel[hidden]{display:none;}
.menu-lista{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,2fr);gap:40px;padding-block:clamp(24px,4vw,48px);}
.smeta{font-family:'Instrument Sans',Arial,sans-serif;font-size:12px;padding-top:14px;}
.menu-lista ul{list-style:none;margin:0;padding:0;border-top:1px solid var(--on-color-line);}
.menu-lista li{border-bottom:1px solid var(--on-color-line);}
.menu-lista a{display:block;text-decoration:none;font-family:var(--display);font-size:clamp(32px,4.6vw,60px);line-height:1.1;padding-block:8px;letter-spacing:-.02em;}
.menu-lista a:hover,.menu-lista a:focus-visible{font-style:italic;}
.menu-lista .seta{display:inline-block;font-family:'Instrument Sans',Arial,sans-serif;font-size:.42em;vertical-align:.25em;margin-right:.4em;}
@media (prefers-reduced-motion: no-preference){.menu-painel:not([hidden]){animation:painel .35s cubic-bezier(.2,.7,.2,1);} @keyframes painel{from{opacity:0;}to{opacity:1;}}}
@media (max-width:860px){.menu-lista{grid-template-columns:1fr;gap:12px;}}
@media (max-width:560px){.secoes{flex-wrap:nowrap;overflow-x:auto;gap:22px;scrollbar-width:none;}.secoes a{white-space:nowrap;}}
.field{position:relative;flex:1;min-height:520px;}
.stage{position:absolute;inset:0;perspective:2400px;perspective-origin:50% 42%;}
.scene{position:absolute;inset:0;transform-style:preserve-3d;}
.ring{position:absolute;left:50%;top:50%;width:0;height:0;transform-style:preserve-3d;
  --r:min(40vw,540px); --tilt:-15deg;
  transform:rotateX(var(--tilt)) rotateY(0deg);}
.stage{cursor:grab;touch-action:pan-y;}
.stage.dragging{cursor:grabbing;}
.orbit-card,.orbit-card img{-webkit-user-drag:none;user-select:none;}
.orbit-card{--w:clamp(78px,9vw,112px);position:absolute;left:calc(var(--w)/-2);top:calc(var(--w)*-0.857);width:var(--w);aspect-ratio:7/12;
  transform-style:preserve-3d;transform:rotateY(calc(var(--i) * 360deg / 7)) translateZ(var(--r));text-decoration:none;color:var(--ink);}
.face{position:absolute;inset:0;backface-visibility:hidden;-webkit-backface-visibility:hidden;}
.front{background:var(--paper);padding:calc(var(--w)*.07);display:flex;flex-direction:column;gap:calc(var(--w)*.05);transition:transform var(--quick) ease-out;}
.front img{display:block;width:100%;aspect-ratio:3/4;object-fit:cover;border:1px solid var(--ink);}
.mini-tab{align-self:center;font-family:var(--display);font-size:calc(var(--w)*.13);line-height:1;padding:2px 6px 1px;border:1px solid var(--ink);margin-top:-1px;}
.mini-name{font-family:var(--display);font-size:calc(var(--w)*.115);line-height:1.02;letter-spacing:-.02em;margin-top:auto;}
.back{transform:rotateY(180deg);background:var(--red);display:grid;place-items:center;}
.back span{font-family:var(--display);color:var(--paper);font-size:calc(var(--w)*.2);border:1px solid var(--on-color-line);padding:4px 10px 2px;}
.orbit-card:hover .front{transform:translateY(-6px);}
.hero-title{position:absolute;left:0;right:0;top:40%;transform:translate3d(0,-50%,0);text-align:center;pointer-events:none;padding:0 var(--outer);}
.hero-title h1,.hero-title .h1{margin:0;font-family:var(--display);font-weight:400;font-size:clamp(2.8rem,6.6vw,6.6rem);line-height:.92;letter-spacing:-.04em;}
.hero-title .sub{display:block;margin:var(--s4) 0 0;font-family:var(--display);font-weight:400;font-size:clamp(1.25rem,2.2vw,2rem);line-height:1.1;letter-spacing:-.015em;color:var(--on-color-muted);}
.hero-title i{font-style:italic;}
.hero-foot{display:flex;justify-content:space-between;gap:var(--s4);padding-block:var(--s3) var(--s5);border-top:1px solid var(--on-color-line);}
.hero-title.mobile{display:none;}
@media (max-width:640px){
  .hero{min-height:0;}
  .field{flex:none;min-height:0;height:330px;}
  .stage{perspective:900px;}
  .ring{--r:36vw;--tilt:-14deg;top:48%;}
  .orbit-card{--w:66px;}
  .scene > .hero-title{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);}
  .hero-title.mobile{display:block;position:static;transform:none;padding:0 0 var(--s6);text-align:left;}
  .hero-title.mobile .h1{font-size:clamp(2.4rem,11vw,3.4rem);}
  .assin.meta .hint{display:none;}
}

/* ── 2. abertura: recuo grande + metadados ── */
.opening{position:relative;isolation:isolate;padding-block:var(--s9) var(--s9);display:grid;grid-template-columns:3fr 9fr;gap:var(--gutter);}
.opening > *{position:relative;z-index:1;}
.opening .seven-bg{position:absolute;z-index:0;right:-.04em;top:50%;transform:translateY(-52%);font-family:var(--display);font-weight:400;font-size:clamp(16rem,46vw,46rem);line-height:.8;letter-spacing:-.06em;color:#dfd2b9;pointer-events:none;user-select:none;}
.opening .lead{margin:0;font-size:clamp(24px,2.9vw,40px);line-height:1.22;letter-spacing:-.005em;text-indent:24%;max-width:30ch;}
.opening .seven{margin:var(--s6) 0 0;max-width:46ch;margin-left:auto;margin-right:12%;}
.meta-row{display:grid;grid-template-columns:repeat(4,1fr);gap:var(--gutter);border-top:1px solid var(--ink);border-bottom:1px solid var(--ink);padding-block:var(--s4);}
.meta-row div{display:flex;flex-direction:column;gap:6px;}
.meta-row span:last-child{font-family:var(--display);font-size:22px;line-height:1.1;letter-spacing:-.01em;}
@media (max-width:820px){
  .opening{grid-template-columns:1fr;padding-block:var(--s8) var(--s8);}
  .opening .seven-bg{font-size:72vw;}
  .opening .lead{text-indent:18%;}
  .opening .seven{margin:var(--s5) 0 0;}
  .meta-row{grid-template-columns:1fr 1fr;row-gap:var(--s4);}
}

/* ── 3. vermelho: possível / necessária ── */


/* ── 4. tríade: lista numerada ── */
.triad{padding-block:var(--s8) var(--s8);}
.triad-head{display:grid;grid-template-columns:3fr 9fr;gap:var(--gutter);align-items:baseline;margin-bottom:var(--s5);}
.triad-head h2{margin:0;font-family:var(--display);font-weight:400;font-size:clamp(1.8rem,3vw,2.8rem);line-height:1;letter-spacing:-.03em;}
.triad-head h2 i{font-style:italic;}
.triad-head p{margin:0;font-size:17px;color:var(--muted);}
@media (max-width:820px){.triad-head{grid-template-columns:1fr;gap:var(--s2);}}
.triad ol{list-style:none;margin:0;padding:0;border-top:1px solid var(--ink);}
.triad li{display:grid;grid-template-columns:64px 1fr auto;gap:var(--gutter);align-items:baseline;padding-block:var(--s3);border-bottom:1px solid var(--hairline);}
.triad .n{font-family:var(--display);font-size:16px;color:var(--muted);}
.triad .t{font-family:var(--display);font-style:italic;font-size:clamp(1.25rem,1.9vw,1.75rem);line-height:1;letter-spacing:-.025em;}
.triad .a{text-align:right;color:var(--muted);}
@media (max-width:820px){ .triad li{grid-template-columns:40px 1fr;} .triad .a{grid-column:2;text-align:left;} }

/* ── menu de seções ── */
.sections-nav{position:sticky;top:0;z-index:10;background:var(--paper);border-top:1px solid var(--ink);border-bottom:1px solid var(--hairline);}
.sections-nav ul{list-style:none;margin:0;padding:0;display:flex;gap:var(--s5);overflow-x:auto;scrollbar-width:none;}
.sections-nav a{display:flex;align-items:center;gap:8px;min-height:52px;text-decoration:none;white-space:nowrap;border-bottom:1px solid transparent;transition:border-color var(--quick) ease-out;}
.sections-nav a span{color:var(--muted);}
.sections-nav a:hover,.sections-nav a[aria-current="true"]{border-bottom-color:var(--ink);}

/* ── seções ── */
.section{padding-block:var(--s7) var(--s8);}
.section-title{display:grid;grid-template-columns:3fr 9fr;gap:var(--gutter);align-items:end;margin:var(--s7) 0 var(--s7);}
.folio-big{font-family:var(--display);font-size:clamp(4rem,9vw,9rem);line-height:.8;color:var(--hairline);letter-spacing:-.04em;}
.section-title h2{margin:0;font-family:var(--display);font-weight:400;font-size:clamp(3rem,7vw,7.5rem);line-height:.9;letter-spacing:-.04em;}
.section-title h2 i{font-style:italic;}

/* olho em faixas */
.bands{border-top:1px solid var(--ink);margin-bottom:var(--s7);}
#mudar-como-mudamos .cols{margin-bottom:0;}
.bands p{margin:0;display:grid;grid-template-columns:3fr 9fr;gap:var(--gutter);align-items:baseline;padding-block:var(--s4);border-bottom:1px solid var(--ink);font-family:var(--display);font-size:clamp(1.8rem,3.8vw,3.8rem);line-height:1;letter-spacing:-.03em;}
.bands p .label{font-size:11px;letter-spacing:.14em;}
.bands p:nth-child(2) span:last-child{font-style:italic;color:var(--muted);}
.cols{display:grid;grid-template-columns:3fr 4.5fr 4.5fr;gap:var(--gutter);margin-bottom:var(--s8);}
.cols p{margin:0 0 1em;}
.cols .first::first-line{font-variant-caps:all-small-caps;letter-spacing:.06em;}
@media (max-width:820px){
  .section-title{grid-template-columns:1fr;gap:var(--s3);}
  .bands p{grid-template-columns:1fr;gap:6px;}
  .cols{grid-template-columns:1fr;}
}

/* lista dos 7 princípios */
.toolkit-note{display:grid;grid-template-columns:9fr 3fr;gap:var(--gutter);align-items:end;border-top:2px solid var(--ink);padding-block:var(--s6) var(--s7);}
.toolkit-note h3{margin:0;font-family:var(--display);font-weight:400;font-size:clamp(3rem,7.4vw,8rem);line-height:.9;letter-spacing:-.045em;}
.toolkit-note h3 i{font-style:italic;}
.tk-side p{margin:var(--s3) 0 0;font-size:18px;line-height:1.4;color:var(--muted);}
@media (max-width:820px){.toolkit-note{grid-template-columns:1fr;}}
.principles{list-style:none;margin:0;padding:0;}
.principles li{border-bottom:1px solid var(--hairline);}
.principle summary{list-style:none;cursor:pointer;display:grid;grid-template-columns:150px minmax(0,6fr) minmax(0,5fr) 150px;gap:var(--gutter);align-items:baseline;padding-block:var(--s7) var(--s7);transition:background var(--quick) ease-out;}
.principle summary::-webkit-details-marker{display:none;}
.p-num{font-family:var(--display);font-size:clamp(3rem,6.2vw,6.4rem);line-height:.9;letter-spacing:-.03em;color:var(--hairline);transition:color var(--quick) ease-out;}
.principle summary:hover .p-num,.principle[open] .p-num{color:var(--red);}
.p-name{display:block;font-family:var(--display);font-size:clamp(2.2rem,4.4vw,4.6rem);line-height:.96;letter-spacing:-.035em;}
.p-label{display:block;margin-top:var(--s4);font-family:var(--utility);font-size:13px;font-weight:500;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);}
.p-short{font-size:clamp(19px,1.6vw,23px);line-height:1.38;max-width:38ch;}
.p-toggle{justify-self:end;display:inline-flex;align-items:center;gap:var(--s3);min-height:44px;font-family:var(--utility);font-size:11px;font-weight:500;letter-spacing:.14em;text-transform:uppercase;border-bottom:1px solid var(--ink);white-space:nowrap;}
.p-toggle svg path{fill:none;stroke:currentColor;stroke-width:1.25;}
.p-toggle svg{transition:transform var(--quick) ease-out;}
.principle summary:hover .p-toggle svg{transform:translateX(4px);}
.principle[open] .p-toggle svg{transform:rotate(90deg);}
.t-close{display:none;} .principle[open] .t-open{display:none;} .principle[open] .t-close{display:inline;}
.principle.flash summary{background:var(--soft);}
.card-text{display:grid;grid-template-columns:150px minmax(0,6fr) minmax(0,5fr) 150px;gap:var(--s5) var(--gutter);padding-bottom:var(--s6);}
.ct-concept{grid-column:2;}
.ct-body{grid-column:3;}
.card-text .label{display:block;color:var(--muted);margin-bottom:var(--s3);}
.ct-body .label:not(:first-child){margin-top:var(--s5);}
.concept{margin:0;font-family:var(--display);font-style:italic;font-size:clamp(1.5rem,2.2vw,2rem);line-height:1.12;letter-spacing:-.02em;}
.ct-body p{margin:0 0 .8em;max-width:60ch;}
/* a carta aparece dentro do bloco quando ele abre */
.ct-card{margin:var(--s6) 0 0;max-width:340px;}
.principle[open] .card-text{perspective:1200px;animation:rise 640ms cubic-bezier(.2,.7,.2,1) both;}
@keyframes rise{from{opacity:0;transform:translateY(14px) rotateX(5deg) scale(.99);transform-origin:50% 0;}to{opacity:1;transform:none;}}
.ct-concept{perspective:900px;}
.principle[open] .ct-card{transform-style:preserve-3d;animation:deal 760ms cubic-bezier(.2,.7,.2,1) both, float 7s ease-in-out 760ms infinite;}
@keyframes deal{from{opacity:0;transform:translate3d(0,24px,-60px) rotateX(10deg) rotateY(-6deg);}to{opacity:1;transform:none;}}
@keyframes float{0%,100%{transform:none;}50%{transform:translate3d(0,-7px,12px) rotateX(1.6deg) rotateY(-2.4deg);}}
@media (prefers-reduced-motion: reduce){.principle[open] .ct-card,.principle[open] .card-text{animation:none;}}
.tarot{display:block;width:100%;height:auto;aspect-ratio:7/12;}
.tarot .tbg{fill:var(--paper);}
.tarot .tb{font-family:var(--utility);font-weight:500;letter-spacing:.16em;fill:var(--ink);text-transform:uppercase;}
.tarot .tl{fill:none;stroke:var(--ink);stroke-width:1.5;}
.tarot .th{stroke:var(--hairline);stroke-width:1.5;}
.tarot .ttab{fill:var(--paper);stroke:var(--ink);stroke-width:1.5;}
.tarot .tnum{font-family:var(--display);font-size:46px;fill:var(--ink);}
.tarot .tp{font-family:var(--display);font-size:78px;letter-spacing:-.03em;fill:var(--ink);}
.tarot .tn{font-family:var(--utility);font-weight:500;font-size:18px;letter-spacing:.16em;fill:var(--ink);}
.tarot .tm{font-family:var(--utility);font-weight:500;font-size:16px;letter-spacing:.16em;fill:var(--muted);}
.ct-card{outline:1px solid var(--hairline);outline-offset:-1px;}
/* a pergunta futurante abre um bloco azul */
.ct-question{grid-column:1 / -1;display:grid;grid-template-columns:150px minmax(0,6fr) minmax(0,5fr) 150px;gap:var(--gutter);padding:var(--s6) 0 var(--s7);margin-top:var(--s4);background:var(--blue);color:var(--on-color);margin-inline:calc(var(--outer) * -1);padding-inline:var(--outer);}
.ct-question .label{grid-column:2;color:var(--on-color-muted);}
.ct-question p{grid-column:3 / 5;margin:0;font-family:var(--display);font-size:clamp(1.7rem,2.8vw,2.8rem);line-height:1.08;letter-spacing:-.025em;}
@media (max-width:900px){
  .principle summary{grid-template-columns:64px 1fr;row-gap:var(--s4);padding-block:var(--s6);}
  .p-short{grid-column:2;} .p-toggle{grid-column:2;justify-self:start;}
  .card-text{grid-template-columns:64px 1fr;}
  .ct-concept,.ct-body{grid-column:2;}
  .ct-card{max-width:260px;}
  .ct-question{grid-template-columns:64px 1fr;}
  .ct-question .label,.ct-question p{grid-column:2;}
}

/* ── seções abre e fecha ── */
.fold{border-top:1px solid var(--ink);transition:background var(--settle) ease-out;}
.fold:not([open]){background:var(--white);}
.fold:last-of-type{border-bottom:1px solid var(--ink);}
.fold > summary{list-style:none;cursor:pointer;display:grid;grid-template-columns:3fr 9fr;gap:var(--gutter);align-items:end;padding-block:var(--s6);}
.fold > summary::-webkit-details-marker{display:none;}
.fold .folio-big{font-size:clamp(3rem,6vw,6rem);}
.fold .head{display:flex;justify-content:space-between;align-items:baseline;gap:var(--s4);}
.fold h2{margin:0;font-family:var(--display);font-weight:400;font-size:clamp(2.2rem,5vw,5.2rem);line-height:.95;letter-spacing:-.035em;}
.fold h2 i{font-style:italic;}
.fold .mark{font-family:var(--utility);font-size:24px;line-height:1;width:44px;height:44px;display:grid;place-items:center;border:1px solid var(--ink);flex:none;}
.mark i{font-style:normal;display:block;transition:transform var(--quick) ease-out;}
.fold[open] .mark i{transform:rotate(45deg);}
.fold > summary:hover .folio-big{color:var(--red);}
.fold-body{padding-bottom:var(--s8);}
.fold-grid{display:grid;grid-template-columns:3fr 9fr;gap:var(--gutter);}
.fold-grid .text{max-width:64ch;}
.fold-grid .text p{margin:0 0 1em;}
.lede{margin:0 0 var(--s6);font-family:var(--display);font-size:clamp(1.7rem,3vw,2.8rem);line-height:1.08;letter-spacing:-.025em;max-width:26ch;}
.note{font-size:15px;line-height:1.45;color:var(--muted);border-top:1px solid var(--hairline);padding-top:var(--s3);margin-top:var(--s5);}
@media (max-width:820px){ .fold > summary,.fold-grid{grid-template-columns:1fr;gap:var(--s3);} }

/* esperança: cartaz azul com o horizonte */
.horizon{margin-block:var(--s6) var(--s7);padding-block:var(--s5) var(--s7);}
.horizon .cabeco{border-top:0;margin-bottom:var(--s7);}
.horizon blockquote{margin:0;font-family:var(--display);font-size:clamp(1.8rem,3.4vw,3.4rem);line-height:1.1;letter-spacing:-.025em;max-width:28ch;}
.horizon blockquote i{font-style:italic;}
.horizon cite{display:block;margin-top:var(--s5);font-style:normal;}
.walk{margin-top:var(--s7);position:relative;height:72px;}
.walk .line{position:absolute;left:0;right:0;top:36px;border-top:1px solid var(--on-color-line);}
.walk .me,.walk .hz{position:absolute;top:0;display:flex;flex-direction:column;align-items:center;gap:6px;transform:translateX(-50%);transition:left 120ms linear;}
.walk .me i{display:block;width:10px;height:10px;background:var(--on-color);margin-top:25px;}
.walk .hz i{display:block;width:1px;height:28px;background:var(--on-color);margin-top:22px;}
.walk .label{white-space:nowrap;color:var(--on-color-muted);}
.walk .steps{position:absolute;right:0;bottom:-6px;}

/* por que futurante: espécime */
.specimen{border-top:1px solid var(--ink);margin-bottom:var(--s7);}
.specimen .row{display:grid;grid-template-columns:3fr 6fr 3fr;gap:var(--gutter);align-items:baseline;padding-block:var(--s5);border-bottom:1px solid var(--ink);}
.specimen .word{font-family:var(--display);font-size:clamp(3rem,9vw,9rem);line-height:.9;letter-spacing:-.045em;white-space:nowrap;}
.specimen .word i{font-style:italic;color:var(--red);}
.specimen .row:first-child .word i{color:var(--muted);}
.specimen .def{font-size:16px;line-height:1.45;margin:0;}
.stem{display:inline-block;transition:opacity var(--settle) ease-out;}
.stem.off{opacity:0;}
@media (max-width:820px){ .specimen .row{grid-template-columns:1fr;gap:var(--s3);} }

/* neomaqueerismo: matriz */
.matrix{display:grid;grid-template-columns:1fr minmax(120px,.55fr) 1fr;grid-template-rows:auto auto auto;margin-block:var(--s7);position:relative;}
.matrix::before,.matrix::after{content:'';position:absolute;background:var(--ink);}
.matrix::before{left:0;right:0;top:50%;height:1px;}
.matrix::after{top:0;bottom:0;left:50%;width:1px;}
.q{position:relative;z-index:1;background:var(--paper);padding:var(--s5);max-width:420px;}
.q-ma{grid-column:2;grid-row:1;justify-self:center;text-align:center;margin-bottom:var(--s6);width:min(420px,80vw);}
.q-neo{grid-column:1;grid-row:2;justify-self:start;}
.q-queer{grid-column:3;grid-row:2;justify-self:end;text-align:right;}
.q-ismo{grid-column:2;grid-row:3;justify-self:center;text-align:center;margin-top:var(--s6);width:min(420px,80vw);}
.q-center{grid-column:2;grid-row:2;align-self:center;justify-self:center;z-index:1;background:var(--paper);padding:var(--s3) var(--s4);border:1px solid var(--ink);}
.q h3{margin:0;font-family:var(--display);font-weight:400;font-size:clamp(2.4rem,4vw,3.6rem);line-height:.95;letter-spacing:-.03em;}
.q .verb{display:inline-block;margin:var(--s2) 0 var(--s4);padding:3px 8px 2px;color:var(--white);}
.q-ma .verb{background:var(--red);} .q-neo .verb{background:var(--blue);}
.q-queer .verb{background:var(--periwinkle);color:var(--ink);} .q-ismo .verb{background:var(--olive);}
.q strong{display:block;font-family:var(--reading);font-weight:400;font-style:italic;font-size:19px;line-height:1.3;margin-bottom:var(--s2);}
.q p{margin:0;font-size:16px;line-height:1.45;}
@media (max-width:820px){
  .matrix{grid-template-columns:1fr;}
  .matrix::before,.matrix::after,.q-center{display:none;}
  .q,.q-ma,.q-ismo,.q-neo,.q-queer{grid-column:1;grid-row:auto;justify-self:stretch;text-align:left;width:auto;max-width:none;margin:0;padding:var(--s5) 0;border-top:1px solid var(--hairline);}
}
/* coda vermelha */
.queer{padding-block:var(--s5) var(--s8);}
.queer .cabeco{border-top:0;margin-bottom:var(--s7);}
.queer .big{margin:0 0 var(--s6);font-family:var(--display);font-size:clamp(2.2rem,5.4vw,5.6rem);line-height:.95;letter-spacing:-.035em;max-width:16ch;}
.queer .big i{font-style:italic;}
.queer .grid{display:grid;grid-template-columns:3fr 9fr;gap:var(--gutter);}
.queer .grid p{margin:0;max-width:62ch;font-size:20px;}
@media (max-width:820px){ .queer .grid{grid-template-columns:1fr;} }

/* ── final: tire uma carta ── */
.draw{padding-block:var(--s8) var(--s8);}
.draw .label{display:block;margin-bottom:var(--s5);}
.draw button{display:flex;align-items:baseline;gap:.25em;font-family:var(--display);font-size:clamp(3.4rem,12vw,12.5rem);line-height:.88;letter-spacing:-.05em;text-align:left;}
.draw button i{font-style:italic;}
.draw svg{width:.6em;height:.3em;flex:none;transition:transform var(--quick) ease-out;}
.draw svg path{fill:none;stroke:currentColor;stroke-width:1.2;vector-effect:non-scaling-stroke;}
.draw button:hover svg{transform:translateX(12px);}
.draw button:hover i{text-decoration:underline;text-decoration-thickness:1px;text-underline-offset:.12em;}

footer{padding-block:var(--s6) var(--s7);display:grid;grid-template-columns:3fr 9fr;gap:var(--gutter);color:var(--on-color-muted);}
footer p{margin:0 0 6px;font-size:13px;line-height:1.5;}
footer .label{color:var(--on-color);}
@media (max-width:820px){footer{grid-template-columns:1fr;}}

/* ══════════ v4 · versão resumida ══════════ */
.white{background:var(--white);color:var(--ink);}

/* abertura com o 07 atrás */
.intro{position:relative;isolation:isolate;overflow:hidden;min-height:min(92vh,880px);display:flex;align-items:center;padding-block:var(--s9);}
.intro .seven-bg{position:absolute;z-index:-1;right:-.05em;top:50%;transform:translateY(-50%);font-family:var(--display);font-size:clamp(18rem,58vw,60rem);line-height:.78;letter-spacing:-.07em;color:#dfd2b9;pointer-events:none;user-select:none;}
.intro-lead{margin:0;max-width:20ch;font-family:var(--display);font-size:clamp(2.1rem,4.6vw,4.8rem);line-height:1.02;letter-spacing:-.035em;}
.intro-lead i{font-style:italic;}
@media (max-width:640px){ .intro{min-height:0;padding-block:var(--s8);} .intro .seven-bg{font-size:90vw;} }

/* título dos princípios */
.principles-sec{padding-bottom:var(--s8);}
.big-h{margin:0 0 var(--s7);padding-top:var(--s5);border-top:2px solid var(--ink);font-family:var(--display);font-weight:400;font-size:clamp(3.2rem,8.4vw,9rem);line-height:.88;letter-spacing:-.05em;}
.big-h i{font-style:italic;}

/* parte 1 · cartas que sobem e empilham */
.stack{list-style:none;margin:0;padding:0;--top:72px;}
.stack-item{display:contents;}
.anchor{display:block;height:0;scroll-margin-top:calc(var(--top) + 8px);}
.stack-item + .stack-item .anchor{margin-top:14vh;}
.stack-card{position:sticky;top:calc(var(--top) + var(--i) * 14px);min-height:min(78vh,760px);display:grid;grid-template-columns:minmax(0,7fr) minmax(0,5fr);gap:var(--s6);align-items:center;padding:var(--s6) clamp(24px,4vw,64px);transform-origin:50% 0;will-change:transform;border:1px solid transparent;}
.stack-card.white{border-color:var(--ink);}
.sc-text{display:flex;flex-direction:column;align-self:stretch;}
.sc-num{font-family:var(--display);font-size:clamp(3.6rem,7vw,7rem);line-height:.8;letter-spacing:-.04em;opacity:.55;}
.sc-principle{margin:auto 0 0;padding-top:var(--s6);font-family:var(--display);font-weight:400;font-size:clamp(3rem,7vw,7.4rem);line-height:.9;letter-spacing:-.045em;}
.sc-name{margin:var(--s4) 0 0;font-family:var(--display);font-style:italic;font-size:clamp(1.3rem,2vw,1.9rem);line-height:1.1;letter-spacing:-.015em;opacity:.72;}
.sc-short{margin:var(--s6) 0 0;font-size:clamp(19px,1.7vw,24px);line-height:1.36;max-width:34ch;}
.sc-more{align-self:flex-start;display:inline-flex;align-items:center;gap:var(--s3);min-height:44px;margin-top:var(--s5);font-family:var(--utility);font-size:11px;font-weight:500;letter-spacing:.14em;text-transform:uppercase;border-bottom:1px solid currentColor;}
.sc-more svg path{fill:none;stroke:currentColor;stroke-width:1.25;}
.sc-more svg{transition:transform var(--quick) ease-out;}
.sc-more:hover svg{transform:translateX(4px);}
.sc-card{margin:0;justify-self:center;width:min(100%,340px);}
.sc-card .tarot{animation:float 8s ease-in-out infinite;}
.stack-card:nth-child(even) .sc-card .tarot{animation-delay:-3s;}
@media (prefers-reduced-motion: reduce){ .sc-card .tarot{animation:none;} }
@media (max-width:820px){
  .stack{--top:60px;}
  .stack-item + .stack-item .anchor{margin-top:8vh;}
  .stack-card{grid-template-columns:1fr;min-height:0;padding:var(--s5) 20px var(--s6);gap:var(--s5);top:calc(var(--top) + var(--i) * 8px);}
  .sc-principle{padding-top:var(--s5);}
  .stack-card{position:sticky;}
  .sc-card{position:absolute;top:var(--s5);right:20px;width:min(26vw,104px);}
  .sc-principle{max-width:calc(100% - 8px);}
  .sc-num{min-height:calc(min(26vw,104px) * 1.62);}
}

/* parte 2 · pastas */
.folders{padding-top:var(--s7);padding-bottom:var(--s7);}
.folders-head{display:flex;justify-content:space-between;padding-bottom:var(--s7);}
.folder{position:relative;z-index:calc(var(--i) + 1);margin-top:-30px;background:transparent;}
.folder:first-of-type{margin-top:0;}
.folder > summary{list-style:none;cursor:pointer;display:block;position:relative;padding-top:30px;transition:transform var(--settle) cubic-bezier(.2,.7,.2,1);}
.folder > summary::-webkit-details-marker{display:none;}
.folder:not([open]) > summary:hover{transform:translateY(-14px);}
.folder > summary .f-band{position:relative;}
.folder:not([open]):not(:last-of-type) > summary .f-band::after{content:"";position:absolute;left:0;right:0;top:100%;height:calc(var(--s5) + 14px);background:inherit;pointer-events:none;}
.folder .tab{position:absolute;top:0;left:calc(var(--outer) + var(--i) * min(16%, 200px));height:31px;min-width:150px;display:flex;align-items:center;padding:0 var(--s5) 0 var(--s4);clip-path:polygon(0 0,calc(100% - 22px) 0,100% 100%,0 100%);font-family:var(--utility);font-size:11px;font-weight:500;letter-spacing:.14em;}
.folder .f-band{display:flex;justify-content:space-between;align-items:center;gap:var(--s4);min-height:150px;padding:var(--s5) var(--outer) calc(var(--s5) + 30px);}
.folder h2{margin:0;font-family:var(--display);font-weight:400;font-size:clamp(2.2rem,5.4vw,5.6rem);line-height:.95;letter-spacing:-.04em;}
.folder h2 i{font-style:italic;}
.folder .mark{font-family:var(--utility);font-size:24px;line-height:1;width:44px;height:44px;display:grid;place-items:center;border:1px solid currentColor;flex:none;}
.folder .mark i{font-style:normal;display:block;transition:transform var(--quick) ease-out;}
.folder[open] .mark i{transform:rotate(45deg);}
.folder.red .tab,.folder.red .f-band{background:var(--red);color:var(--on-color);}
.folder.blue .tab,.folder.blue .f-band{background:var(--blue);color:var(--on-color);}
.folder.white .tab,.folder.white .f-band{background:var(--white);color:var(--ink);}
.folder.white .f-band{border-top:1px solid var(--ink);}
.folder .tab,.folder .f-band{box-shadow:none;}
.f-body{background:var(--paper);color:var(--ink);padding-top:var(--s7);padding-bottom:calc(var(--s8) + 30px);border-top:0;}
.folder[open] .f-body{animation:unfold 520ms cubic-bezier(.2,.7,.2,1) both;}
@keyframes unfold{from{opacity:0;transform:translateY(-18px);}to{opacity:1;transform:none;}}
@media (prefers-reduced-motion: reduce){ .folder > summary,.folder[open] .f-body{transition:none;animation:none;} }
.folder .triad{padding:0;}
.folder .bands{margin-bottom:var(--s6);}
@media (max-width:640px){
  .folder .tab{left:calc(20px + var(--i) * 13%);min-width:96px;}
  .folder .f-band{min-height:120px;}
}

/* carta inteira: diálogo */
dialog.carta{width:min(1180px,calc(100vw - 32px));max-height:calc(100vh - 32px);padding:0;border:0;background:var(--paper);color:var(--ink);overflow:auto;}
dialog.carta::backdrop{background:rgba(27,38,79,.86);}
dialog.carta[open]{animation:rise 520ms cubic-bezier(.2,.7,.2,1) both;}
.carta-in{padding:var(--s5) clamp(20px,4vw,56px) var(--s6);}
.carta-top{display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid var(--ink);padding-bottom:var(--s3);margin-bottom:var(--s6);font-family:'Instrument Sans',Arial,sans-serif;}
.carta-grid{display:grid;grid-template-columns:5fr 7fr;gap:var(--s6);}
.carta-head h3{margin:0;font-family:var(--display);font-weight:400;font-size:clamp(2.4rem,4.6vw,4.4rem);line-height:.92;letter-spacing:-.04em;}
.carta-head .sc-name{margin-bottom:var(--s6);}
.carta-grid .label{display:block;color:var(--muted);margin-bottom:var(--s3);}
.carta-body .label:not(:first-child){margin-top:var(--s5);}
.carta-body p{margin:0 0 .8em;max-width:60ch;}
.carta-q{margin:0;padding:var(--s5) clamp(20px,4vw,56px) var(--s6);background:var(--blue);color:var(--on-color);display:grid;grid-template-columns:5fr 7fr;gap:var(--s6);}
.carta-q .label{color:var(--on-color-muted);}
.carta-q p{margin:0;font-family:var(--display);font-size:clamp(1.6rem,2.6vw,2.6rem);line-height:1.08;letter-spacing:-.025em;}
@media (max-width:820px){ .carta-grid,.carta-q{grid-template-columns:1fr;gap:var(--s3);} }
```

## Componentes da estrutura EF

### SiteTop

O topo de toda página EF repete a home de gira.guru: fio, assinatura (o M, a fagulha e "Maia Oazem · laborateliê", com link para a home) e o botão "menu", fio, as seções da página em caixa-alta, fio.

- Fonte do site: Instrument Sans (`--font-site`), `site-sign` 15px e `site-nav` 12px com +0.09em.
- No EF o topo vive dentro do bloco `blue`; fios em `on-color-line`, texto em `on-color`.
- O desenho do M não é copiado: a página busca o símbolo `#m` na home (`fetch('/')`) e só então mostra o `.logo-m`. Fora de gira.guru, aparecem só a fagulha e o texto.
- O menu abre um painel azul em tela cheia com "outras páginas" (início, portfólio, lab aberto, cv, Clube de Contexto) em Bodoni grande e o contato sob um fio.
- Quem usa fornece: as seções da página (âncoras) e, se quiser, o idioma.

```html
<svg width="0" height="0" style="position:absolute" aria-hidden="true"><symbol id="fagulha" viewBox="0 0 100 100"><path fill="currentColor" d="M53 8L91 72H15Z"/><path fill="currentColor" d="M43 94L9 36H77Z"/></symbol></svg><header class="blue wrap" style="padding-bottom:12px"><hr class="sfio">
  <div class="assin">
    <a class="marcas" href="#"><svg class="logo-m" viewBox="20 19 576 656" aria-hidden="true"><use href="#m"></use></svg><svg class="fagulha" viewBox="0 0 100 100" aria-hidden="true"><use href="#fagulha"></use></svg><span>Maia Oazem · laborateliê</span></a>
    <button type="button" class="menu-botao"><span class="tracos" aria-hidden="true"><i></i><i></i><i></i></span><span>menu</span></button>
  </div>
  <hr class="sfio">
  <nav class="secoes" aria-label="Nesta página"><a href="#">os 07 princípios</a><a href="#">outra coisa é possível</a><a href="#">esperança acionável</a><a href="#">por que futurante?</a><a href="#">neomaqueerismo</a><a href="#">tríade de livros</a></nav>
  <hr class="sfio"></header>
```

### OrbitHero

O destaque animado do topo: as sete cartas giram num anel em perspectiva em volta do título, sobre o bloco `blue`. É o único lugar da home com as imagens das cartas.

- Título em `ef-hero` ("Uma Ética Futurante"); o subtítulo ("em uma Cultura de *Esperança*") separado, menor, em `on-color-muted`.
- A frente da carta é Bone com moldura de 1px e a imagem 3:4; o verso é `red` com o numeral romano.
- Gira sempre, uma volta a cada `orbit-turn`; não para no hover. Arrastar com mouse ou dedo gira o anel com inércia e depois volta ao ritmo. Um clique sem arrastar leva à carta na página.
- As cartas da frente passam diante do título e as de trás por detrás (mesmo contexto 3D, `preserve-3d`).
- No celular o anel fica acima do título. Com `prefers-reduced-motion`, o anel não gira sozinho, mas o arraste continua.
- Quem usa fornece: as sete imagens (`01.jpg`–`07.jpg`) e os links das cartas.

```html
<header class="hero blue wrap" style="min-height:560px">
  <div class="field" style="min-height:420px"><div class="stage"><div class="scene">
    <nav class="ring" aria-label="As sete cartas"><a class="orbit-card" href="#" style="--i:0" draggable="false"><span class="face front"><span class="mini-tab">I</span><span style="display:block;aspect-ratio:3/4;background:var(--soft);border:1px solid var(--ink)"></span><span class="mini-name">Agência Futurante</span></span><span class="face back" aria-hidden="true"><span>I</span></span></a><a class="orbit-card" href="#" style="--i:1" draggable="false"><span class="face front"><span class="mini-tab">II</span><span style="display:block;aspect-ratio:3/4;background:var(--soft);border:1px solid var(--ink)"></span><span class="mini-name">Imaginação Fértil</span></span><span class="face back" aria-hidden="true"><span>II</span></span></a><a class="orbit-card" href="#" style="--i:2" draggable="false"><span class="face front"><span class="mini-tab">III</span><span style="display:block;aspect-ratio:3/4;background:var(--soft);border:1px solid var(--ink)"></span><span class="mini-name">Horizontes de Esperança</span></span><span class="face back" aria-hidden="true"><span>III</span></span></a><a class="orbit-card" href="#" style="--i:3" draggable="false"><span class="face front"><span class="mini-tab">IV</span><span style="display:block;aspect-ratio:3/4;background:var(--soft);border:1px solid var(--ink)"></span><span class="mini-name">Eu-Mundo</span></span><span class="face back" aria-hidden="true"><span>IV</span></span></a><a class="orbit-card" href="#" style="--i:4" draggable="false"><span class="face front"><span class="mini-tab">V</span><span style="display:block;aspect-ratio:3/4;background:var(--soft);border:1px solid var(--ink)"></span><span class="mini-name">Sensibilidade Ecossistêmica</span></span><span class="face back" aria-hidden="true"><span>V</span></span></a><a class="orbit-card" href="#" style="--i:5" draggable="false"><span class="face front"><span class="mini-tab">VI</span><span style="display:block;aspect-ratio:3/4;background:var(--soft);border:1px solid var(--ink)"></span><span class="mini-name">Criador Consequente</span></span><span class="face back" aria-hidden="true"><span>VI</span></span></a><a class="orbit-card" href="#" style="--i:6" draggable="false"><span class="face front"><span class="mini-tab">VII</span><span style="display:block;aspect-ratio:3/4;background:var(--soft);border:1px solid var(--ink)"></span><span class="mini-name">Tecnologia Comum</span></span><span class="face back" aria-hidden="true"><span>VII</span></span></a></nav>
    <div class="hero-title"><h1>Uma Ética Futurante</h1><p class="sub">em uma Cultura de <i>Esperança</i></p></div>
  </div></div></div>
  <hr class="sfio"><div class="assin meta"><span><b>Hope Culture</b> · <i>o laborateliê da gira. é um hope lab</i></span><span class="hint">clique numa carta para lê-la</span></div>
</header>
<script>const ring=document.querySelector('.ring'),stage=document.querySelector('.stage');const reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;const base=reduce?0:-360/70;let a=0,v=base,d=null,last=performance.now();
function f(n){const dt=Math.min(.05,(n-last)/1000);last=n;if(!d){v+=(base-v)*Math.min(1,dt*1.2);a+=v*dt;}ring.style.transform=`rotateX(var(--tilt)) rotateY(${a}deg)`;requestAnimationFrame(f);}requestAnimationFrame(f);
stage.addEventListener('pointerdown',e=>{d={x:e.clientX,t:performance.now(),m:0,id:e.pointerId,c:false};});
stage.addEventListener('pointermove',e=>{if(!d)return;const n=performance.now(),dx=e.clientX-d.x,k=dx*.28;a+=k;v=k/Math.max(.008,(n-d.t)/1000);d.m+=Math.abs(dx);d.x=e.clientX;d.t=n;if(!d.c&&d.m>6){stage.setPointerCapture(d.id);stage.classList.add('dragging');d.c=true;}});
const end=()=>{if(!d)return;stage.classList.remove('dragging');if(performance.now()-d.t>120)v=base;v=Math.max(-240,Math.min(240,v));d=null;};stage.addEventListener('pointerup',end);stage.addEventListener('pointercancel',end);</script>
```

### Intro07

A abertura logo abaixo do topo: uma frase só, em `ef-lead`, com o número de princípios ("07") enorme atrás de tudo.

- O número é Bodoni em ~58vw, tom `#dfd2b9` (um passo abaixo de `soft`), decorativo e `aria-hidden`.
- Nada mais no bloco: sem rótulos, sem faixa de dados.
- A palavra final da frase pode ir em itálico.

```html
<section class="intro wrap" style="min-height:440px"><span class="seven-bg" aria-hidden="true">07</span><p class="intro-lead">Uma rede de princípios para transformar, coletiva e intencionalmente, os futuros que criamos, ao transformar nossos modos de criar <i>futuros.</i></p></section>
```

### StackCards

Parte 1 da página: os sete princípios como cartas grandes que sobem com a rolagem e param uma sobre a outra (scroll empilhado). É o destaque da página.

- Cada carta é um bloco de cor inteiro, alternando `blue`, `red`, `white` (branco com fio de 1px em ink).
- Anatomia: numeral romano, nome do princípio em `ef-principle` (o destaque), nome em inglês menor e em itálico, a frase curta, o botão "Ler a carta inteira" e a carta (Carta) flutuando ao lado.
- As cartas ficam `sticky` dentro da mesma lista; cada uma para `stack-step` mais abaixo que a anterior (`stack-top` + i × `stack-step`), deixando as bordas à vista. A de baixo recua até 3,5% por carta que chega.
- A âncora `#principio-N` fica no fluxo, antes da carta, para os links do topo funcionarem.
- No celular a carta vira miniatura no canto, para o bloco caber na tela.
- Quem usa fornece: princípio, nome, frase curta e a carta.

```html
<div class="scroller wrap"><h2 class="big-h">Os 07 Princípios <i>de Futuração</i></h2><ol class="stack" style="--top:24px"><li class="stack-item"><span class="anchor" id="principio-1"></span><article class="stack-card blue" style="--i:0">
  <div class="sc-text"><span class="sc-num" aria-hidden="true">I</span><h3 class="sc-principle">Agência Futurante</h3><p class="sc-name">One Day, Tomorrow</p><p class="sc-short">Frase curta do princípio, em uma ou duas linhas.</p>
  <button type="button" class="sc-more">Ler a carta inteira<svg width="28" height="10" viewBox="0 0 28 10" aria-hidden="true"><path d="M0 5H26M21 1L26 5L21 9"/></svg></button></div>
  <figure class="sc-card"><!-- Carta: ver o componente Carta (SVG 700×1200) --></figure></article></li><li class="stack-item"><span class="anchor" id="principio-2"></span><article class="stack-card red" style="--i:1">
  <div class="sc-text"><span class="sc-num" aria-hidden="true">II</span><h3 class="sc-principle">Imaginação Fértil</h3><p class="sc-name">The Mother Imagination World Order</p><p class="sc-short">Frase curta do princípio, em uma ou duas linhas.</p>
  <button type="button" class="sc-more">Ler a carta inteira<svg width="28" height="10" viewBox="0 0 28 10" aria-hidden="true"><path d="M0 5H26M21 1L26 5L21 9"/></svg></button></div>
  <figure class="sc-card"><!-- Carta: ver o componente Carta (SVG 700×1200) --></figure></article></li><li class="stack-item"><span class="anchor" id="principio-3"></span><article class="stack-card white" style="--i:2">
  <div class="sc-text"><span class="sc-num" aria-hidden="true">III</span><h3 class="sc-principle">Horizontes de Esperança</h3><p class="sc-name">89 Seconds To Hope</p><p class="sc-short">Frase curta do princípio, em uma ou duas linhas.</p>
  <button type="button" class="sc-more">Ler a carta inteira<svg width="28" height="10" viewBox="0 0 28 10" aria-hidden="true"><path d="M0 5H26M21 1L26 5L21 9"/></svg></button></div>
  <figure class="sc-card"><!-- Carta: ver o componente Carta (SVG 700×1200) --></figure></article></li></ol><div style="height:400px"></div></div>
<script>const sc=document.querySelector('.scroller'),cards=[...document.querySelectorAll('.stack-card')];sc.addEventListener('scroll',()=>{const H=sc.clientHeight,top=sc.getBoundingClientRect().top;cards.forEach((c,i)=>{let d=0;for(let j=i+1;j<cards.length;j++){const r=cards[j].getBoundingClientRect().top-top,st=parseFloat(getComputedStyle(cards[j]).top);d+=Math.min(1,Math.max(0,(H-r)/(H-st)));}c.style.transform=d>0.001?`scale(${1-Math.min(d,4)*.035})`:'';});},{passive:true});</script>
```

### Carta

A frente da carta de um arcano, em 70 × 120 mm (proporção de tarô): a mesma peça na impressão, nas cartas que sobem e no topo.

- Anatomia: o conceito corre como borda em volta da carta (sentido horário, sempre virado para fora), cantos com quadradinhos de 1px, moldura, a imagem 3:4 emoldurada, o numeral numa aba que toca a moldura, o princípio em Bodoni grande, fio `hairline`, o nome em DM Sans espaçado e "N / VII".
- A borda repete o conceito até dar a volta e corta entre palavras, nunca deixando "o", "e" ou "de" sozinhos num canto; o corpo da borda fica entre 14,8 e 17px no viewBox 700×1200.
- Nomes longos quebram em duas linhas.
- Quem usa fornece: número, princípio, nome, conceito e a imagem.

```html
<div style="padding:24px;display:flex;gap:24px"><div style="width:300px"><!-- Carta: ver o componente Carta (SVG 700×1200) --></div><div style="width:300px"><!-- Carta: ver o componente Carta (SVG 700×1200) --></div></div>
```

### CardDialog

O texto completo de uma carta (conceito, descrição, compromisso e pergunta futurante) abre numa janela (`<dialog>`) por cima da página. Assim a página fica curta e o texto continua acessível.

- Fundo da janela em `paper`; o fundo atrás em `blue` a 86%.
- O princípio em Bodoni grande, o nome em itálico, o conceito em itálico; descrição e compromisso em Newsreader.
- A pergunta futurante fecha a janela num bloco `blue` de ponta a ponta.
- Abre por "Ler a carta inteira" e por "Tire uma carta" (ao acaso). Fecha pelo botão, pelo Esc ou clicando fora.

```html
<div style="background:rgba(27,38,79,.86);padding:24px"><dialog class="carta" open style="position:static;margin:0 auto">
  <div class="carta-in"><div class="carta-top"><span class="label">Carta I / VII</span><button type="button" class="menu-botao"><span class="tracos fechar" aria-hidden="true"><i></i><i></i></span><span>fechar</span></button></div>
  <div class="carta-grid"><div class="carta-head"><h3>Agência Futurante</h3><p class="sc-name">One Day, Tomorrow</p><span class="label">Conceito</span><p class="concept">O presente é uma produção contínua de futuros.</p></div>
  <div class="carta-body"><span class="label">Descrição</span><p>Reconhecer que tudo que existe está em transformação e que, por meio de nossas ações e relações, participamos da produção das condições de existência que virão.</p><span class="label">Compromisso</span><p>Não tratar o futuro como algo que simplesmente acontecerá conosco, nem confundir agência com capacidade de controlar o que virá.</p></div></div></div>
  <div class="carta-q"><span class="label">Pergunta futurante</span><p>Que futuro estamos fazendo existir com aquilo que fazemos hoje?</p></div>
</dialog></div>
```

### Folders

Parte 2 da página: os blocos de informação de suporte empilhados como pastas de arquivo. Cada pasta é um `<details>`: fechada mostra só a faixa colorida com o título; aberta, o conteúdo em `paper`.

- Cada pasta sobe `folder-overlap` sobre a anterior; a aba (`folder-tab` de altura, canto cortado em diagonal) fica numerada e escalonada para a direita (16% por pasta, até 200px).
- Cores em sequência: `red`, `blue`, `white`, `red`, `blue`. O texto da faixa vai em `on-color`; o conteúdo aberto volta para `ink` sobre `paper`.
- Ao passar o mouse, a pasta fechada levanta 14px; ao abrir, o conteúdo desce com um leve desdobrar; o "+" vira "×".
- Ordem padrão no EF: Outra coisa é possível · Uma Esperança Acionável · Por que futurante? · O Neomaqueerismo · Tríade de livros referência.
- Dentro das pastas valem os blocos de apoio da página: o cartaz azul da citação com o horizonte que anda, o espécime futur*ista*/futur*ante*, a matriz NEO·MA·QUEER·ISMO e o fechamento vermelho.

```html
<section class="folders"><div class="wrap folders-head"><span class="label">Para ir mais fundo</span><span class="label">05 pastas</span></div><details class="folder red" id="f1" style="--i:0"><summary><span class="tab"><span>01</span></span><span class="f-band"><h2>Outra coisa é <i>possível</i></h2><span class="mark" aria-hidden="true"><i>+</i></span></span></summary><div class="fold-body f-body wrap"><div class="fold-grid"><span class="label">Rótulo pendurado</span><div class="text"><p class="lede">A frase que abre o bloco.</p><p>O texto de apoio, em Newsreader, até 64 caracteres por linha.</p></div></div></div></details><details class="folder blue" id="f2" style="--i:1"><summary><span class="tab"><span>02</span></span><span class="f-band"><h2>Uma Esperança <i>Acionável</i></h2><span class="mark" aria-hidden="true"><i>+</i></span></span></summary><div class="fold-body f-body wrap"><div class="fold-grid"><span class="label">Rótulo pendurado</span><div class="text"><p class="lede">A frase que abre o bloco.</p><p>O texto de apoio, em Newsreader, até 64 caracteres por linha.</p></div></div></div></details><details class="folder white" id="f3" style="--i:2"><summary><span class="tab"><span>03</span></span><span class="f-band"><h2>Por que <i>Futurante?</i></h2><span class="mark" aria-hidden="true"><i>+</i></span></span></summary><div class="fold-body f-body wrap"><div class="fold-grid"><span class="label">Rótulo pendurado</span><div class="text"><p class="lede">A frase que abre o bloco.</p><p>O texto de apoio, em Newsreader, até 64 caracteres por linha.</p></div></div></div></details><details class="folder red" id="f4" style="--i:3"><summary><span class="tab"><span>04</span></span><span class="f-band"><h2>O <i>Neomaqueerismo</i></h2><span class="mark" aria-hidden="true"><i>+</i></span></span></summary><div class="fold-body f-body wrap"><div class="fold-grid"><span class="label">Rótulo pendurado</span><div class="text"><p class="lede">A frase que abre o bloco.</p><p>O texto de apoio, em Newsreader, até 64 caracteres por linha.</p></div></div></div></details><details class="folder blue" id="f5" style="--i:4" open><summary><span class="tab"><span>05</span></span><span class="f-band"><h2>Tríade de <i>livros</i> referência</h2><span class="mark" aria-hidden="true"><i>+</i></span></span></summary><div class="fold-body f-body wrap"><div class="fold-grid"><span class="label">Rótulo pendurado</span><div class="text"><p class="lede">A frase que abre o bloco.</p><p>O texto de apoio, em Newsreader, até 64 caracteres por linha.</p></div></div></div></details></section>
```

### DrawBlock

O fechamento da página, num bloco `red` de ponta a ponta: "Tire uma *carta*" em tamanho de cartaz, com a seta aberta.

- O clique abre uma carta inteira ao acaso (CardDialog).
- Ao passar o mouse, a palavra em itálico ganha sublinhado de 1px e a seta anda 12px.

```html
<section class="draw red wrap" style="padding-block:72px"><span class="label">Uma carta ao acaso, entre as sete</span><button type="button" id="draw" style="font-size:clamp(3rem,10vw,8rem)">Tire uma <i>carta</i><svg viewBox="0 0 60 30" aria-hidden="true"><path d="M0 15H56M44 3L56 15L44 27"/></svg></button></section>
```

### FooterEF

O rodapé da página EF, em `blue`: "gira. · laborateliê" à esquerda e, à direita, a linha da versão e os créditos de cada imagem das cartas.

```html
<footer class="blue wrap"><span class="label">gira. · laborateliê</span><div><p>Ética Futurante 1.0 · Hope Culture · Imaginação Futurante. Material aberto e em construção.</p><p>Imagens das cartas: créditos de cada imagem, separados por " · ".</p></div></footer>
```


### A carta (SVG)

```html
<svg class="tarot" viewBox="0 0 700 1200" role="img" aria-label="Carta I: Agência Futurante, ONE DAY, TOMORROW">
<defs><path id="t1-0" d="M76 54 H624"/><path id="t1-1" d="M646 76 V1124"/><path id="t1-2" d="M624 1146 H76"/><path id="t1-3" d="M54 1124 V76"/><clipPath id="t1-p"><rect x="118" y="148" width="464" height="619"/></clipPath></defs>
<rect class="tbg" width="700" height="1200"/><text class="tb" style="font-size:16.4px"><textPath href="#t1-0" textLength="548" lengthAdjust="spacing">O presente é uma produção contínua de futuros.</textPath></text><text class="tb" style="font-size:16.4px"><textPath href="#t1-1" textLength="1048" lengthAdjust="spacing">O presente é uma produção contínua de futuros. · O presente é uma produção contínua de futuros.</textPath></text><text class="tb" style="font-size:16.4px"><textPath href="#t1-2" textLength="548" lengthAdjust="spacing">O presente é uma produção contínua de futuros.</textPath></text><text class="tb" style="font-size:16.4px"><textPath href="#t1-3" textLength="1048" lengthAdjust="spacing">O presente é uma produção contínua de futuros. · O presente é uma produção contínua de futuros.</textPath></text>
<rect class="tl" x="42" y="42" width="12" height="12"/><rect class="tl" x="646" y="42" width="12" height="12"/><rect class="tl" x="646" y="1146" width="12" height="12"/><rect class="tl" x="42" y="1146" width="12" height="12"/>
<rect class="tl" x="76" y="76" width="548" height="1048"/>
<rect x="118" y="148" width="464" height="619" fill="#e2d6c0"/><text x="350" y="470" text-anchor="middle" font-family="DM Sans, Arial" font-size="18" letter-spacing="3" fill="#5f5b52">IMAGEM 01.JPG</text>
<rect class="tl" x="118" y="148" width="464" height="619"/>
<rect class="ttab" x="304" y="76" width="92" height="72"/><text class="tnum" x="350" y="129" text-anchor="middle">I</text>
<text class="tp"><tspan x="114" y="870">Agência</tspan><tspan x="114" y="946">Futurante</tspan></text>
<line class="th" x1="118" y1="1002" x2="582" y2="1002"/>
<text class="tn"><tspan x="118" y="1050">ONE DAY, TOMORROW</tspan></text><text class="tm" x="582" y="1050" text-anchor="end">I / VII</text>
</svg>
```
