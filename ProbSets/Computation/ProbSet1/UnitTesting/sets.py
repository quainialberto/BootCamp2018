import numpy as np
import itertools as it

def is_set(a, b, c):
    """Determine if the cards a, b, and c constitute a set.
    Parameters:
        a, b, c (str): string representations of 4-bit integers in base 3.
            For example, "1022", "1122", and "1020" (which is not a set).
    Returns:
        True if a, b, and c form a set, meaning the ith digit of a, b,
            and c are either the same or all different for i=1,2,3,4.
        False if a, b, and c do not form a set.
    """
    sets = np.zeros(4)
    for i in range(0, 4):
        if a[i] == b[i] == c[i]:
            sets[i] = 1
        if a[i] != b[i] and a[i] != c[i] and b[i] != c[i]:
            sets[i] = 1
    if sum(sets) == 4:
        return True
    else:
        return False


def count_sets(cards):
    """Return the number of sets in the provided Set hand.
    Parameters:
        cards (list(str)) a list of twelve cards as 4-bit integers in
        base 3 as strings, such as ["1022", "1122", ..., "1020"].
    Returns:
        (int) The number of sets in the hand.
    Raises:
        ValueError: if the list does not contain a valid Set hand, meaning
            - there are not exactly 12 cards,
            - the cards are not all unique,
            - one or more cards does not have exactly 4 digits, or
            - one or more cards has a character other than 0, 1, or 2.
    """
    if len(cards) != 12:
        raise ValueError('the number of cards must be 12')
    if len(set(cards)) != 12:
        raise ValueError('the cards are not unique')
    for i in cards:
        if len(i) != 4:
            raise ValueError('one or more cards does not have exactly 4 digits')
        for j in i:
            if j == '0' or j == '1' or j == '2':
                pass
            else:
                raise ValueError('one or more cards has a character other than 0, 1, or 2')

    combs = list(it.combinations(cards, 3))
    combs_len = len(combs)
    combs_vec = np.zeros(combs_len)
    for i, val in enumerate(combs):
        if is_set(*val):
            combs_vec[i] = 1

    return int(sum(combs_vec))
