from itertools import combinations

def powerset(A):
    powA = []
    for i in range(len(A)+1):
        addSet = combinations(A, i)
        for item in addSet:
            powA.append(set(item))
    return powA

A = ['aa', 'b', 'c']
print( list(powerset(A)) )
