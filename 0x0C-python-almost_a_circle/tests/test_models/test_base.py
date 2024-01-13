#!/usr/bin/python3
'''Test the base class'''
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


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

    def test_save_to_file(self):
        '''test save to file'''
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_r = [r1, r2]
        Rectangle.save_to_file(list_r)
        with open("Rectangle.json", "r") as file:
            acutal = file.read()
            res = '[{"y": 8, "x": 2, "id": 1, "width": 10, "height": 7},\
 {"y": 0, "x": 0, "id": 2, "width": 2, "height": 4}]'
            self.assertEqual(len(acutal), len(res))

    def test_save_emp(self):
        '''test save to file'''
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_r = []
        Rectangle.save_to_file(list_r)
        with open("Rectangle.json", "r") as file:
            acutal = file.read()
            res = '[]'
            self.assertEqual(len(acutal), len(res))

    def test_save_None(self):
        '''test save to file'''
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_r = []
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            acutal = file.read()
            res = '[]'
            self.assertEqual(len(acutal), len(res))

    def test_save_no_arg(self):
        '''test save to file'''
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        with self.assertRaises(TypeError) as e:
            Rectangle.save_to_file()
            err = "Base.save_to_file() missing 1 required positional argument: 'list_objs'"
            self.assertEqual(str(e.exception), err)

    def test_S_save_to_file(self):
        '''test save to file'''
        r1 = Square(10, 2, 8)
        r2 = Square(2, 4)
        list_r = [r1, r2]
        Square.save_to_file(list_r)
        with open("Square.json", "r") as file:
            acutal = file.read()
            res = '[{"y": 8, "x": 2, "id": 1, "size": 10},\
 {"y": 0, "x": 0, "id": 2, "size": 2}]'
            self.assertEqual(len(acutal), len(res))

    def test_save_emp_S(self):
        '''test save to file'''
        r1 = Square(10, 2, 8)
        r2 = Square(2, 4)
        list_r = []
        Square.save_to_file(list_r)
        with open("Square.json", "r") as file:
            acutal = file.read()
            res = '[]'
            self.assertEqual(len(acutal), len(res))

    def test_save_None_S(self):
        '''test save to file'''
        r1 = Square(10, 7, 2, 8)
        r2 = Square(2, 4)
        list_r = []
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            acutal = file.read()
            res = '[]'
            self.assertEqual(len(acutal), len(res))

    def test_save_no_arg_S(self):
        '''test save to file'''
        r1 = Square(10, 7, 2, 8)
        r2 = Square(2, 4)
        with self.assertRaises(TypeError) as e:
            Square.save_to_file()
            err = "Base.save_to_file() missing 1 required positional argument: 'list_objs'"
            self.assertEqual(str(e.exception), err)


if __name__ == '__main__':
    unittest.main()
