import pytest
import sets as st
import copy

def test_count_sets():
    # hand with 6 sets
    hand1 = ["1022", "1122", "0100", "2021",
            "0010", "2201", "2111", "0020",
            "1102", "0210", "2110", "1020"]
    # hand with missing card
    hand2 = ["1122", "0100", "2021",
            "0010", "2201", "2111", "0020",
            "1102", "0210", "2110", "1020"]
    # hand with not unique cards
    hand3 = ["1122", "1122", "0100", "2021",
            "0010", "2201", "2111", "0020",
            "1102", "0210", "2110", "1020"]
    # hand with a card missing an entry
    hand4 = ["022", "1122", "0100", "2021",
            "0010", "2201", "2111", "0020",
            "1102", "0210", "2110", "1020"]
    # hand with a card with an entry different
    # from '0', '1' or '2'
    hand5 = ["1522", "1122", "0100", "2021",
            "0010", "2201", "2111", "0020",
            "1102", "0210", "2110", "1020"]
    assert st.count_sets(hand1) == 6, "failed for a valid Set card"
    with pytest.raises(ValueError) as excinfo:
        st.count_sets(hand2)
    with pytest.raises(ValueError) as excinfo:
        st.count_sets(hand3)
    with pytest.raises(ValueError) as excinfo:
        st.count_sets(hand4)
    with pytest.raises(ValueError) as excinfo:
        st.count_sets(hand5)

def test_is_set():
    a = "1111"
    b = "1020"
    c = "1202"
    d = "0100"
    assert st.is_set(a, b, c) == True, "failed to recognise a set"
    assert st.is_set(a, b, d) == False, "failed to recognise a non set"
