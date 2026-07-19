# yalix carousel — copy-paste skeleton (Instagram)

A ready starting point for a new post. Create
`Instagram/<Series>/<Post>/<Post>.tex`, paste this, drop a **new** cover image in
`Instagram/<Series>/<Post>/assets/`, then write the article between the cover and
the closing. Compile with `xelatex` twice.

```latex
% =====================================================================
%  yalix -- "<TÍTULO>"  (apuntes de estudiante)
%  Compilar:  xelatex <Post>.tex   (dos pasadas)
% =====================================================================
\def\yalixroot{../../../}\input{\yalixroot Headers/Headers.tex}
\input{../palette.tex}                      % OPCIONAL: paleta de la serie (un nivel arriba)
\settotalslides{10}                        % opcional: ya no hay puntos de progreso (no-op)
\setwatermark{@asanchezyali}
\setseriestag{Álgebra lineal · ML \#2}     % OPCIONAL: módulo + nº de parte (el número va aquí, no en el texto)

\begin{document}

% ===================== PORTADA ======================================
\begin{slidec}
  \coverphoto{assets/cover.jpg}            % foto NUEVA para cada post
  \raggedright
  \serlead{Serie · Matemáticas para Machine Learning}
  \vspace{1mm}
  \sertitle{\fontsize{35}{38}\selectfont <Título del post>}
  \vspace{4mm}
  \hand{\hl{Parte 1} · <subtítulo breve>}
\end{slidec}
\clearpage

% ===================== ARTÍCULO (fluye y se pagina solo) =============
\RaggedRight\hyphenpenalty=2500\exhyphenpenalty=2500
\setlength{\parindent}{0pt}\setlength{\parskip}{1.4mm}
\fontsize{13.5}{16}\selectfont\vspace*{1mm}

\topic{Primer tema}
\hand{Texto que fluye, alineado a la izquierda, como apuntes reales.}
\defn{Una \uhand{palabra clave} es <definición en una frase>.}
\eqx{a_{11}x_1 + \cdots + a_{1n}x_n = b_1}
\obs{Observación que se sostiene por sí sola, sin conectar hacia atrás.}

\topic{Segundo tema}
\hand{Más apuntes. Resalta lo importante con \hl{marcador}.}
\keyeq{A\,\mathbf{x} = \mathbf{b}}

% ... más \topic / \hand / \defn / \eq / \obs / gráficos pgfplots ...

\clearpage
% ===================== CIERRE =======================================
\begin{slidec}
  \raggedright
  \sertitle{\fontsize{24}{27}\selectfont ¿Te sirvió este resumen?}
  \vspace{5mm}
  \hand{Esta es la \hl{Parte 1} de la serie "Matemáticas para Machine Learning".}
  \vspace{3mm}
  \hand{\hl{Guarda} esto y \hl{sígueme} para las siguientes en \hl{asanchezyali.com}}
\end{slidec}

\end{document}
```

## Gráfico pgfplots (patrón de referencia)

Etiquetas sobre cada recta (mismo color que la recta), sin tocar la curva, y la
coordenada de la intersección debajo del punto con guía punteada:

```latex
\begin{center}
\begin{tikzpicture}
  \begin{axis}[
      width=64mm, height=48mm,
      axis lines=middle, axis line style={mauve, line width=0.5pt},
      xlabel={$x_1$}, ylabel={$x_2$},
      xlabel style={mauve, font=\tiny, anchor=north west},
      ylabel style={mauve, font=\tiny, anchor=south east},
      xtick=\empty, ytick=\empty, clip=false,
    ]
    \addplot[eqink, line width=1pt, domain=-0.6:2.3] {1.25 - x}
      node[pos=0.17, sloped, above, eqink, font=\tiny, inner sep=2.5pt] {$4x_1+4x_2=5$};
    \addplot[accent, line width=1pt, domain=-0.6:2.3] {0.5*x - 0.25}
      node[pos=0.82, sloped, above, accent, font=\tiny, inner sep=2.5pt] {$2x_1-4x_2=1$};
    \fill[ink] (axis cs:1,0.25) circle (1.5pt);
    \draw[ink, line width=0.3pt, densely dotted] (axis cs:1,0.16) -- (axis cs:1,-0.34);
    \node[ink, font=\tiny, anchor=north] at (axis cs:1,-0.4) {$(1,\tfrac14)$};
  \end{axis}
\end{tikzpicture}
\end{center}
```
