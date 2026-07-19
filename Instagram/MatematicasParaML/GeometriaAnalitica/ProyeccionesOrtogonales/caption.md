Proyecciones ortogonales — la sombra más cercana de un vector. 🔦

Módulo de Geometría Analítica de la serie Matemáticas para Machine Learning. Proyectar es, quizá, la operación más usada en machine learning: PCA, mínimos cuadrados y la regresión son, en el fondo, proyecciones.

En este resumen:
• La idea: proyectar x sobre un subespacio U es hallar el punto de U más cercano a x. La clave es que el error x − π_U(x) queda perpendicular a U.
• Sobre una recta: π_U(x) = (⟨x,b⟩ / ⟨b,b⟩) b.
• La matriz de proyección: P = bbᵀ/(bᵀb) sobre una recta, y P = B(BᵀB)⁻¹Bᵀ en general. Es simétrica y cumple P² = P (proyectar dos veces da lo mismo).
• Por qué importa: mínimos cuadrados proyecta sobre el espacio columna; PCA proyecta sobre las direcciones de mayor varianza. Comprimir bien es proyectar bien.

¿Sobre qué subespacio proyectas tus datos? 👇

Guárdalo y sígueme para las siguientes en asanchezyali.com

#geometríaanalítica #álgebralineal #matemáticas #machinelearning #proyecciones #pca #mínimoscuadrados #matematicasparaml #datascience #linearalgebra
