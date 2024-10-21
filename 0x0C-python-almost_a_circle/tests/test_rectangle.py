#!/usr/bin/python3
"""This module tests the Rectangle class."""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """This tests the Rectangle class."""

    def test_rectangle_initialization(self):
        """This tests initialization."""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_rectangle_attributes(self):
        """This tests attributes."""
        r = Rectangle(10, 2, 5, 5)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 5)

    def test_setters(self):
        """This tests setters."""
        r = Rectangle(10, 2)
        r.width = 15
        r.height = 3
        self.assertEqual(r.width, 15)
        self.assertEqual(r.height, 3)

        r.x = 10
        r.y = 4
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 4)


if __name__ == "__main__":
    unittest.main()
