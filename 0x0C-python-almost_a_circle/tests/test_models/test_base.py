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
        err = "save_to_file() missing 1 required positional\
 argument: 'list_objs'"
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
        err = "save_to_file() missing 1 required positional\
 argument: 'list_objs'"
        self.assertEqual(str(e.exception), err)

    def test_from_json_no_arg(self):
        '''test from_json_string with no arg'''
        with self.assertRaises(TypeError) as e:
            Base.from_json_string()
        err = "from_json_string() missing 1 required\
 positional argument: 'json_string'"
        self.assertEqual(str(e.exception), err)

    def test_from_json_emp(self):
        '''test from_json_string with empty string'''
        obj = Base.from_json_string('')
        self.assertEqual(obj, [])

    def test_from_json_None(self):
        '''test from_json_string with None'''
        obj = Base.from_json_string(None)
        self.assertEqual(obj, [])

    def test_from_json_2_arg(self):
        '''test from_json_string with 2 arg'''
        with self.assertRaises(TypeError) as e:
            Base.from_json_string('fdfd', 'fdfdfd')
        err = "from_json_string() takes 1 positional\
 argument but 2 were given"
        self.assertEqual(str(e.exception), err)

    def test_form_json(self):
        '''test from json normal json string'''
        list_input = [{'id': 89, 'width': 10, 'height': 4},
                      {'id': 7, 'width': 1, 'height': 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        acutal = '''[{"height": 4, "width": 10, "id": 89},
{"height": 7, "width": 1, "id": 7}]'''
        self.assertIsInstance(json_list_input, str)
        self.assertIsInstance(list_output, list)
        self.assertEqual(list_input, list_output)
        self.assertEqual(len(acutal), len(json_list_input))

    def test_wrong_input(self):
        '''give object other that str to from_json_string'''
        input_str = ([5, 3, 2], "string fake")
        with self.assertRaises(TypeError) as e:
            Rectangle.from_json_string(input_str)
        err = "the JSON object must be str, bytes or bytearray, not tuple"
        self.assertEqual(str(e.exception), err)

    def test_create(self):
        '''test create function'''
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        r2_dictionary = r2.to_dictionary()
        self.assertEqual(r1_dictionary, r2_dictionary)

    def test_create_s(self):
        '''test create function'''
        r1 = Square(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Square.create(**r1_dictionary)
        r2_dictionary = r2.to_dictionary()
        self.assertEqual(r1_dictionary, r2_dictionary)

    def test_create_type(self):
        '''check the type'''
        r1 = Square(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Square.create(**r1_dictionary)
        self.assertEqual(type(r1), type(r2))

    def test_file_exist(self):
        '''check the output if file doesn't exist'''
        fil = Base.load_from_file()
        self.assertEqual(fil, [])

    def test_load(self):
        '''test the normal'''
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(len(list_rectangles_input),
                         len(list_rectangles_output))
        for i in range(len(list_rectangles_input)):
            self.assertEqual(list_rectangles_input[i].to_dictionary(),
                             list_rectangles_output[i].to_dictionary())

    def test_load_s(self):
        '''test the normal'''
        r1 = Square(10, 7, 2)
        r2 = Square(2)
        list_rectangles_input = [r1, r2]
        Square.save_to_file(list_rectangles_input)
        list_rectangles_output = Square.load_from_file()
        self.assertEqual(len(list_rectangles_input),
                         len(list_rectangles_output))
        for i in range(len(list_rectangles_input)):
            self.assertEqual(list_rectangles_input[i].to_dictionary(),
                             list_rectangles_output[i].to_dictionary())

    def test_load_csv(self):
        '''test load_to_csv'''
        import csv
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file_csv(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(len(list_rectangles_input),
                         len(list_rectangles_output))
        for i in range(len(list_rectangles_input)):
            self.assertEqual(str(list_rectangles_input[i]),
                             str(list_rectangles_output[i]))

    def test_load_csv_s(self):
        '''test load_to_csv'''
        import csv
        r1 = Square(10, 7, 2, 8)
        r2 = Square(2, 4)
        list_rectangles_input = [r1, r2]
        Square.save_to_file_csv(list_rectangles_input)
        list_rectangles_output = Square.load_from_file_csv()
        self.assertEqual(len(list_rectangles_input),
                         len(list_rectangles_output))
        for i in range(len(list_rectangles_input)):
            self.assertEqual(str(list_rectangles_input[i]),
                             str(list_rectangles_output[i]))


if __name__ == '__main__':
    unittest.main()
