---
name: instagram-carousel
description: Create yalix "study-notes" math/tech carousels for Instagram (3:4 portrait, cream grid-paper, XeLaTeX + SignPainter). Use when the user asks to create, draft, restyle, or extend an Instagram post/carousel in this repo — a new topic, a new part of a series, a new palette, or edits to the "apuntes" slides. The template lives in Instagram/Headers/Headers.tex. NOTE: for LinkedIn dark-theme code posts, use the linkedin-post skill instead.
---

# yalix carousel — study-notes math posts (Instagram)

This skill builds **yalix**-brand carousels for **Instagram**: a student's
**lecture-notes (apuntes)** look on cream grid paper, written in **Spanish**,
3:4 portrait (1080×1440). Content **flows like a small article** — several topics per slide,
auto-paginated — not one topic per slide. The reference deck is
`Instagram/MatematicasParaML/` — the series *Matemáticas para Machine Learning*,
with posts `SistemasLineales/` (#1), `Matrices/` (#2), `InversaTranspuesta/` (#3)
`MultiplicacionEscalar/` (#4), `SolucionParticularGeneral/` (#5),
`EliminacionGauss/` (#6), `TrucoMenosUno/` (#7), `CalcularInversa/` (#8) and
`AlgoritmosSolucion/` (#9), `EspaciosVectoriales/` (#10), `Subespacios/` (#11), `IndependenciaLineal/` (#12), `BaseYDimension/` (#13), `Rango/` (#14), `AplicacionesLineales/` (#15), `MatrizTransformacion/` (#16), `CambioDeBase/` (#17), `ImagenNucleo/` (#18) and `EspaciosAfines/` (#19, finale of the LA chapter). A
second module, `GeometriaAnalitica/` (indigo/violet palette), covers book §3:
`Normas/` (#1), `ProductosInternos/` (#2), `LongitudesAngulos/` (#3), `BaseOrtonormal/` (#4),
`ComplementoOrtogonal/` (#5), `ProductoInternoFunciones/` (#6), `ProyeccionesOrtogonales/` (#7),
`Rotaciones/` (#8) — the whole §3 chapter. A third module,
`AlgebraLinealPython/` (Python-blue palette), retells the Álgebra Lineal topics
**developed with NumPy** — same apuntes style, plus brand-styled code cards
(`pycode`/`pyout`); tag `\setseriestag{Álgebra lineal · Python \#N}`. Its pilot is
`SistemasLineales/` (#1): `Ax=b` via `np.linalg.solve`, verify with `A @ x`,
classify with `matrix_rank`, LAPACK/LU note. The tag names the module:
`\setseriestag{Álgebra lineal · ML \#N}` or `\setseriestag{Geometría analítica · ML \#N}`
(numbering restarts per module). The goal is a genuinely useful **study
resource** — lean into many colourful, didactic illustrations, and write like an
advanced student (precise terms: núcleo/kernel, subespacio afín, definida positiva).

> This is a **different system** from the LinkedIn dark-theme code posts
> (Python/JS/AI). For those, use the **`linkedin-post`** skill instead.

## Engine & fonts (non-negotiable)

- **Compile with XeLaTeX, run TWICE** (`fontspec` + a page-counter/overlays need
  two passes). NOT pdfLaTeX.
- **Exactly two typefaces:** Playfair Display (display titles, vendored in
  `Instagram/fonts/`) + **SignPainter** (brush handwriting body, a **macOS system
  font** — this template assumes macOS). Math stays in default **Latin Modern**
  (legible primes/derivatives), coloured — it reads as neutral notation, not a
  third font. Never set math in Playfair.
- SignPainter has **no bold and no italic** → don't use `\textbf`/`\emph` inside
  `\hand{}`. A cosmetic `Font shape TU/SignPainter/b/n undefined` warning is
  harmless; ignore it.
- Unicode Spanish (á é í ó ú ñ ¿ ¡ —) renders fine in SignPainter. Use the real
  `—` em-dash character, never `---` (SignPainter shows three hyphens).

## Three-colour rule

Every colour maps to one **semantic role** — never decorate freely:

| Role | Command context | Brand default |
|---|---|---|
| General text (titles + body) | `ink` / `handInk` | graphite `#2B2723` |
| **Equations** (all math) | `eqink` | teal-green `#1C6B5B` |
| **Highlight** (`\hl`, `Def.`/`Obs.` labels, `\keyeq` box) | `accent` | terracotta `#DB5A1E` |
| Muted chrome (dots, axes, tags) | `mauve` | sage `#8A9A7E` |
| Section-title highlighter swipe | `hltopic` | green `#96C855` |

Paper is always cream `#F9F5EB` with a soft grid — the yalix signature, kept
across all palettes.

## Per-series palettes

Each **module lives in its own folder** (`Instagram/MatematicasParaML/<Module>/`)
holding a `palette.tex` plus one subfolder per post. The palette overrides the
four semantic colours in a file that is `\input` **after** `Headers.tex`. Three in
the repo: `AlgebraLineal/palette.tex` (forest green),
`GeometriaAnalitica/palette.tex` (indigo/violet — `accent` #6A4FC0, `eqink`
#3A4A9E, `hltopic` #C4BAEA, `mauve` #7C82A6) and `AlgebraLinealPython/palette.tex`
(Python blue — `accent` #1E6FB0, `eqink` #21486E, `hltopic` #BED4E9, `mauve`
#7C8BA3). One file recolours a whole module:

```latex
% forest green (deep pine + leaf green). Keep highlight dark enough to read on
% cream — a bright/light green (e.g. #4E9D2F) has poor contrast; this is darker.
\definecolor{eqink}{RGB}{34, 74, 26}      % equations  (deep pine green)
\definecolor{accent}{RGB}{56, 132, 34}    % highlight   (rich leaf green)
\definecolor{hltopic}{RGB}{200, 227, 175} % title highlighter (pale green)
\definecolor{mauve}{RGB}{149, 167, 132}   % dots / axes / tags (muted sage)
```

To create a new series palette: copy that file, pick a **theme-appropriate,
mostly monochromatic** set (equations = the deep anchor colour; highlight = a
clearly distinct sibling that pops on cream; highlighter = a pale tint of the
theme; mauve = a desaturated grey of the theme). Keep paper/grid/ink untouched.
When two plot lines use `eqink` + `accent`, verify they stay distinguishable.

## Starting a new post

The series **Matemáticas para ML** is split into **modules**; a post lives
**three levels below `Instagram/`** (`Series/Module/Post/`):

```
Instagram/
├── Headers/Headers.tex        # the shared template (don't fork; \input it)
├── Headers/veil.png           # cream alpha-PNG for the cover veil (required asset)
├── fonts/                     # vendored Playfair Display .otf
└── MatematicasParaML/         # the SERIES
    ├── AlgebraLineal/         # a MODULE (forest-green palette)
    │   ├── palette.tex        # this module's colour override
    │   ├── <Post1>/
    │   │   ├── <Post1>.tex
    │   │   ├── caption.md      # Spanish caption for publishing
    │   │   └── assets/cover.jpg   # cover photo — VARY it per post
    │   └── <Post2>/ ...
    └── GeometriaAnalitica/    # another MODULE (indigo/violet palette)
        ├── palette.tex
        └── Normas/ ...
```

**Depth-independent paths (`\yalixroot`).** `Headers.tex` finds the shared fonts
and `veil.png` relative to `\yalixroot` — the path from the post file back up to
`Instagram/`. Each post declares it before `\input`-ing the template, so a post
works at any depth. For a module post (`Series/Module/Post/`) it is `../../../`.
`\input{../palette.tex}` pulls the **module** palette (one level up).

**Cover robustness / `veil.png`.** `\coverphoto` places the photo AND its cream
veil on the page background via eso-pic (`\AtPageLowerLeft`), so the cover is
full-bleed **even on a single XeLaTeX pass**. Two gotchas are baked into the
design — don't undo them:
- Do **not** position the cover photo with a `remember picture` overlay: that
  resolves only on the 2nd pass and otherwise collapses the photo to a top band.
- Do **not** veil it with a pgf `opacity` fill inside the eso-pic background:
  pgf transparency corrupts that stream here (`unknown ExtGState`) and blanks the
  whole cover. The veil is instead a pre-baked alpha PNG, `Headers/veil.png`
  (cream `#F9F5EB` @ ~0.80), referenced as `\yalixroot Headers/veil.png`.
  A strong veil (~0.80) is deliberate: it mutes busy/dark photos so the dark
  title stays readable everywhere (0.66 left dark text over dark photo areas).
  Regenerate to change the tint/strength, e.g.
  `magick -size 8x8 xc:"rgba(249,245,235,0.80)" Headers/veil.png`.

Preamble of a post (2-level series layout):

```latex
\def\yalixroot{../../../}\input{\yalixroot Headers/Headers.tex}
\input{../palette.tex}              % this series' palette (one level up)
\settotalslides{10}                 % update to the real page count (see below)
\setwatermark{@asanchezyali}        % top-right on every slide (default already this)
\setseriestag{Álgebra lineal · ML \#2}     % footer-left tag — module + part number, on every slide
```

Numbering lives **only** in the series tag (`· #N`) — do not also write "Parte N"
in the cover/closing text (that was removed as duplicate).

`\settotalslides{N}` is optional now — the progress dots were removed, so it's a
harmless no-op (kept for backwards compatibility). The footer shows the series
tag (left) + swipe arrow (right); no dots to keep in sync.
Compile once, read the page count, set N, compile again.

## Authoring — the apuntes flow

Body text is one **flowing article** between the cover and closing. Do **not**
hand-break lines in prose; text is left-aligned and wraps. Only equations are
centred. Structure it with topic headings and note blocks:

```latex
\topic{Título de sección}          % handwritten heading + highlighter swipe (auto-numbered)
\hand{Texto que fluye, alineado a la izquierda, como apuntes reales.}
\defn{Una \uhand{solución} es una $n$-tupla que satisface todas las ecuaciones.}
\eqx{a_{11}x_1 + \cdots + a_{1n}x_n = b_1}
\obs{En todo sistema lineal ocurre siempre uno de tres casos: ...}
\keyeq{A\,\mathbf{x} = \mathbf{b}}   % hand-boxed key result
```

### Command reference

| Command | Purpose |
|---|---|
| `\begin{slide}...\end{slide}` | Interior slide, content anchored to top (rarely needed — the article flows between `\clearpage`s) |
| `\begin{slidec}...\end{slidec}` | Vertically-centred slide — use for **cover** and **closing** |
| `\coverphoto[opacity]{file}` | Full-bleed cover photo + uniform cream veil (default opacity 0.66) |
| `\sertitle{...}` | Big Playfair display title (wrap in `\fontsize{..}{..}\selectfont` to size) |
| `\serlead{...}` / `\hand{...}` | SignPainter body text, left-aligned, size 15/21 |
| `\topic[<height>]{...}` | Section heading (auto-numbered). Optional needspace (default 4 mm); set it to the topic height to keep a big figure with its text — see "Flow like a document" |
| `\defn{full sentence}` | "Def." + sentence; underline the defined term with `\uhand{...}` |
| `\obs{...}` | "Obs." remark. Write it **standalone**, not as a trailing connector |
| `\eg{...}` | "Ej." example |
| `\hl{texto}` / `\hlm{$math$}` | Highlight: accent colour + hand-drawn double underline (text) / colour only (math) |
| `\uhand{...}` | Single hand-drawn underline (used inside `\defn` for the term) |
| `\eq{...}` / `\eqx{...}` | Centred display equation, uniform size, with `\eqskip` breathing room above/below |
| `\eqfit{...}` | Wide block (big matrix) auto-scaled to the text width |
| `\keyeq{...}` | Key result boxed by four wobbly hand-drawn pen strokes |
| `\begin{pycode}…\end{pycode}` | **Python module only.** Code card: rounded pale panel, 3 dots + `python` label, Menlo mono; syntax colours are theme-driven (keywords=`accent`, comments=`mauve`, strings=`pygold`). Atomic (won't split across slides) — keep it with its heading via `\topic[<h>]{...}` |
| `\begin{pyout}…\end{pyout}` | **Python module only.** REPL result box (paper-tinted, "Out" tab, Menlo) — put the printed array / value / error here right after its `pycode` |
| `\coverphoto`, `\polaroid[angle]{file}{width}` | Photos (polaroid = framed, tilted) |
| `\penrule[width]` / `\wavyrule[width]` | Hand-drawn underline rules (legacy; prefer `\hl`/`\topic`) |

### Graphs & didactic illustrations

Draw everything **natively in TikZ/pgfplots** (vector, on-brand), not imported
images. Lean into **colourful, didactic illustrations** — they make the post.

- **Plots**: `eqink` / `accent` lines, `mauve` axes/ticks (`font=\tiny`), each
  equation label on its own `sloped` line in that line's colour, clear of the
  curve. See `MatematicasParaML/SistemasLineales/SistemasLineales.tex`
  (topic *Geometría*).
- **Matrix / grid diagrams** (anatomy of a matrix, reshape-to-vector, row×column
  product, dimension matching, identity, `AB≠BA`): a grid of cells drawn with a
  `\cell{col}{-row}{fill}{content}` helper on an `[x=6.2mm, y=6.2mm]` canvas,
  filled with soft pastels that harmonise with the series palette (pale aqua /
  warm gold / green / violet). Highlight a row/column/cell to show what an
  operation touches. Full worked set in
  `MatematicasParaML/Matrices/Matrices.tex` — copy those figures as a starting
  point. Aim for **several** illustrations per post; keep each ~40–50 mm tall so
  text + figure fit one slide.
- **Geometric effect on the unit circle**: for square-matrix transformations,
  draw the unit circle (dashed) and its image, plus a vector `v` → its image, on
  faint `mauve` axes. A scalar `λI` maps the circle to a circle of radius `λ`
  (uniform scaling); a general matrix deforms it into an **ellipse**. Great for
  building geometric intuition — see the scalar case in
  `MatematicasParaML/MultiplicacionEscalar/MultiplicacionEscalar.tex`.

## Writing conventions (learned from iteration)

- **Spanish**, warm and plain — real student notes.
- **Definitions** read as a sentence: *"Def. Una **solución** es una n-tupla…"*
  (term underlined with `\uhand`), never *"Def. término: cuerpo"*.
- **Observations** stand on their own. Avoid openers like "y…", "es una…" that
  dangle off the previous line. Prefer *"Obs. En todo sistema lineal ocurre
  siempre uno de tres casos: …"*.
- When slides are examples of cases, **frame them explicitly** ("Este sistema no
  tiene ninguna solución:", "Si ahora cambiamos la última ecuación…").
- **Cover photo must VARY** between posts — don't reuse the same image.
- If the post is part of a **series**, say so in three places: the **cover**
  (`\serlead{Serie · …}` + a highlighted "Parte N"), the persistent **footer
  series tag** (`\setseriestag`), and the **closing** CTA.
- Closing = a big **question** + Save/Follow CTA ("Guarda esto y sígueme … en
  asanchezyali.com"). **Vary the closing question across posts** — do NOT default
  to "¿Te quedó claro…?/¿Te sirvió…?" every time (passive and repetitive). Make it
  engaging: invite reflection or a comment (e.g. "¿Dónde has visto un sistema
  lineal sin darte cuenta?"), an opinion ("¿Cuál se te resiste más: X o Y?"), or a
  perspective shift ("¿Ya ves una matriz como una transformación?").
- Sprinkle a genuinely interesting fact when natural (etymology, history).

## Flow like a document (not one-topic-per-slide)

The article **flows and fills each page continuously**, like a normal LaTeX
document — a topic can start halfway down a page, and content packs tightly with
no big empty gaps. Do **not** try to make each slide a self-contained topic
(that's what left ugly bottom gaps before). `\topic` uses a tiny `needspace`
plus `\nobreak` glue so a heading welds to its first following line (never
orphaned at a page foot) while everything else fills naturally.

**Keeping a big figure with its text — `\topic[<height>]{...}`.** A topic that
ends in a large *atomic* block (a pgfplots graph or an `\eqfit` matrix that can't
be split) will otherwise tear off onto its own slide, leaving a gap. Give that
topic an explicit needspace equal to roughly its whole height so the entire block
(heading + text + figure) moves together, e.g. `\topic[74mm]{Notación compacta}`.
Tune the number (and, if it won't fit alongside the preceding page's tail, trim a
line of intro text or shrink the figure a touch) until it packs without a gap.
Plain text topics just use `\topic{...}` (4 mm default). `\eqfit` and `\keyeq`
centre themselves — `\eqfit` uses `\centerline` so it stays centred under
`\RaggedRight`.

Consequence: page count is driven by content, and denser than the old
one-per-slide layout. **Always recompile and re-check the page count.**
(Progress dots were removed, so `\settotalslides` no longer needs to match.)

## Layout discipline (avoid overflow)

Dense slides sit near the 144 mm height limit. Keep uniform sizing:

- Keep body at 13.5/16 and handwriting at 15/21 — **do not bump sizes** to fill
  space; that causes overflow to an extra page and breaks the dot count.
- Split a too-wide equation into **two lines by hand** to keep it the same size —
  don't rely on shrinking (users noticed a shrunk equation "luce diferente").
  Use `\eqfit` only for big matrices.
- `\eq`/`\eqx`/`\eqfit`/`\keyeq` add `\eqskip` (4 mm) of space above and below so
  equations never crowd the text — don't add your own `\vspace` around them. Tune
  `\eqskip` in `Headers.tex` to change equation breathing room everywhere.
- **Small figures (≈2×2/3×3 grids): let them flow** (plain `\topic{...}`) so pages
  pack full. Reserve `\topic[<height>]{...}` keep-together only for genuinely
  LARGE atomic figures (a pgfplots graph, a wide `\eqfit` matrix) that would tear
  badly — otherwise big needspace leaves half-empty pages.
- After edits, recompile and re-check the page count; update `\settotalslides`.

## Compile & preview

```bash
cd Instagram/<Series>/<Post>
xelatex -interaction=nonstopmode -halt-on-error <Post>.tex   # pass 1
xelatex -interaction=nonstopmode -halt-on-error <Post>.tex   # pass 2
pdfinfo <Post>.pdf | grep Pages          # confirm N for \settotalslides
pdftoppm -png -r 120 -f 1 -l 1 <Post>.pdf preview   # render a page to inspect
```

Always **render and visually verify** the affected pages after a change —
colour, overflow, label collisions, and the footer tag vs. top-right watermark.

## Checklist

- [ ] `\def\yalixroot{../../../}\input{\yalixroot Headers/Headers.tex}` + `\input{../palette.tex}`
- [ ] Cover: full-bleed photo (a **new** one), series lead + Parte N, subtitle
- [ ] Interior flows as an article; topics via `\topic`; only equations centred
- [ ] Definitions as sentences; observations standalone; Spanish reads naturally
- [ ] Math coloured `eqink`; highlights `accent`; no `\textbf`/`\emph` in handwriting
- [ ] Graphs are native pgfplots in brand colours, labels clear of the curves
- [ ] Series mentioned on cover + footer tag + closing
- [ ] Compiles clean with **XeLaTeX ×2**; no page overflow
