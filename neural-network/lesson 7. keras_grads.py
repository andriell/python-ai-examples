import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Input

c = np.array([-40, -10, 0, 8, 15, 22, 38])
f = np.array([-40, 14, 32, 46, 59, 72, 100])
# f = np.array([-40, 14, 32, 46.4, 59, 71.6, 100.4])

model = keras.Sequential()
model.add(Input(shape=(1,)))
model.add(Dense(units=1, activation='linear'))
model.compile(loss='mean_squared_error', optimizer=keras.optimizers.Adam(0.1))
# model.set_weights(([np.array([[9/5]]), np.array([32])]))
history = model.fit(c, f, epochs=500, verbose=0)
print("Обучение завершено")

print(model.predict(x=np.array([100])))
print(model.get_weights())
print(model.save_weights(filepath='lesson7.weights.h5'))

plt.plot(history.history['loss'])
plt.grid(True)
plt.show()
