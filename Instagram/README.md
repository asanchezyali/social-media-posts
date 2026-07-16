# yalix — carousel template

The **yalix** brand style for technical carousels: a grid-paper "study notes"
(*apuntes*) look designed for **Instagram** (3:4 portrait, 108×144 mm — matches
the 2026 profile-grid crop). The
content **flows like a small article** — several topics per slide, auto-paginated
— with left-aligned handwritten text (like real maths notes), centred equations,
a warm cream palette, and a full-bleed photo cover.

Reference deck: `SistemasLineales/` — "Sistemas de ecuaciones lineales", Parte 1
of the series *Matemáticas para Machine Learning*.

## Identity

**Only two typefaces:** Playfair Display (titles) + SignPainter (brush
handwriting). Maths uses the standard Latin Modern font (clean primes /
derivatives), coloured — it reads as neutral notation, not a third typeface.
SignPainter is a **macOS system font** and has no bold/italic (a cosmetic
`SignPainter/b/n undefined` warning is harmless).

| Element | Choice |
|---|---|
| Canvas | light warm cream `#F9F5EB` + soft grid |
| General text | near-black `#2B2723` (`ink` — titles + handwriting) |
| Equations | teal-green `#1C6B5B` (`eqink`) |
| Highlight | vivid terracotta `#DB5A1E` (`accent`) + hand-drawn double underline (`\hl`) |
| Section titles | handwriting + a highlighter swipe (`hltopic`) |
| Muted chrome | sage `#8A9A7E` (`mauve` — dots, axes, tags) |
| Titles | **Playfair Display** (vendored in `fonts/`) |
| Handwriting | **SignPainter** (macOS system) |
| Composition | text left-aligned; equations centred |
| Chrome | progress dots + hand-drawn pen arrow; `@handle` watermark (top-right); series tag (top-left) |

## Per-series palettes

The base template keeps the cream/teal/terracotta identity. A **series** overrides
the four semantic colours (`eqink`, `accent`, `hltopic`, `mauve`) in a small file
`\input` **after** `Headers.tex`. Each **series has its own folder** with a
`palette.tex` (e.g. `MatematicasParaML/palette.tex`, forest green) plus one
subfolder per post. Copy the palette to theme a new series; keep paper, grid and
general `ink` untouched.

## Requirements & compile

Needs **XeLaTeX** (`fontspec`) — not pdfLaTeX. Run twice (dots + page counter).

```bash
cd MatematicasParaML/Matrices
xelatex -interaction=nonstopmode Matrices.tex   # pass 1
xelatex -interaction=nonstopmode Matrices.tex   # pass 2
pdfinfo Matrices.pdf | grep Pages               # confirm \settotalslides
```

## Structure

Posts are grouped **by series**, two levels below `Instagram/`:

```
Instagram/
├── Headers/Headers.tex          # shared template: palette, fonts, layout, commands
├── Headers/veil.png             # cream alpha-PNG veil for the cover (required)
├── fonts/                       # vendored Playfair Display .otf
├── MatematicasParaML/           # a SERIES
│   ├── palette.tex              # this series' colour override
│   ├── SistemasLineales/        # post #1
│   │   ├── SistemasLineales.tex
│   │   └── assets/cover.jpg
│   ├── Matrices/                # post #2 (colourful TikZ illustrations)
│   │   ├── Matrices.tex
│   │   └── assets/cover.jpg
│   ├── InversaTranspuesta/      # post #3 (inverse, determinant, transpose, symmetric)
│   │   ├── InversaTranspuesta.tex
│   │   └── assets/cover.jpg
│   ├── MultiplicacionEscalar/   # post #4 (scalar multiplication)
│   │   ├── MultiplicacionEscalar.tex
│   │   └── assets/cover.jpg
│   ├── SolucionParticularGeneral/  # post #5 (particular & general solution, affine subspace)
│   │   ├── SolucionParticularGeneral.tex
│   │   └── assets/cover.jpg
│   ├── EliminacionGauss/        # post #6 (elementary transforms, row-echelon, RREF)
│   │   ├── EliminacionGauss.tex
│   │   └── assets/cover.jpg
│   ├── TrucoMenosUno/           # post #7 (Minus-1 trick: kernel basis from RREF)
│   │   ├── TrucoMenosUno.tex
│   │   └── assets/cover.jpg
│   ├── CalcularInversa/         # post #8 (inverse via Gauss-Jordan: [A|I]→[I|A⁻¹])
│   │   ├── CalcularInversa.tex
│   │   └── assets/cover.jpg
│   ├── AlgoritmosSolucion/      # post #9 (methods map: inverse, least-squares/pseudo-inverse, gaussian elim., iterative)
│   │   ├── AlgoritmosSolucion.tex
│   │   └── assets/cover.jpg
│   ├── EspaciosVectoriales/     # post #10 (§2.4: groups, Abelian, GL(n,R), vector spaces, column/row vectors)
│   │   ├── EspaciosVectoriales.tex
│   │   └── assets/cover.jpg
│   └── Subespacios/             # post #11 (§2.4.3: vector subspaces, 3 conditions, R^2 figure, homogeneous systems)
│       ├── Subespacios.tex
│       └── assets/cover.jpg
└── MachineLearningMathematics/  # earlier standalone demo (1 level deep)
```

