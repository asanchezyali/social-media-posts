---
name: linkedin-post
description: Generate LaTeX technical carousel/post content for LinkedIn (dark theme). Two systems — the NEW code-editor 4:5 carousel in LinkedIn/ (XeLaTeX + vendored Inter/JetBrains Mono, clean & low-density) and the legacy dense articles in Python/JavaScript/AI (pdfLaTeX). Use when the user asks to create, draft, or restyle a LinkedIn post, add a new topic, or work with the dark-theme templates. NOTE: for the cream Instagram "study notes" (yalix) carousels, use the instagram-carousel skill instead.
---

# Social Media Post Skill - LaTeX Technical Articles (LinkedIn)

This skill generates technical social media posts (designed for LinkedIn) using LaTeX with a professional dark theme. The posts are organized by programming language/topic and follow a consistent visual format.

> For the **Instagram** cream grid-paper "study notes" carousels (yalix brand,
> XeLaTeX + SignPainter), use the separate **`instagram-carousel`** skill. This
> skill is only the LinkedIn dark-theme format.

---

## TWO LinkedIn systems — pick the right one

1. **`LinkedIn/` — code-editor carousel (NEW, preferred, English).** A clean,
   low-density **4:5 carousel** (1080×1350) styled like a code editor: dark navy
   canvas, a faint line-number gutter, a top-right glow, a giant ghost slide
   number, monospace kicker comments, a blue keyword pill, big **Inter Display
   Black** headlines with one word in blue, muted leads with inline code chips, a
   mac-window **code card**, progress dots, and an author closing card. Mirrors
   the Instagram architecture: shared `LinkedIn/Headers/Headers.tex` +
   **vendored fonts** (`LinkedIn/fonts/`: Inter + JetBrains Mono) + one folder per
   post. **XeLaTeX (fontspec), run twice.** Reference deck: `LinkedIn/SQLForBeginners/`.
   The **cover is an old-LinkedIn-style title page**: full-bleed photo + dark
   overlay + topic tag + big title + subtitle + a **QR code to the source**.
   (A giant ghost slide-number was tried and **removed** at Alejandro's request —
   the `sld` `[NN]` arg is now a harmless no-op; the left line-number gutter stays.)
2. **`Python/`, `JavaScript/`, `ArtificialIntelligence/` — legacy dense articles.**
   The older multi-page `article` decks (pdfLaTeX, Source Sans Pro, `macterminal`).
   Documented in the rest of this file. Keep for maintaining old posts.

### `LinkedIn/` carousel — authoring

Paths mirror the yalix mechanism: a post declares its depth, then inputs the
shared template.

```latex
\def\lnkroot{../}\input{\lnkroot Headers/Headers.tex}
\setdeck{12}                       % total slides (for the progress dots)
\begin{document}
\begin{sld}                        % COVER — photo title page (old-LinkedIn style)
  \coverdark{assets/cover.jpg}     % full-bleed photo + dark overlay (this page)
  \kicker{\kgreen{quick guide · 10 commands}}
  \topictag{SQL}                   % compact blue topic badge
  \vskip 6mm
  \headline{\hb{SQL} explained\\ for beginners}   % \hb{} = blue word; \\ = manual break; NO trailing period
  \lead{Ten keywords that handle \tb{90\% of your day} with databases.}
\end{sld}

\begin{sld}[01]                    % SECTION ([NN] arg kept but no longer drawn)
  \kicker{\kblue{01} · read data}
  \pill{SELECT}                    % full-width blue keyword bar
  \headline{Pick \hb{which columns}\\ you want.}
  \lead{Ask for the columns you need. \chip{*} means \tb{all of them}.}
  \begin{codecard}{select.sql}
SELECT * FROM users;
  \end{codecard}
\end{sld}

\begin{sld}                        % CLOSING — author card + QR to the source
  \kicker{\kgreen{that's the 90\%}}
  \headline{You just learned the \hb{core of SQL}}
  \lead{Which one do you reach for most?}
  \vskip 3mm
  \authorcard
  \vskip 6mm
  \sourceqr{https://github.com/.../LinkedIn/SQLForBeginners}{study with me}{the full source on GitHub}
\end{sld}
\end{document}
```

