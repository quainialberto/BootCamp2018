import smallest_factor as sm

def test_smallest_factor_corrected():
    assert sm.smallest_factor_corrected(6) == 2, "failed on 6"
    assert sm.smallest_factor_corrected(3) == 3, "failed on 3"

def test_smallest_factor():
    assert sm.smallest_factor(1) == 1, "failed on 1"
    assert sm.smallest_factor(2) == 2, "failed on 2"
    assert sm.smallest_factor(10) == 2, "failed on 10"
    assert sm.smallest_factor(6) == 2, "failed on 6"
