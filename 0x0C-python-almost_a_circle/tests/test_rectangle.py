#!/usr/bin/python3
import unittest

from models.rectangle import Rectangle


class TestRectangleUpdate(unittest.TestCase):
    """This class tests the update method of the Rectangle class."""

    def setUp(self):
        """This sets up the test environment."""
        self.r1 = Rectangle(10, 10, 10, 10)

    def test_update_with_args(self):
        """This tests update with *args."""
        self.r1.update(89, 2, 3, 4, 5)
        self.assertEqual(self.r1.id, 89)
        self.assertEqual(self.r1.width, 2)
        self.assertEqual(self.r1.height, 3)
        self.assertEqual(self.r1.x, 4)
        self.assertEqual(self.r1.y, 5)

    def test_update_with_partial_args(self):
        """This tests update with partial *args."""
        self.r1.update(89, 2)
        self.assertEqual(self.r1.id, 89)
        self.assertEqual(self.r1.width, 2)
        self.assertEqual(self.r1.height, 10)  # Unchanged
        self.assertEqual(self.r1.x, 10)       # Unchanged
        self.assertEqual(self.r1.y, 10)       # Unchanged

    def test_update_with_kwargs(self):
        """This tests update with **kwargs."""
        self.r1.update(height=1)
        self.assertEqual(self.r1.height, 1)
        self.r1.update(width=1, x=2)
        self.assertEqual(self.r1.width, 1)
        self.assertEqual(self.r1.x, 2)
        self.assertEqual(self.r1.y, 10)  # Unchanged

    def test_update_with_kwargs_and_args(self):
        """This tests update when both *args and **kwargs are present."""
        # *args should take precedence, so kwargs will be ignored
        self.r1.update(89, 2, 3, 4, 5, width=100, height=200, x=1, y=1)
        self.assertEqual(self.r1.id, 89)
        self.assertEqual(self.r1.width, 2)  # *args takes precedence
        self.assertEqual(self.r1.height, 3)  # *args takes precedence
        self.assertEqual(self.r1.x, 4)      # *args takes precedence
        self.assertEqual(self.r1.y, 5)      # *args takes precedence

    def test_update_empty_args_kwargs(self):
        """This tests update with no args and no kwargs."""
        self.r1.update()
        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r1.height, 10)
        self.assertEqual(self.r1.x, 10)
        self.assertEqual(self.r1.y, 10)


if __name__ == '__main__':
    unittest.main()
