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
     pass
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
pass
