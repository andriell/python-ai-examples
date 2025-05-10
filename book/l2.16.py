import numpy as np

# Пример данных
x = np.array([1, 2, 3])
y = np.array([2, 4, 6])

# Вычисление линейной зависимости
print(np.polyfit(x, y, 1))
