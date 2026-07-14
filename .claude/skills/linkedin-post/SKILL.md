---
name: linkedin-post
description: Generate LaTeX technical carousel/post content for LinkedIn — the dark-theme slides organized by programming language/topic (Python/JavaScript/AI) compiled with pdfLaTeX. Use when the user asks to create, draft, or restyle a LinkedIn post here, add a new topic, or work with the dark-theme templates. NOTE: for the cream Instagram "study notes" (yalix) carousels, use the instagram-carousel skill instead.
---

# Social Media Post Skill - LaTeX Technical Articles (LinkedIn)

This skill generates technical social media posts (designed for LinkedIn) using LaTeX with a professional dark theme. The posts are organized by programming language/topic and follow a consistent visual format.

> For the **Instagram** cream grid-paper "study notes" carousels (yalix brand,
> XeLaTeX + SignPainter), use the separate **`instagram-carousel`** skill. This
> skill is only the LinkedIn dark-theme format.

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
