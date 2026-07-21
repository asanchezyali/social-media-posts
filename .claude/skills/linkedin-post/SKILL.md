---
name: linkedin-post
description: >-
  Write a technical LinkedIn post as a polished multi-page ARTICLE (dark "code-editor" theme, XeLaTeX).
  Use whenever the user asks to create, draft, port, or restyle a LinkedIn post, or add a new topic.
  The template is LinkedIn/Headers/Article.tex; reference post: LinkedIn/PythonDecorators/. Follow the
  five-step workflow: (1) write, (2) verify the claims/APIs against current sources online, (3) keep
  concepts current to 2025-2026, (4) always add a references section with real links, (5) run the
  humanize-writing-en pass on the prose. NOTE: for the cream Instagram "study notes" (yalix) carousels
  use the instagram-carousel skill instead; the legacy dense pdfLaTeX posts under Python/, JavaScript/,
  ArtificialIntelligence/ are kept only for maintaining what's already published.
---

# LinkedIn technical article (dark code-editor theme)

A LinkedIn post here is a **multi-page article** — a modern dev-blog post rendered
as a PDF "document" people scroll: dark navy canvas, Inter + JetBrains Mono, a
faint line-number gutter, numbered sections, mac-window code cards, coloured
callouts, a magazine-style photo cover, and an author bar on every page. It's for
**long-form depth**, not a swipe deck.

- **Template:** `LinkedIn/Headers/Article.tex` (shared; `\input` it, don't fork).
- **Reference post:** `LinkedIn/PythonDecorators/` — read it before writing a new one.
- Instagram cream "study notes" carousels → use the **`instagram-carousel`** skill.

## Authoring workflow — do all five, every post

1. **Write.** A real point of view, a concrete detail in every section, working
   code. Shape: photo title page → numbered sections (each = concept + code card +
   callout) → a "Common mistakes" section → a "Read more" section (references) +
   the closing card. Keep it to **≤ 8 pages** — the `.tex` is the concise version;
   push extra depth into the post's `README.md`.
2. **Verify against current sources.** Before finishing, confirm the claims, API
   names, and behavior against the **official docs / primary sources** online
   (WebSearch / WebFetch). Never ship a gotcha, a stdlib name, or a version detail
   you didn't check. Fix anything the sources contradict.
3. **Keep concepts current to 2025-2026.** Use current best practice and current
   library/language versions (e.g. today's Python stdlib, current framework
   idioms). Call out anything that changed recently or is newly recommended.
4. **Always add references with links.** A short "Read more" section near the end
   with 2-4 **primary** links — official docs, PEPs/specs, the source repo. Real
   URLs only; never invent a link, a stat, or a citation.
5. **Run the humanize-writing-en pass.** The article is English prose the user
   publishes as their own — invoke the **`humanize-writing-en`** skill on it. Kill
   the AI tells: thin **em-dashes** to a handful (they pile up fastest here), drop
   the "delve/leverage/robust" vocabulary and summary closers, keep it concrete
   and staked.

## Engine & fonts

- **XeLaTeX (fontspec), run twice.** NOT pdfLaTeX.
- Vendored in `LinkedIn/fonts/`: **Inter** (Inter Display Bold for the title +
  headings) + **JetBrains Mono** (code + labels). Body is Inter Regular.

## Structure & commands

```latex
\def\lnkroot{../}\input{\lnkroot Headers/Article.tex}
\setheader{Python}{Decorators}         % per-page header: [PYTHON] blue pill + green TOPIC
\begin{document}

\coverphoto{assets/cover.jpg}          % full-bleed photo + baked dark overlay (title page)
\arttitlepage{Python}{Decorators, from\\ the ground up}%
  {The one-liner that adds behavior to any function — and the \tb{functools}
   details nobody explains.}            % tag, title (\\ = break), subtitle. NO QR/kicker here.

\section{What a decorator really is}
A decorator takes a function and returns a new one ... The \code{@} is sugar.

\begin{pycard}{pattern.py}             % mac-window Python card (\sqlcard for SQL)
def log(fn):
    def wrapper(*a, **k):
        return fn(*a, **k)
    return wrapper
\end{pycard}

\begin{callout}[dotamber]{GOTCHA}      % blue=WHY IT MATTERS (default), amber=GOTCHA, green=PRO TIP
Add \code{@wraps} to \tb{every} decorator ...
\end{callout}

\subsection{A finer point}             % optional H3
\begin{itemize}\item ... \end{itemize} % blue ▸ bullets

\section{Read more}
\begin{itemize}
  \item Python docs — functools: \href{https://docs.python.org/3/library/functools.html}{docs.python.org/...}
\end{itemize}
\artclosing{https://github.com/asanchezyali/social-media-posts/tree/main/LinkedIn/PythonDecorators}
\end{document}
```

| Command | Purpose |
|---|---|
| `\setheader{Lang}{Topic}` | Per-page header: blue **[LANG]** pill + divider + **green TOPIC**. Footer author bar + page number is automatic. |
| `\coverphoto{img}` | Full-bleed title-page photo + baked dark overlay (`Headers/overlay.png`). Cover from **`Images/`** (dark tech backdrops), NOT `Photos/`. |
| `\arttitlepage{tag}{Title}{Subtitle}` | Magazine title page (tag + big Inter-Black title + subtitle + author). No QR, no kicker on it. |
| `\section{}` / `\subsection{}` | Numbered heading (blue number + thin rule) / blue H3. |
| `\begin{pycard}{f.py}` / `\begin{sqlcard}{f.sql}` | mac-window code card. **No `_` in the filename arg** (use `args.py`); inside the body `_ % * @` are fine. |
| `\begin{callout}[colour]{LABEL}` | Value box, coloured left border. `dotamber`=GOTCHA, default blue=WHY IT MATTERS, `dotgreen`=PRO TIP — the senior insight. |
| `\code{}` / `\hb{}` / `\tb{}` | inline code chip / blue accent word / semibold-bright emphasis. **Escape `_` and `%`** inside `\code{}` and prose. |
| `\artclosing{url}` | Closing cross-promo card (heading + description left, QR right). |

## Style rules (baked in — keep them)

- **Ragged-right** body + callouts (the template sets `\RaggedRight` +
  `\emergencystretch`). Justifying this narrow measure with inline chips makes
  ugly rivers — don't switch back to justified.
- **≤ 8 pages.** If it runs over, move an example to `codes/` + the `README.md`
  and reference it, rather than padding the PDF. Recompile and check the count.
- Header topic is **green**; the title page has **no QR and no kicker**.
- The post folder also holds **`codes/NN_name.py`** (runnable, dependency-free —
  actually run them), a **`README.md`** deep-dive (GitHub renders it as the folder
  landing page, which is what `\artclosing`'s QR points to), a `caption.md` (the
  LinkedIn caption), and `assets/cover.jpg`.

## Compile & preview

```bash
cd LinkedIn/<Post>
xelatex -interaction=nonstopmode <Post>.tex   # twice
pdfinfo <Post>.pdf | grep Pages               # confirm ≤ 8
pdftoppm -png -r 110 <Post>.pdf preview        # inspect
```

Always render and eyeball: ragged-right rhythm, code-card fit, callouts not
orphaned, header/footer, and the page count.

---

## Legacy dense articles (Python/, JavaScript/, ArtificialIntelligence/)

The older multi-page `article` posts (pdfLaTeX, Source Sans Pro, `macterminal`,
`Python/Headers/Headers.tex`). **Kept only to maintain what's already published** —
write every NEW post in the article format above. They're also useful as source
material to port from (but re-verify against current docs per step 2).
