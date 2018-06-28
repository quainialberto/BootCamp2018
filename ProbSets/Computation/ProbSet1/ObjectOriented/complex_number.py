from math import sqrt

class ComplexNumber:
    """A ComplexNumber object class. Has a real part and an impaginary.
     Attributes:
         real (float): the real part.
         imag (float): the imaginary part.
     Methods:
         put: add items to the backpack's list of contents.
         take: remove items from the backpack's list of contents.
    """
    def __init__(self, real, imag):
        """Set the real and the imaginary part.
        Parameters:
            real (float): the real part.
            imag (float): the imaginary part.
        """
        self.real = real
        self.imag = imag
    def conjugate(self):
        """Returns the conjugate of the ComplexNumber."""
        return ComplexNumber(self.real, -self.imag)
    def __str__(self):
        """Return the string representation of ComplexNumber.
        """
        if self.imag >=0:
            return "(" + str(self.real) + "+" + str(self.imag) + "i)"
        else:
            return "(" + str(self.real) + str(self.imag) + "i)"
    def __abs__(self):
        """Return the absolute value of ComplexNumber.
        """
        return sqrt(self.real**2 + self.imag**2)
    def __eq__(self, other):
        """Returns True if two ComplexNumbers have the same real and
        imaginary part. Returns False otherwise.
        """
        if self.real == other.real and self.imag == other.imag:
            return True
        else:
            return False
    def __add__(self, other):
        """Add two ComplexNumbers.
        """
        return ComplexNumber(self.real + other.real,
                self.imag + other.imag)
    def __sub__(self, other):
        """Subtract two ComplexNumbers.
        """
        return ComplexNumber(self.real - other.real,
                self.imag - other.imag)
    def __mul__(self, other):
        """Multiply two ComplexNumbers.
        """
        real1 = self.real * other.real - self.imag * other.imag
        imag1 = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real1, imag1)
    def __truediv__(self, other):
        """Divide two ComplexNumbers.
        """
        denom = other.real**2 + other.imag**2
        real2 = self.real * other.real + self.imag * other.imag
        imag2 = self.imag * other.real - self.real * other.imag
        return ComplexNumber(real2 / denom, imag2 / denom)

def test_complex_number():
    print("Test ComplexNumber")
    print("==================")
    my_cmp = ComplexNumber(2, 3)
    my_conj = my_cmp.conjugate()
    py_cmp = complex(2, 3)
    py_conj = complex(2, -3)
    if my_cmp.real != 2:
        print("ComplexNumber.real assigned incorrectly")
    if my_cmp.imag != 3:
        print("ComplexNumber.imag assigned incorrectly")
    if my_conj.real != 2 and my_conj.imag != -3:
        print("ComplexNumber's conjugate method incorrect")
    print(my_cmp)
    print(my_conj)
    if abs(my_cmp) != abs(py_cmp):
        print("ComplexNumber __abs__ method implemented incorrectly")
    if my_cmp != py_cmp:
        print("ComplexNumber __eq__ method implemented incorrectly")
    if my_cmp + my_conj != py_cmp + py_conj:
        print("ComplexNumber __add__ method implemented incorrectly")
    if my_cmp - my_conj != py_cmp - py_conj:
        print("ComplexNumber __sub__ method implemented incorrectly")
    if my_cmp * my_conj != py_cmp * py_conj:
        print("ComplexNumber __mul__ method implemented incorrectly")
    if my_cmp / my_conj != py_cmp / py_conj:
        print("ComplexNumber __truediv__ method implemented incorrectly")

test_complex_number()
