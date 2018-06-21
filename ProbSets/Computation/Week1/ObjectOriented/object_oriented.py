class Backpack:
    """A Backpack object class. Has a name and a list of contents.
    Attributes:
        name (str): the name of the backpack's owner.
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
        self.contents.append(item)  # Use 'self.contents', not just 'contents'.
    def take(self, item):
        """Remove 'item' from the backpack's list of contents."""
        self.contents.remove(item)
