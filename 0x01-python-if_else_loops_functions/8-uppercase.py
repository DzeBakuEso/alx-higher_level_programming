#!/usr/bin/python3  # Shebang to specify Python interpreter

def uppercase(str):
    """Prints the string in uppercase."""
    for char in str:
        # Convert lowercase letters to uppercase
        if 'a' <= char <= 'z':
            # Convert to uppercase by subtracting 32 from ASCII value
            print(chr(ord(char) - 32), end='')
        else:
            print(char, end='')
    print()  # Print newline at the end