`Headers.tex` resolves the shared fonts and `veil.png` via `\yalixroot` — the
relative path from the post back to `Instagram/`. A post declares it before
loading the template, so it works at any depth (`../../` for series posts, `../`
for the old 1-level demo).

## Authoring

```latex
\def\yalixroot{../../}\input{\yalixroot Headers/Headers.tex}
\input{../palette.tex}                      % series palette (one level up)
\settotalslides{10}                        % = real page count
\setwatermark{@asanchezyali}
\setseriestag{Matemáticas para ML · \#2}   % series tag (top-left) — carries the part number

\begin{document}
\begin{slidec}                                  % photo cover (vertically centred)
  \coverphoto{assets/cover.jpg}                 % use a NEW photo per post
  \raggedright
  \serlead{Serie · Matemáticas para Machine Learning}
  \sertitle{\fontsize{40}{43}\selectfont Matrices}
  \hand{Cómo \hl{organizamos} y transformamos datos}
\end{slidec}
\clearpage

% article flows and paginates itself
\topic{¿Qué son?}
\hand{Texto que fluye, alineado a la izquierda, como apuntes reales.}
\defn{Una \uhand{solución} es una $n$-tupla que satisface todas las ecuaciones.}
\eqx{a_{11}x_1 + \cdots + a_{1n}x_n = b_1}
\obs{En todo sistema lineal ocurre siempre uno de tres casos: ...}
\keyeq{A\,\mathbf{x} = \mathbf{b}}
\end{document}
```

### Commands

| Command | Purpose |
|---|---|
| `\begin{slidec}...\end{slidec}` | Vertically-centred slide (cover / closing) |
| `\coverphoto{file}` | Full-bleed cover photo + cream veil (single-pass safe; veil baked into `Headers/veil.png`) |
| `\sertitle{...}` | Big Playfair display title |
| `\serlead{...}` / `\hand{...}` | SignPainter body (left-aligned) |
| `\topic{...}` | Section heading: handwriting + highlighter swipe (auto-numbered) |
| `\defn{sentence}` | "Def." + full sentence; underline the term with `\uhand{...}` |
| `\obs{...}` / `\eg{...}` | "Obs." remark / "Ej." example |
| `\hl{...}` / `\hlm{...}` | Highlight (text: accent + double underline / maths: colour) |
| `\eq{...}` / `\eqx{...}` | Centred equation, uniform size (break wide ones by hand) |
| `\eqfit{...}` | Big block (matrix) scaled to fit the width |
| `\keyeq{...}` | Key result boxed by hand-drawn pen strokes |
| `\setseriestag{...}` / `\setwatermark{...}` | Top-left series tag / top-right handle |
| `\polaroid[angle]{file}{width}` | Framed tilted photo (optional) |

**Notes on layout:** text is left-aligned and flows (no manual `\\`); equations
stay centred. Wide equations are split into two lines by hand so they keep the
same size (don't rely on shrinking; `\eqfit` is only for big matrices). Dense
slides are near the 144 mm height limit — keep sizes uniform and `\eq` spacing
minimal so nothing overflows to an extra page. Graphs are native **pgfplots** in
the brand colours. See `SistemasLineales/SistemasLineales.tex` for the full
pattern.
