import Fraction
import pytest

@pytest.fixture
def set_up_Fraction():
    frac_1_3 = Fraction.Fraction(1, 3)
    frac_1_2 = Fraction.Fraction(1, 2)
    frac_n2_3 = Fraction.Fraction(-2, 3)
    frac_1_1 = Fraction.Fraction(1, 1)
    frac_0_1 = Fraction.Fraction(0, 1)
    return frac_1_3, frac_1_2, frac_n2_3, frac_1_1, frac_0_1

def test_fraction_init(set_up_Fraction):
    frac_1_3, frac_1_2, frac_n2_3, frac_1_1, frac_0_1 = set_up_Fraction
    assert frac_1_3.numer == 1
    assert frac_1_2.denom == 2
    assert frac_n2_3.numer == -2
    frac = Fraction.Fraction(30, 42) # 30/42 reduces to 5/7.
    assert frac.numer == 5
    assert frac.denom == 7

    with pytest.raises(ZeroDivisionError) as excinfo:
        Fraction.Fraction.__init__('Test', 3, 0)
    with pytest.raises(TypeError) as excinfo:
        Fraction.Fraction.__init__('Test', 3.5, 2)

def test_fraction_str(set_up_Fraction):
    frac_1_3, frac_1_2, frac_n2_3, frac_1_1, frac_0_1 = set_up_Fraction
    assert str(frac_1_3) == "1/3"
    assert str(frac_1_2) == "1/2"
    assert str(frac_n2_3) == "-2/3"
    assert str(frac_1_1) == "1"

def test_fraction_float(set_up_Fraction):
    frac_1_3, frac_1_2, frac_n2_3, frac_1_1, frac_0_1 = set_up_Fraction
    assert float(frac_1_3) == 1 / 3.
    assert float(frac_1_2) == .5
    assert float(frac_n2_3) == -2 / 3.

def test_fraction_eq(set_up_Fraction):
    frac_1_3, frac_1_2, frac_n2_3, frac_1_1, frac_0_1 = set_up_Fraction
    assert frac_1_2 == Fraction.Fraction(1, 2)
    assert frac_1_3 == Fraction.Fraction(2, 6)
    assert frac_n2_3 == Fraction.Fraction(8, -12)

    assert float(frac_n2_3) == frac_n2_3

def test_fraction_add(set_up_Fraction):
    frac_1_3, frac_1_2, frac_n2_3, frac_1_1, frac_0_1 = set_up_Fraction
    assert frac_1_2 + frac_1_3 == Fraction.Fraction(5, 6)

def test_fraction_sub(set_up_Fraction):
    frac_1_3, frac_1_2, frac_n2_3, frac_1_1, frac_0_1 = set_up_Fraction
    assert frac_1_2 - frac_1_3 == Fraction.Fraction(1, 6)

def test_fraction_mul(set_up_Fraction):
    frac_1_3, frac_1_2, frac_n2_3, frac_1_1, frac_0_1 = set_up_Fraction
    assert frac_1_2 * frac_1_3 == Fraction.Fraction(1, 6)

def test_fraction_div(set_up_Fraction):
    frac_1_3, frac_1_2, frac_n2_3, frac_1_1, frac_0_1 = set_up_Fraction
    assert frac_1_2 / frac_1_3 == Fraction.Fraction(3, 2)

    with pytest.raises(ZeroDivisionError) as excinfo:
        frac_1_2 / frac_0_1
