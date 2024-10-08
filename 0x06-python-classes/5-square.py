class Square:
    """
    A class that defines a square by its size.

    Attributes:
        size (int): The size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes the Square instance with an optional size.

        Args:
            size (int): The size of the square. Defaults to 0.
        """
        self.size = size  # Use the setter to validate size upon initial.

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value  # Set the private size attribute after vali.

    def area(self):
        """
        Returns the current area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints the square using the character '#'.

        If size is equal to 0, an empty line is printed.
        """
        if self.__size == 0:
            print()  # Print an empty line if size is 0
            return

        for _ in range(self.__size):
            print('#' * self.__size)  # Print the square
