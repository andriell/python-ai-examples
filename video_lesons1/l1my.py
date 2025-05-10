import numpy as np

def act(x):
    return 1 if x >= 0.5 else 0

def do(x1, x2, x3):
    w = np.array([0.5, -0.5, 0.5])
    arr = np.array([x1, x2, x3])
    return act(np.dot(w, arr))

print(do(1, 0, 0))

exit()
