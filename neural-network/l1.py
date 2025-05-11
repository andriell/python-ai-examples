import numpy as np

def act(x):
    return 0 if x < 0.5 else 1

def go(house, rock, attr):
    x = np.array([house, rock, attr])
    w11 = [0.3, 0.3, 0]
    w12 = [0.4, -0.5, 1]
    weight1 = np.array([w11, w12]) # Матрица 2х3
    weight2 = np.array([-1, 1]) # Вектор 1х2

    sum_hidden = np.dot(weight1, x)
    print("Значения сумм на нейронах скрытого слоя: " + str(sum_hidden))

    out_hidden = np.array([act(x) for x in sum_hidden])
    print("Значения на выходов нейронах скрытого слоя: " + str(out_hidden))

    sum_end = np.dot(weight2, out_hidden)
    y = act(sum_end)

    print("Выходное знчение НС: " + str(y))

    return y

res = go(1, 0, 1)

if res == 1:
    print("Ты мне наравишься")
else:
    print("Ты мне не наравишься")
