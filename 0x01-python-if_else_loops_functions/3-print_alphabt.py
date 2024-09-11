#!/usr/bin/python3  # Shebang to specify Python interpreter

# Print the alphabet excluding 'q' and 'e', without a newline at the end
print("".join("{:c}".format(letter) for letter in range(97, 123) if letter not in (ord('q'), ord('e'))), end="")

