import numpy as np

def cayleyHamilton():
    A = np.array([
        [3, 1, 4],
        [1, 5, 9],
        [-5, 3, 1]
        ])
    Asquare = np.dot(A, A)
    Acube = np.dot(Asquare, A)
    return -Acube + 9 * Asquare - 15 * A

print(cayleyHamilton())
