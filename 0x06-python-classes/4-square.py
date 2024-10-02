class Square:
    """
    A class that defines a square by its size.
    Attributes:
        __size (int): The size of the square (private attribute).
    """

    def __init__(self, size=0):
        """
        Initializes the square with an optional size.
        Args:
            size (int): The size of the square, defaults to 0.
        """
        self.size = size  # This triggers the setter for validation

    @property
    def size(self):
        """
        Getter method to retrieve the size of the square.
        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size of the square with validation.
        Args:
            value (int): The new size of the square.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.
        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
