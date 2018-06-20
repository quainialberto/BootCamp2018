import pytest
import sets as st
import copy

def test_count_sets():
     hand1 = ["1022", "1122", "0100", "2021",
             "0010", "2201", "2111", "0020",
             "1102", "0210", "2110", "1020"]
     hand2 = hand1.append(["1120"])
     hand3 = copy.copy(hand1)
     hand3[0] = "1122"
     hand4 = copy.copy(hand1)
     hand4[0] = "102"
     hand5 = copy.copy(hand1)
     hand5[0] = "1023"
     assert st.count_sets(hand1) == 6, "failed for a valid Set card"
     with pytest.raises(ValueError) as excinfo:
         st.count_sets(hand1)
         st.count_sets(hand2)
         st.count_sets(hand3)
         st.count_sets(hand4)
         st.count_sets(hand5)

def test_is_set():
    a = "1111"
    b = "1020"
    c = "1202"
    d = "0100"
    assert st.is_set(a, b, c) == True, "failed to recognise a set"
    assert st.is_set(a, b, d) == False, "failed to recognise a non set"