**Commands:** `\kicker{...}` (mono `-- ` comment; wrap words in `\kgreen`/`\kblue`),
`\pill{KEYWORD}`, `\headline{...}` / `\headlinesm{...}` (Inter Display **Bold**, big / smaller — NOT Black; Black read as too heavy/saturated;
`\hb{}` blue word, `\\` for deliberate line breaks — short headlines MUST be broken
or they overflow), `\lead{...}` (muted 1-liner; `\tb{}` = bold white, `\chip{...}` =
inline code chip — **escape `_` and `%`** inside chips/leads), `\begin{codecard}{file.sql}…\end{codecard}`
(mac-window SQL card; atomic — won't split), `\authorcard` (photo + name + role +
site, on the closing slide), `\setdeck{N}` (dot count). **Title-page commands:**
`\coverdark{img}` (full-bleed photo + baked dark overlay for that page),
`\topictag{SQL}` (compact blue badge), `\sourceqr{url}{heading}{subtitle}` (QR with
**solid dark modules** on a white card so it scans — `\qrcode` inherits the text
colour, so it's forced dark; goes on the **closing** slide, e.g. heading "study
with me"). The `[NN]` optional arg of `sld` is retained but no longer drawn (the
giant watermark was removed). Headlines carry **no trailing period**. The code
card's `*` is raised via a listings `literate` (JetBrains Mono's asterisk sits low).

**Content-depth blocks (the "balance" — professional substance, not influencer-thin):**
`\body{...}` (a 2-line explanation: what + why), `\pt{...}` (one bullet, blue ▸
marker), and `\begin{callout}[colour]{LABEL} … \end{callout}` — a value box with a
coloured left border: **GOTCHA** (`dotamber`), **WHY IT MATTERS** (default blue),
**PRO TIP** (`dotgreen`). The callout is where the *senior insight* lives (the trap,
the trade-off, the perf note) — that's what separates it from a syntax listicle.

**Balanced slide anatomy (learned from the 4:5 height budget ≈ 101mm):** you
CANNOT fit `body + code + callout` on one slide. Compose by slide type:
- **Concept slide** (no code): `kicker → headlinesm → body → \pt bullets → callout`.
- **Example slide** (with code): `kicker → headlinesm → codecard → callout` — no
  separate body; the **callout carries the depth**. Keep code ≤3 lines, callout ≤3.
- **Recap slide**: `kicker → headlinesm → \pt bullets → PRO TIP callout`.
Deck shape: cover (photo) → 1 context slide → N example slides → a "common
mistakes" recap → closing (author + QR). ~13 slides ≈ a 5-min read. Always
recompile and confirm the page count == number of `sld`s (an overflowing slide
silently spills to a 2nd page).

**Code cards per language:** `\begin{codecard}{f.sql}` = SQL highlighting;
`\begin{pycard}{f.py}` = Python highlighting (both mac-window, atomic). Add a new
`\lstdefinestyle` + `\newtcblisting` to Headers for another language. **The card's
filename argument is typeset as text — avoid `_` in it** (use `args.py`, not
`with_args.py`) or escape it. Inside the listing body, `_ % * @` are fine.

**Covers use `Images/`, not `Photos/`.** LinkedIn covers come from the repo-root
`Images/` pool (`../../Images/` — dark tech backdrops: Coder_at_Night, Futuristic
Cybersecurity Analyst, Glowing Neon Abstract…). `Photos/` is the Instagram pool.
Bake to 4:5: `magick "Images/<name>.jpeg" -auto-orient -resize 1080x1350^ -gravity
center -extent 1080x1350 assets/cover.jpg`.

**Porting an old post + a QR guide.** To rebuild a `Python/…` post in this format:
put runnable examples in `codes/NN_name.py`, write the deep-dive as the post
folder's **`README.md`** (GitHub renders it as the folder landing page), and point
`\sourceqr` at the folder URL (`.../tree/main/LinkedIn/<Post>`) so scanning the QR
lands on the guide with `codes/` right there. Reference deck: `LinkedIn/PythonDecorators/`.

