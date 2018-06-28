class Backpack:
    """A Backpack object class. Has a name and a list of contents.
    Attributes:
        name (str): the name of the backpack's owner.
        color (str): the backpack's color.
        max_size (int): the backpack's max number of items capacity.
        contents (list): the contents of the backpack.
    Methods:
        put: add items to the backpack's list of contents.
        take: remove items from the backpack's list of contents.
    """
    def __init__(self, name, color, max_size = 5):           # This function is the constructor.
        """Set the name and initialize an empty list of contents.
        Parameters:
            name (str): the name of the backpack's owner.
            color (str): the backpack's color.
            max_size (int): the backpack's max number of items capacity.
        """
        self.name = name                # Initialize some attributes.
        self.contents = []
        self.color = color
        self.max_size = max_size
    def put(self, item):
        """Add 'item' to the backpack's list of contents."""
        if len(self.contents) >= self.max_size:
            print("No Room!")
        else:
            self.contents.append(item)  # Use 'self.contents', not just 'contents'.
    def take(self, item):
        """Remove 'item' from the backpack's list of contents."""
        self.contents.remove(item)
    def dump(self):
        """Reset backpack's content to empty list"""
        self.contents = []
    def __eq__(self, other):
        """If 'self' has the same name, color and number of contents as
        'other', return True. Otherwise, return False.
        """
        if (self.name == other.name and \
            self.color == other.color and \
            len(self.contents) == len(other.contents)):
            return True
        else:
            return False
    def __str__(self):
        """Returns the string representation of a Backpack.
        Namely, returns the owner name, the color, the size,
        the max size and the contents.
        """
        text = "Owner:   \t" + str(self.name) + " \n"\
        "Color:   \t"     + str(self.color) + " \n"\
        "Size:    \t"     + str(len(self.contents)) + " \n"\
        "Max size:\t"     + str(self.max_size) + " \n"\
        "Contents:\t"     + str(self.contents)
        return text

def test_backpack():
    print("Test Backpack")
    print("============")
    testpack = Backpack("Barry", "black")       # Instantiate the object.
    if testpack.name != "Barry":                # Test an attribute.
        print("Backpack.name assigned incorrectly")
    if testpack.color != "black":
        print("Backpack.color assigned incorrectly")
    if not testpack.contents == []:
        print("Default Backpack.contents assigned incorrectly")
    for item in ["pencil", "pen", "paper", "computer"]:
        testpack.put(item)                      # Test put method.
    print("Contents:", testpack.contents)
    for item in ["bread", "knife"]:
        testpack.put(item)                      # Test max_size
    testpack.take("pencil")
    print(testpack.contents)                    # Test take method
    testpack.dump()
    print(testpack.contents)                    # Test dump method
    testpack2 = testpack
    if not testpack == testpack2:
        print("Method __eq__ failed")
    print(testpack)

test_backpack()

# Inherit from the Backpack class in the class definition.
class Jetpack(Backpack):
    """A Jetpack object class. Inherits from the Backpack class.
    A Jetpack is smaller than a backpack but has a fuel tank.
    Attributes:
        name (str): the name of the knapsack's owner.
        color (str): the color of the knapsack.
        max_size (int): the maximum number of items that can fit inside.
        fuel (float): amount of fuel in the fuel tank.
    """
    def __init__(self, name, color, max_size = 2, fuel = 10.0):
        """Use the Backpack constructor to initialize the name, color,
        and max_size attributes. A Jetpack only holds 2 item by default.
        Then initialize the amount of fuel in the fuel tank, which is 10 by default
        Parameters:
            name (str): the name of the Jetpack's owner.
            color (str): the color of the Jetpack.
            max_size (int): the maximum number of items that can fit inside.
            fuel (float): the amount of fuel in the fuel tank
        """
        Backpack.__init__(self, name, color, max_size)
        self.fuel = fuel
        self.closed = True
    def fly(self, fuel_amount):            # Define the fly method.
        """decrement fuel by fuel_amount if the latter is less than or equal
        to fuel, otherwise don't and print out that there is not enough fuel"""
        if fuel_amount <= self.fuel:
            self.fuel = self.fuel - fuel_amount
        else:
            print("Not enough fuel!")
    def dump(self):                        # override the dump methon.
        """Empty jetPack's contents and fuel tank"""
        self.contents = []
        self.fuel = 0

def test_jetpack():
    print("Test Jetpack")
    print("============")
    testjetpack = Jetpack("Boing", "black")       # Instantiate the object.
    if testjetpack.name != "Boing":                  # Test an attribute.
        print("Jetpack.name assigned incorrectly")
    if testjetpack.color != "black":
        print("Jetpack.color assigned incorrectly")
    if testjetpack.fuel != 10:
        print("Jetpack.fuel assigned incorrectly")
    testjetpack.fly(5)
    if testjetpack.fuel != 5:
        print("Jetpack.fuel not decreased by fly")
    testjetpack.fly(10)
    if testjetpack.fuel != 5:
        print("Jetpack.fuel ")
    testjetpack.dump()
    print(testjetpack.contents)                    # Test dump method

print("")
test_jetpack()
