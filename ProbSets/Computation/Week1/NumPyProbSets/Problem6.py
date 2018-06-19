import numpy as np

def rowStochastic(A):
    Asum = A.sum(axis = 1)
    ARowStochastic = A / Asum[:, np.newaxis]
    return ARowStochastic

A = np.array([
    [1, 2, 3],
    [4, 4, 4]
    ])
print(rowStochastic(A))
