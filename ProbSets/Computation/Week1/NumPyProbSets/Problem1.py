import numpy as np

def dotProduct():
    A = np.array([
        [3, -1, 4],
        [1, 5, -9]
        ])
    B = np.array([
        [2, 6, -5, 3],
        [5, -8, 9, 7],
        [9, -3, -2, -3]
        ])
    return np.dot(A, B)

print(dotProduct())
