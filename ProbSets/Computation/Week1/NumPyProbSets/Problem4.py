import numpy as np

def negativeToZero(A):
    B = np.copy(A)
    mask = B < 0
    B[mask] = 0
    return B

A = np.array([
    [1, -2, 3],
    [2, 4, -5]
    ])
print(negativeToZero(A))
