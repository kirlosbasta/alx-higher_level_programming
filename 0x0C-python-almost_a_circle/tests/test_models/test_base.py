#!/usr/bin/python3
'''Test the base class'''
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    '''Test the base class'''

    def setUp(self):
        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base()
        self.b4 = Base(12)
        self.b5 = Base()

    def test_no_id(self):
        '''test with no id multiple times'''

        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 3)
        self.assertEqual(self.b4.id, 12)
        self.assertEqual(self.b5.id, 4)

    def test_private(self):
        '''check if _nb_objects is private'''

        with self.assertRaises(AttributeError):
            print(self.__nb_objects)


if __name__ == '__main__':
    unittest.main()
