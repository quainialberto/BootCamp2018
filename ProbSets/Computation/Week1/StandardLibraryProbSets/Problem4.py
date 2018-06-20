from itertools import chain, combinations

def powerset(A):
    A = list(A)
    return chain.from_iterable(combinations(A, r) for r in range(len(A) + 1))

A = ['a', 'b', 'c']
print( list(powerset(A)) )
