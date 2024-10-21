import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """This is Test cases for the Base class"""

    def setUp(self):
        """Method called to prepare the test fixture.
        It resets the __nb_objects before every test.
        """
        Base._Base__nb_objects = 0

    def test_id_autoincrement(self):
        """This is to test that the ID is auto-incrementing properly"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_custom_id(self):
        """This is to test that a custom ID is assigned correctly"""
        b4 = Base(12)
        self.assertEqual(b4.id, 12)

    def test_id_increment_after_custom(self):
        """This is to test that the auto-increment continues after a custom ID"""
        b5 = Base()
        self.assertEqual(b5.id, 1)
        b6 = Base(7)
        self.assertEqual(b6.id, 7)
        b7 = Base()
        self.assertEqual(b7.id, 2)

if __name__ == '__main__':
    unittest.main()
