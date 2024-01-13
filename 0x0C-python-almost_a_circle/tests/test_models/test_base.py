#!/usr/bin/python3
'''Test the base class'''
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    '''Test the base class'''

    def setUp(self):
        Base._Base__nb_objects = 0
        pass

    def tearDown(self):
        pass

    def test_no_id(self):
        '''test with no id multiple times'''
        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base()
        self.b4 = Base(12)
        self.b5 = Base()

        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 3)
        self.assertEqual(self.b4.id, 12)
        self.assertEqual(self.b5.id, 4)

    def test_private(self):
        '''check if _nb_objects is private'''

        with self.assertRaises(AttributeError):
            print(self.__nb_objects)

    def test_to_json(self):
        '''test to json'''
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        res = '[{"x": 2, "y": 8, "id": 1, "height": 7, "width": 10}]'
        self.assertEqual(type(json_dictionary), str)
        self.assertEqual(type(dictionary), dict)
        self.assertEqual(json_dictionary, res)

    def test_to_json_empty(self):
        '''test to json'''
        json_dictionary = Base.to_json_string([])
        self.assertEqual(json_dictionary, "[]")

    def test_to_json_None(self):
        '''test to json'''
        json_dictionary = Base.to_json_string(None)
        self.assertEqual(json_dictionary, "[]")


if __name__ == '__main__':
    unittest.main()
