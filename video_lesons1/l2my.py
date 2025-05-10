import numpy as np

def act(x):
    return 0 if x < 0.5 else 1

def do(x01, x02):
    w11 = np.array([1, 1])
    b11 = -1.5
    w12 = np.array([1, 1])
    b12 = -0.5
    x11 = act(np.dot(w11, np.array([x01, x02])) + b11)
    x12 = act(np.dot(w12, np.array([x01, x02])) + b12)
    w21 = np.array([-1, 1])
    b21 = -0.5
    y = act(np.dot(w21, np.array([x11, x12])) + b21)
    return y

print(do(1, 0), do(0, 1))
print(do(0, 0), do(1, 1))
