import month_length as ml

def test_month_length():
    assert ml.month_length("September") == 30, "failed September"
    assert ml.month_length("January") == 31, "failed January"
    assert ml.month_length("February") == 28, "failed January"
    assert ml.month_length("February", leap_year = True) == 29, "failed January"
    assert ml.month_length("Pythonista") == None, "failed no month"
