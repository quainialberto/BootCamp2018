import numpy as np

def foo():
    A = np.triu( np.ones((7, 7)) )
    Bl = np.tril( np.full_like(A, -1) )
    Bu = np.triu( np.full_like(A, 5) )
    np.fill_diagonal(Bu, 0)
    B = Bl + Bu
    M = np.dot( np.dot(A, B), A)
    M = M.astype(np.int64)
    return M

print(foo())
