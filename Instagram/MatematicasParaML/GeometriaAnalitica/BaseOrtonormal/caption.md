Base ortonormal — la base más cómoda para trabajar. 🧭

Módulo de Geometría Analítica de la serie Matemáticas para Machine Learning. Entre todas las bases posibles, hay una familia especialmente cómoda: aquellas cuyos vectores son perpendiculares entre sí y de longitud 1.

En este resumen:
• Qué es una base ortonormal (ONB): ⟨bᵢ,bⱼ⟩ = 1 si i=j y 0 si i≠j. La base estándar es el ejemplo típico.
• Por qué es tan cómoda: las coordenadas de un vector se leen con productos internos, x = Σ ⟨x,bᵢ⟩ bᵢ, sin resolver ningún sistema.
• Cada coeficiente ⟨x,bᵢ⟩ es la proyección de x sobre esa dirección.
• Cómo conseguir una: el proceso de Gram–Schmidt convierte cualquier base en ortonormal. A cada vector le resta su sombra sobre los anteriores, ũₖ = vₖ − Σᵢ<ₖ ⟨vₖ,uᵢ⟩ uᵢ, y luego lo normaliza, uₖ = ũₖ/‖ũₖ‖.

¿En qué base se simplifican tus cuentas? 👇

Guárdalo y sígueme para las siguientes en asanchezyali.com

#geometríaanalítica #álgebralineal #matemáticas #machinelearning #baseortonormal #gramschmidt #matematicasparaml #datascience #mathematics #linearalgebra
