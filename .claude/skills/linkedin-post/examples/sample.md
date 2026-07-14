# Sample Output: Python Context Managers Post

This is an example of the expected LaTeX output for a Python Context Managers post.

## Generated Files

### File: `Python/ContextManagers/context_managers.tex`

```latex
\input{../Headers/Headers.tex}

\newcommand{\BackgroundPic}{%
    \put(0,0){%
        \begin{tikzpicture}[remember picture, overlay]
            \node[inner sep=0pt] at (current page.center) {
                \includegraphics[width=\paperwidth,height=\paperheight,keepaspectratio=false]{../../Images/Cyberpunk City Night.jpeg}
            };
            \fill[black, opacity=0.7] (current page.south west) rectangle (current page.north east);
        \end{tikzpicture}%
    }%
}

\newcommand{\titlepagecontents}{%
    \AddToShipoutPicture*{\BackgroundPic}
    \vspace*{2cm}
    \begin{flushleft}
    \languagetag{Python}\\[0.4cm]
    {\fontsize{48}{52}\bfseries\color{primaryColor}Python \color{accentColor}Context Managers\par}
    \vspace{0.3cm}
    {\fontsize{18}{52}\color{secondaryColor}Elegant Resource Management with "with"\par}
    \vspace{0.3cm}
    {\color{secondaryColor}\today\par}
    \vspace{2cm}
    \elegantqr{https://github.com/asanchezyali/social-media-posts/tree/main/Python/ContextManagers}{Source Code}
    \end{flushleft}
}

\newcommand{\finalpagecontents}{%
    \AddToShipoutPicture*{\BackgroundPic}
    \vspace*{3cm}
    \begin{flushleft}
    \languagetag{Feedback}\\[0.4cm]
    {\fontsize{46}{52}\bfseries\color{primaryColor}Found this \color{accentColor}helpful?\par}
    \vspace{0.3cm}
    {\fontsize{18}{52}\color{secondaryColor}Save, comment and share\par}
    \vspace{0.3cm}
    {\color{secondaryColor}\today\par}
    \end{flushleft}
}

\begin{document}
\setlength{\parindent}{0pt}

\begin{titlepage}
    \titlepagecontents
\end{titlepage}

\section{Understanding Context Managers}

Context managers provide a clean way to handle setup and teardown operations, ensuring resources are properly acquired and released.

\subsection{Why Use Context Managers?}

Traditional resource management requires manual cleanup:

\begin{macterminal}
\begin{lstlisting}
# Without context manager - error-prone
file = open("data.txt", "r")
content = file.read()
file.close()  # What if an error occurs above?
\end{lstlisting}
\end{macterminal}

Context managers solve this with guaranteed cleanup:

\begin{macterminal}
\begin{lstlisting}
# With context manager - automatic cleanup
with open("data.txt", "r") as file:
    content = file.read()
# File automatically closed, even if error occurs
\end{lstlisting}
\end{macterminal}

Key benefits:
\begin{itemize}
    \item \textbf{\textcolor{pythonBlue}{Guaranteed Cleanup:}} Resources released even on exceptions
    \item \textbf{\textcolor{pythonBlue}{Readability:}} Clear scope boundaries
    \item \textbf{\textcolor{pythonBlue}{Reusability:}} Create custom managers with \code{\_\_enter\_\_} and \code{\_\_exit\_\_}
\end{itemize}

\section{The \textit{with} Statement}

The \code{with} statement handles context management automatically:

\begin{macterminal}
\lstinputlisting[language=Python]{codes/01_basic_context.py}
\end{macterminal}

\section{Creating Custom Context Managers}

You can create custom managers in two ways:

\subsection{Class-Based Approach}

\begin{macterminal}
\begin{lstlisting}
class Timer:
    def __enter__(self):
        import time
        self.start = time.time()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        elapsed = time.time() - self.start
        print(f"Elapsed: {elapsed:.4f} seconds")
        return False  # Don't suppress exceptions

with Timer() as t:
    sum(range(1000000))
# Output: Elapsed: 0.0234 seconds
\end{lstlisting}
\end{macterminal}

\subsection{Decorator-Based Approach}

\begin{macterminal}
\begin{lstlisting}
from contextlib import contextmanager

@contextmanager
def timer():
    import time
    start = time.time()
    try:
        yield
    finally:
        elapsed = time.time() - start
        print(f"Elapsed: {elapsed:.4f} seconds")

with timer():
    sum(range(1000000))
# Output: Elapsed: 0.0234 seconds
\end{lstlisting}
\end{macterminal}

\section{Practical Applications}

Context managers are perfect for:
\begin{itemize}
    \item \textbf{\textcolor{pythonBlue}{File Operations:}} Automatic file closing
    \item \textbf{\textcolor{pythonBlue}{Database Connections:}} Transaction handling
    \item \textbf{\textcolor{pythonBlue}{Locks:}} Thread synchronization
    \item \textbf{\textcolor{pythonBlue}{Temporary Changes:}} State management
\end{itemize}

\section{Conclusion}

Context managers are a powerful Python feature for resource management. They ensure cleanup happens reliably, make code more readable, and can be created for any setup/teardown pattern.

\section{References}
\begin{itemize}
    \item Python Documentation. \textit{Context Managers}. \href{https://docs.python.org/3/reference/compound_stmts.html#with}{Link}
    \item Real Python. \textit{Context Managers}. \href{https://realpython.com/python-with-statement}{Link}
    \item Translated, edited and written in collaboration with AI.
\end{itemize}

\clearpage
\thispagestyle{empty}
\finalpagecontents

\end{document}
```

### File: `Python/ContextManagers/codes/01_basic_context.py`

```python
# --- 01_basic_context.py ---
# How to run:
# 1. Save as 01_basic_context.py
# 2. Run: python 01_basic_context.py

with open("sample.txt", "w") as file:
    file.write("Hello, Context Managers!")

# File is automatically closed here
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)

# Output:
# Hello, Context Managers!
```

---

## Visual Structure

```
┌─────────────────────────────────────┐
│  [Background Image + Dark Overlay]  │
│                                     │
│  ┌──────────┐                      │
│  │  PYTHON  │                      │
│  └──────────┘                      │
│                                     │
│  Python Context Managers            │
│  Elegant Resource Management        │
│                                     │
│  ┌─────────┐                       │
│  │ QR Code │   Source Code         │
│  └─────────┘                       │
└─────────────────────────────────────┘

Page 2-N:
┌─────────────────────────────────────┐
│ PYTHON │ CONTEXT MANAGERS      [H] │
│─────────────────────────────────────│
│                                     │
│  1. Understanding Context Managers │
│     • Why Use Context Managers?     │
│     • Code examples with output     │
│                                     │
│  2. The with Statement              │
│     • Basic usage                   │
│     • File operations               │
│                                     │
│  3. Creating Custom Managers        │
│     • Class-based                   │
│     • Decorator-based               │
│                                     │
│  4. Practical Applications         │
│                                     │
│  5. Conclusion                      │
│                                     │
│  6. References                      │
│                                     │
│─────────────────────────────────────│
│ [Photo] Alejandro Sanchez Yali      │
│        Software Developer...        │
│        www.asanchezyali.com         │
└─────────────────────────────────────┘

Final Page:
┌─────────────────────────────────────┐
│  [Background Image + Dark Overlay]  │
│                                     │
│  ┌──────────┐                      │
│  │ FEEDBACK │                      │
│  └──────────┘                      │
│                                     │
│  Found this helpful?                │
│  Save, comment and share            │
└─────────────────────────────────────┘
```
