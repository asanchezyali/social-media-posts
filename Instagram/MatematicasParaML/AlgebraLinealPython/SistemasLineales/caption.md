Sistemas lineales con Python — resolver Ax = b en una línea. 🐍

Arranca la serie Álgebra Lineal con Python: los mismos temas del álgebra lineal, pero desarrollados con NumPy. Empezamos por lo más útil: resolver un sistema de ecuaciones lineales.

En este resumen:
• La idea: un sistema se guarda como una matriz A y un vector b. Resolverlo es hallar el x con Ax = b.
• Montarlo: A = np.array([[1,1,1],[1,-1,2],[0,1,1]]), b = np.array([3,2,2]).
• Resolverlo en una línea: x = np.linalg.solve(A, b) → array([1., 1., 1.]). Por dentro NumPy factoriza A = LU (LAPACK), no invierte A: es O(n³) y estable.
• Verificar: np.allclose(A @ x, b) → True. El operador @ es el producto matriz-vector.
• Cuándo NO hay solución única: si A es singular (una fila combinación de otras), solve lanza LinAlgError. El rango decide: si rank(A) < n hay 0 o ∞ soluciones. Para esos casos, np.linalg.lstsq da la solución de mínimos cuadrados.
• Regla de oro: usa solve, nunca inv(A) @ b — más lento, menos preciso y casi nunca hace falta.

¿Resuelves tus sistemas a mano o dejas que NumPy piense? 👇

Guárdalo y sígueme para las siguientes en asanchezyali.com

#álgebralineal #python #numpy #machinelearning #sistemaslineales #datascience #matematicas #linearalgebra #programación #cienciadedatos
