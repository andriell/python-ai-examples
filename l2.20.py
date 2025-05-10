import numpy as np

# Создание произвольной матрицы
A = np.array([[1, 2], [3, 4]])

# Сингулярное разложение
U, Sigma, Vt = np.linalg.svd (A)
print("матрица U: \n", U)
print("матрица Sigma: \n", Sigma)
print("матрица Vt: \n", Vt)

# Проверка результатов
reconstructed_A = np.dot (U, np.dot(np. diag (Sigma), Vt))
print("Исходная матрица А: \n", A)
print("Восстановленная матрица A:\n", reconstructed_A)
