def read_file(filename=""):

    """
    This defines a function that reads a text file (UTF8)
    and prints its content to stdout.
    """
    with open("my_file_0.txt", 'r', encoding='utf-8') as file:
        """
        This uses 'with' to open the file safely and
        print the content to stdout.
        """
        print(file.read(), end="")