**ARTICLE format (`LinkedIn/Headers/Article.tex`).** A THIRD LinkedIn output: the
old flowing multi-page *article* (sections, prose, references) dressed in the new
navy palette (Inter + JetBrains Mono, mac-window code cards, callouts, left line-number gutter + top-right glow). Use it when
the topic wants depth/long-form rather than a swipe deck — Alejandro asked for this
"mix" for Python Decorators. 3:4 portrait document (180×240mm), XeLaTeX ×2. Preamble
`\def\lnkroot{../}\input{\lnkroot Headers/Article.tex}`; commands: `\arttitlepage{tag}{Title}{Subtitle}{qr}`
(magazine-style photo cover via `\coverphoto{img}` first), `\setheader{Python}{Decorators}` (per-page header: blue LANG pill + divider + gold TOPIC; the footer is an author bar on every page; QR labels sit centered BELOW the QR),
`\section`/`\subsection`, `\begin{pycard}{f.py}`/`\begin{sqlcard}{f.sql}`,
`\begin{callout}[colour]{LABEL}`, `\code{}` / `\hb{}` / `\tb{}`, `\artclosing{qr}`.
Same folder as the deck (shares `codes/`, `assets/`, `README.md`). Reference:
`LinkedIn/PythonDecorators/DecoratorsArticle.tex`. (Code-card filenames still can't
contain `_`; the `callout` is unbreakable so it never orphans its label mid-page.)

**Gotchas learned:** `\pagestyle{empty}` kills default page numbers. The cover
overlay is a **baked alpha PNG** (`Headers/overlay.png`), NOT a pgf-opacity fill —
pgf transparency corrupts the eso-pic stream under XeLaTeX (same lesson as the
Instagram veil). 4:5 is shorter than 3:4, so keep leads to ~2 lines and code cards
to ~4 lines or a slide overflows to a 2nd page (recompile and check the page count
== `\setdeck`). Palette/fonts/commands all live in `LinkedIn/Headers/Headers.tex`.

**Compile:** `cd LinkedIn/<Post> && xelatex -interaction=nonstopmode <Post>.tex` (twice),
then `pdftoppm -png -scale-to-x 1080 -scale-to-y 1350 <Post>.pdf preview` to inspect.

---

## Legacy dense-article format (Python / JavaScript / AI)

## Project Structure

```
social-media-posts/
├── Python/
│   ├── Decorators/
│   │   ├── decorators.tex
│   │   └── codes/
│   │       └── example.py
│   └── Headers/
│       └── Headers.tex
├── JavaScript/
│   ├── Promises/
│   │   ├── PromisesPart1.tex
│   │   └── codes/
│   └── Headers/
│       └── Headers.tex
├── ArtificialIntelligence/
│   └── ReasoningFrameworks/
│       └── reasoning_framework.tex
└── Images/
    ├── profile-image.jpeg
    └── *.jpeg (background images)
```

## Color Schemes

### Python Posts
- **Background**: Dark blue (`RGB{15, 22, 36}`)
- **Primary Text**: White (`RGB{255, 255, 255}`)
- **Accent**: Python Yellow (`RGB{255, 212, 59}`)
- **Code Blue**: `RGB{120, 180, 255}`

### JavaScript Posts
- **Background**: Dark (`RGB{13, 17, 23}`)
- **Primary Text**: White (`RGB{255, 255, 255}`)
- **Accent**: JS Yellow (`RGB{255, 220, 60}`)
- **Secondary**: Gray (`RGB{180, 180, 180}`)

### AI Posts
- **Background**: Dark blue-purple (`RGB{15, 22, 36}`)
- **Primary Text**: White
- **Accent**: Purple/Violet theme

## Document Structure

Every post MUST follow this structure:

### 1. Title Page
```latex
\begin{titlepage}
    \titlepagecontents
\end{titlepage}
```

The `titlepagecontents` macro includes:
- Language tag (e.g., `\languagetag{Python}`)
- Main title with accent color
- Subtitle/tagline
- Date
- QR code to source code

### 2. Content Sections

```latex
\section{Section Title}
\subsection{Subsection Title}
\subsubsection{Subsubsection Title}
```

### 3. Code Blocks

Use the `macterminal` environment:
```latex
\begin{macterminal}
\begin{lstlisting}
# Your code here
\end{lstlisting}
\end{macterminal}
```

