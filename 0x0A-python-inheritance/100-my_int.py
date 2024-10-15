#!/usr/bin/python3
"""A class that inherits from int with inverted equality operators."""


class MyInt(int):
    """A rebel integer class with inverted == and != operators."""

    def __eq__(self, other):
        """Inverts the behavior of the equality operator."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Inverts the behavior of the not-equal operator."""
        return super().__eq__(other)
