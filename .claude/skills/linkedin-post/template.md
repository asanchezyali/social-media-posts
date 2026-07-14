# [TOPIC NAME] - Post Template (LinkedIn, dark theme)

Replace all placeholders marked with `[]` with actual content. This is the
**LinkedIn** dark-theme format (pdfLaTeX). For the Instagram cream "study notes"
carousels, use the `instagram-carousel` skill instead.

Create `[Category]/[TopicName]/[topic_name].tex`, copy the appropriate
`[Category]/Headers/Headers.tex` conventions, and extract code to `codes/`.

---

## Preamble

Reuse the category Headers (colors, `macterminal`, `\languagetag`, title/final
page macros). A typical Python post begins:

```latex
\documentclass[12pt,letterpaper]{article}
\usepackage[utf8]{inputenc}
\usepackage[letterpaper, margin=1in, bottom=2.5in, top=1.2in]{geometry}
\usepackage{fancyhdr}
\setlength{\headheight}{15pt}
\setlength{\footskip}{72pt}
\usepackage{xcolor}
\usepackage{amsmath}
\usepackage{anyfontsize}
\usepackage{graphicx}
\usepackage{tikz}
\usepackage{listings}
\usepackage{sourcesanspro}
\renewcommand{\familydefault}{\sfdefault}
\usepackage{fontawesome5}
\usepackage{titlesec}
\usepackage{setspace}
\usepackage{hyperref}
\usepackage{mdframed}
\usepackage{qrcode}
\usepackage{eso-pic}
\usetikzlibrary{calc,shapes,positioning}

% Palette (Python example — swap per language/topic)
\definecolor{bgColor}{RGB}{15, 22, 36}
\definecolor{primaryColor}{RGB}{255, 255, 255}
\definecolor{accentColor}{RGB}{255, 212, 59}      % Python yellow
\definecolor{pythonBlue}{RGB}{120, 180, 255}
\definecolor{secondaryColor}{RGB}{220, 230, 240}

\AtBeginDocument{\color{primaryColor}}
\pagecolor{bgColor}
```

## Body structure

```latex
\begin{document}

% 1. TITLE PAGE (background image + QR to source)
\begin{titlepage}
    \titlepagecontents   % language tag, title, subtitle, date, QR
\end{titlepage}

% 2. INTRODUCTION — what the topic is and why it matters
\section{Introduction}
[Hook + why the reader should care.]

% 3. BASIC CONCEPTS
\section{[Concept]}
[Explanation.]
\begin{itemize}
    \item \textbf{\textcolor{pythonBlue}{Label:}} description
\end{itemize}

% 4. CODE EXAMPLES — Mac-terminal window, from file or inline
\begin{macterminal}
\lstinputlisting[language=Python]{codes/01_example.py}
\end{macterminal}

\textbf{\textcolor{accentColor}{How to Run:}} \code{python codes/01_example.py}

\textbf{Output:}
\begin{macterminal}
\begin{lstlisting}
[expected output]
\end{lstlisting}
\end{macterminal}

% 5. PRACTICAL APPLICATIONS   % 6. BEST PRACTICES
\section{[...]}

% 7. CONCLUSION
\section{Conclusion}
[Summary + next steps.]

% 8. REFERENCES
\section{References}
[Cited links with \href{https://...}{...}.]

% 9. EXPLORE MY OTHER POSTS (QR to a related post)
\section{Explore My Other Posts}

% 10. FINAL PAGE — CTA
\clearpage
\thispagestyle{empty}
\finalpagecontents

\end{document}
```

## Checklist (see SKILL.md for the full list)

- [ ] Title page with background image + QR
- [ ] Code in `macterminal`, extracted to `codes/NN_name.ext`, with run + output
- [ ] Header `[TOPIC] SECTION`, footer with profile + website
- [ ] References + "Explore My Other Posts" + final CTA
- [ ] Compiles with pdfLaTeX; color scheme matches the language