Or include from file:
```latex
\begin{macterminal}
\lstinputlisting[language=Python]{codes/example.py}
\end{macterminal}
```

### 4. Bullet Lists

```latex
\begin{itemize}
    \item \textbf{\textcolor{pythonBlue}{Bold Label:}} Description
    \item \textbf{\textcolor{pythonBlue}{Another:}} More text
\end{itemize}
```

### 5. Final Page (Call to Action)
```latex
\clearpage
\thispagestyle{empty}
\finalpagecontents
```

### 6. "Explore My Other Posts" Section
Include before final page with QR code linking to related post.

### 7. References Section
Always include references with proper citations and links.

## Required LaTeX Packages

```
\usepackage{xcolor}
\usepackage{amsmath}
\usepackage{graphicx}
\usepackage{tikz}
\usepackage{listings}
\usepackage{sourcesanspro}
\usepackage{fontawesome5}
\usepackage{titlesec}
\usepackage{hyperref}
\usepackage{mdframed}
\usepackage{qrcode}
\usepackage{eso-pic}
\usetikzlibrary{calc,shapes,positioning}
```

## Key Commands

### Language Tag
```latex
\languagetag{Python}  % Creates colored badge
```

### Inline Code
```latex
\code{variable_name}           % Yellow monospace
\codebf{keyword_or_function}    % Blue monospace
```

### Section Colors
```latex
\textcolor{accentColor}{text}   % Yellow/Gold
\textcolor{pythonBlue}{text}    % Light blue (Python)
\textcolor{secondaryColor}{text}% Gray
```

## Code Style Guidelines

1. **Python Posts**: Use `language=Python` in listings, include built-in functions in emphasized list
2. **JavaScript Posts**: Use `language=JavaScript`, include Node.js-specific functions
3. **Include run instructions**: Tell users how to run the code
4. **Show output**: Include expected output after code blocks
5. **Add comments**: Explain complex parts in code comments

## Post Structure Template

```
1. Title Page (with background image + QR)
2. Introduction - What is the topic and why it matters
3. Basic Concepts - Fundamental explanations
4. Code Examples - Step-by-step demonstrations
5. Practical Applications - Real-world use cases
6. Best Practices - Tips and recommendations
7. Conclusion - Summary and next steps
8. References - Links to sources
9. "Explore My Other Posts" - Cross-promotion
10. Final Page - "Found this helpful?" CTA
```

## Header/Footer

### Header (all pages except title)
- Left: `[TOPIC] SECTION NAME` badge
- Example: `[PYTHON] DECORATORS`

### Footer
- Profile image (circular, 1.2-1.6cm)
- Name: `Alejandro Sánchez Yalí`
- Tagline: `Software Developer | AI & Blockchain Enthusiast`
- Website: `www.asanchezyali.com`

## Image Requirements

### Background Images
- Location: `../../Images/` (from post directory)
- Recommended: 1920x1080 or similar aspect ratio
- Overlay: 70% black opacity for readability

### Profile Image
- Location: `../../Images/profile-image.jpeg` or `Images/profile-image.jpeg`
- Shape: Circular (clipped in TikZ)

## Naming Conventions

- Directories: `TopicName/` or `TopicName_PartN/`
- LaTeX files: `topic_name.tex` or `topic_name_partN.tex`
- Code files: `NN_filename.ext` (numbered for order)

## Workflow

1. User requests a new post on a topic
2. Identify the correct category (Python/JavaScript/AI)
3. Create directory structure
4. Copy appropriate Headers.tex
5. Write content following template
6. Extract code examples to separate files in `codes/`
7. Add QR codes linking to:
   - Source code (GitHub)
   - Related posts (LinkedIn)
8. Validate LaTeX compiles correctly

## Quality Checklist

- [ ] Document compiles without errors
- [ ] All code examples are complete and runnable
- [ ] Code includes run instructions
- [ ] Expected output shown
- [ ] Proper syntax highlighting per language
- [ ] Header shows correct topic/section
- [ ] Footer has correct profile info
- [ ] Title page has background image and QR
- [ ] Final page has CTA
- [ ] References section included
- [ ] Cross-promotion section present
- [ ] All external links work
- [ ] Color scheme matches topic
