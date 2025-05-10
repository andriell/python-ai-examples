import cv2
import numpy as np

# Загрузка изображения
image = cv2.imread('image.jpg')

# Преобразование изображения в двумерный массив пикселов
pixel_values = image.reshape((-1, 3))
print(pixel_values)

# Применение алгоитма K-средних
k = 3 # Колличество кластеров сегментов
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)

_, label, center = cv2.kmeans(pixel_values.astype(np.float32), k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

# Преобразование центров кластеров в целочисленный фррмат
center = np.uint8(center)

# Приведение каждому пикселю его цвета кластера
segmented_image = center[label.flatten()]

# Преобразование обратно в форму изображения
segmented_image = segmented_image.reshape(image.shape)

# Вывод и сохранение сегментированного изображения
cv2.imshow('Segmented Image', segmented_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('segmented_image.jpg', segmented_image)
