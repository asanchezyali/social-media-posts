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
| Chrome | footer: series tag (left) + hand-drawn pen arrow (right); `@handle` watermark (top-right). No progress dots. |

## Per-series palettes

The base template keeps the cream/teal/terracotta identity. A **module** overrides
the four semantic colours (`eqink`, `accent`, `hltopic`, `mauve`) in a small file
`\input` **after** `Headers.tex`. Each **module has its own folder** with a
`palette.tex`: `AlgebraLineal/palette.tex` (forest green),
`GeometriaAnalitica/palette.tex` (indigo/violet) and
`AlgebraLinealPython/palette.tex` (Python blue — same LA topics, developed with
NumPy code cards), each plus one subfolder per post. Copy a palette to theme a
new module; keep paper, grid and general `ink` untouched.

## Requirements & compile

Needs **XeLaTeX** (`fontspec`) — not pdfLaTeX. Run twice (safe for overlays).

```bash
cd MatematicasParaML/AlgebraLineal/Matrices
xelatex -interaction=nonstopmode Matrices.tex   # pass 1
xelatex -interaction=nonstopmode Matrices.tex   # pass 2
pdfinfo Matrices.pdf | grep Pages               # (settotalslides is now vestigial)
```

## Structure

The series **Matemáticas para ML** is split into **modules**, each in its own
folder with its own `palette.tex`; every module holds one subfolder per post:

```
Instagram/
├── Headers/Headers.tex          # shared template: palette, fonts, layout, commands
├── Headers/veil.png             # cream alpha-PNG veil for the cover (required)
├── fonts/                       # vendored Playfair Display .otf
└── MatematicasParaML/                    # the SERIES
    ├── AlgebraLineal/                     # module 1 — forest-green palette (book §2)
    │   ├── palette.tex                    #   forest green
    │   ├── SistemasLineales/  … #1        #   19 posts, §2.1–§2.8:
    │   │   ├── SistemasLineales.tex       #     Sistemas, Matrices, InversaTranspuesta,
    │   │   ├── caption.md                 #     MultiplicacionEscalar, SolucionParticularGeneral,
    │   │   └── assets/cover.jpg           #     EliminacionGauss, TrucoMenosUno, CalcularInversa,
    │   ├── Matrices/ … EspaciosAfines/    #     AlgoritmosSolucion, EspaciosVectoriales, Subespacios,
    │   │                                  #     IndependenciaLineal, BaseYDimension, Rango,
    │   │                                  #     AplicacionesLineales, MatrizTransformacion,
    │   │                                  #     CambioDeBase, ImagenNucleo, EspaciosAfines (#19)
    ├── GeometriaAnalitica/                # module 2 — indigo/violet palette (book §3)
    │   ├── palette.tex                    #   indigo / violet
    │   ├── Normas/  … #1                  #   §3.1: norm axioms, ℓ1/ℓ2, unit ball (rombo vs círculo)
    │   │   ├── Normas.tex
    │   │   ├── caption.md
    │   │   └── assets/cover.jpg
    │   ├── ProductosInternos/ … #2        #   §3.2: dot/inner product, SPD matrix, ellipse vs hyperbola
    │   │   └── ProductosInternos.tex + caption.md + assets/cover.jpg
    │   ├── LongitudesAngulos/ … #3         #   §3.3: induced norm, Cauchy–Schwarz, distance, angle cos ω, orthogonality
    │   ├── BaseOrtonormal/ … #4            #   §3.5: orthonormal basis, coords via inner products, Gram–Schmidt
    │   ├── ComplementoOrtogonal/ … #5      #   §3.6: U⊥, V = U ⊕ U⊥, normal vector
    │   ├── ProductoInternoFunciones/ … #6  #   §3.7: functions as vectors, ∫uv, orthogonal sin/cos, Fourier
    │   ├── ProyeccionesOrtogonales/ … #7   #   §3.8: projection onto line/subspace, projection matrix, PCA/least-squares
    │   └── Rotaciones/ … #8                #   §3.9: rotation matrix R(θ), RᵀR=I, preserves length/angle (closes §3)
    │       (each: <Post>.tex + caption.md + assets/cover.jpg)
    └── AlgebraLinealPython/               # module 3 — Python-blue palette (LA topics via NumPy)
        ├── palette.tex                    #   Python blue (+ gold reserved for code strings)
        └── SistemasLineales/ … #1         #   Ax=b with np.linalg.solve: setup, verify (A@x), rank, LAPACK/LU
            (code cards via \begin{pycode}…\end{pycode} + \begin{pyout}…\end{pyout})
```

`Headers.tex` resolves the shared fonts and `veil.png` via `\yalixroot` — the
relative path from the post back to `Instagram/`. A post declares it before
loading the template, so it works at any depth: **`../../../`** for a module post
(`MatematicasParaML/<Module>/<Post>/`). Each post also does
`\input{../palette.tex}` to pull its **module** palette (one level up).

## Authoring

```latex
\def\yalixroot{../../../}\input{\yalixroot Headers/Headers.tex}
\input{../palette.tex}                      % series palette (one level up)
\settotalslides{10}                        % = real page count
\setwatermark{@asanchezyali}
\setseriestag{Matemáticas para ML · \#2}   % series tag (footer-left) — carries the part number

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
| `\setseriestag{...}` / `\setwatermark{...}` | Footer series tag / top-right handle |
| `\polaroid[angle]{file}{width}` | Framed tilted photo (optional) |

**Notes on layout:** text is left-aligned and flows (no manual `\\`); equations
stay centred. Wide equations are split into two lines by hand so they keep the
same size (don't rely on shrinking; `\eqfit` is only for big matrices). Dense
slides are near the 144 mm height limit — keep sizes uniform and `\eq` spacing
minimal so nothing overflows to an extra page. Graphs are native **pgfplots** in
the brand colours. See `SistemasLineales/SistemasLineales.tex` for the full
pattern.
