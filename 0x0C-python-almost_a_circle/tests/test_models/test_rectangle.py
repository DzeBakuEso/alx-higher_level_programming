#!/usr/bin/python3 
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """This class contains tests for the Rectangle class."""

    def test_initialization(self):
        """This tests initialization of the Rectangle."""
        r1 = Rectangle(10, 5)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 5)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

    def test_area(self):
        """This tests the area method."""
        r2 = Rectangle(3, 4)
        self.assertEqual(r2.area(), 12)

    def test_update(self):
        """This tests the update method."""
        r3 = Rectangle(10, 10, 10, 10)
        r3.update(89, 5, 6, 7, 8)
        self.assertEqual(r3.id, 89)
        self.assertEqual(r3.width, 5)
        self.assertEqual(r3.height, 6)
        self.assertEqual(r3.x, 7)
        self.assertEqual(r3.y, 8)

    def test_invalid_width(self):
        """This tests if invalid width raises the correct exception."""
        with self.assertRaises(ValueError):
            r4 = Rectangle(-5, 10)

    def test_invalid_type(self):
        """This tests if a non-integer width raises a TypeError."""
        with self.assertRaises(TypeError):
            r5 = Rectangle("10", 10)

if __name__ == "__main__":
    unittest.main()
