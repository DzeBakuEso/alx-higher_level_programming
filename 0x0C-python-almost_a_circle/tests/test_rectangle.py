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

    def test_area(self):
        """This tests the area method."""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test_invalid_width(self):
        """This tests invalid width."""
        with self.assertRaises(TypeError) as e:
            Rectangle("10", 2)
        self.assertEqual(str(e.exception), "width must be an integer")

        r = Rectangle(10, 2)
        with self.assertRaises(ValueError) as e:
            r.width = -10
        self.assertEqual(str(e.exception), "width must be > 0")

    def test_invalid_height(self):
        """This tests invalid height."""
        with self.assertRaises(TypeError) as e:
            Rectangle(10, "2")
        self.assertEqual(str(e.exception), "height must be an integer")

        r = Rectangle(10, 2)
        with self.assertRaises(ValueError) as e:
            r.height = 0
        self.assertEqual(str(e.exception), "height must be > 0")

    def test_invalid_x(self):
        """This tests invalid x."""
        r = Rectangle(10, 2)
        with self.assertRaises(TypeError) as e:
            r.x = {}
        self.assertEqual(str(e.exception), "x must be an integer")

        with self.assertRaises(ValueError) as e:
            Rectangle(10, 2, -1)
        self.assertEqual(str(e.exception), "x must be >= 0")

    def test_invalid_y(self):
        """This tests invalid y."""
        r = Rectangle(10, 2)
        with self.assertRaises(TypeError) as e:
            r.y = []
        self.assertEqual(str(e.exception), "y must be an integer")

        with self.assertRaises(ValueError) as e:
            Rectangle(10, 2, 0, -1)
        self.assertEqual(str(e.exception), "y must be >= 0")


if __name__ == "__main__":
    unittest.main()
