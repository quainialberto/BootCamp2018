import numpy as np

def stackBunchMatrices():
    A = np.array([
        [0, 2, 4],
        [1, 3, 5]
        ])
    B = np.tril( np.full((3, 3), 3) )
    C = -2 * np.eye(3)
    Mcol1 = np.vstack((
        np.zeros((3, 3)),
        A,
        B
        ))
    Mcol2 = np.vstack((
        A.T,
        np.zeros((2, 2)),
        np.zeros((3, 2))
        ))
    Mcol3 = np.vstack((
        np.eye(3),
        np.zeros((2, 3)),
        C
        ))
    M = np.hstack((
        Mcol1,
        Mcol2,
        Mcol3
        ))
    return M

print(stackBunchMatrices())
