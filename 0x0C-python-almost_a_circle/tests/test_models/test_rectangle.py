#!/usr/bin/python3
'''Test for Rectangle class attribute'''
from models.rectangle import Rectangle
from models.base import Base
from unittest.mock import patch
import unittest
import io
import sys


class TestRectangle(unittest.TestCase):
    '''Test for Rectangle class attribute'''

    def setUp(self):
        Base._Base__nb_objects = 0

    def tearDown(self):
        pass

    def test_no_arg(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle()

    def test_arg_1(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(2)

    def test_no_x_or_y_or_id(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 1)

    def test_no_id(self):
        r2 = Rectangle(10, 2, 3, 4)
        self.assertEqual(r2.width, 10)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r2.y, 4)
        self.assertEqual(r2.id, 1)

    def test_all(self):
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)
        self.assertEqual(r3.id, 12)

    def test_validation_width(self):
        '''test the width validation for type'''
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle('3', 4)
            self.assertEqual(str(e.exception), 'width must be an integer')

    def test_validation_height(self):
        '''test the height validation for type'''
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(3, '4')
            self.assertEqual(str(e.exception), 'height must be an integer')

    def test_validation_x(self):
        '''test the x validation for type'''
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(3, 8, '2', 8)
            self.assertEqual(str(e.exception), 'x must be an integer')

    def test_validation_y(self):
        '''test the y validation for type'''
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(3, 2, 8, '1')
            self.assertEqual(str(e.exception), 'y must be an integer')

    def test_value_validation_width(self):
        '''test the values'''
        with self.assertRaises(ValueError) as e:
            r1 = Rectangle(-1, 2)
            self.assertEqual(str(e.exception), 'width must be > 0')

    def test_value_validation_height(self):
        '''test the values'''
        with self.assertRaises(ValueError) as e:
            r1 = Rectangle(3, -2)
            self.assertEqual(str(e.exception), 'height must be > 0')

    def test_value_validation_x(self):
        '''test the values'''
        with self.assertRaises(ValueError) as e:
            r1 = Rectangle(3, 5, -2, 0)
            self.assertEqual(str(e.exception), 'x must be >= 0')

    def test_value_validation_y(self):
        '''test the values'''
        with self.assertRaises(ValueError) as e:
            r1 = Rectangle(3, 5, 9, -2)
            self.assertEqual(str(e.exception), 'y must be >= 0')

    def test_area(self):
        '''test the area of rectangle'''
        r1 = Rectangle(3, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(7, 5, 0, 0, 40)
        self.assertEqual(r1.area(), 6)
        self.assertEqual(r2.area(), 20)
        self.assertEqual(r3.area(), 35)

    def test_area_arg(self):
        '''pass some arg to area'''
        r1 = Rectangle(3, 2)
        with self.assertRaises(TypeError) as e:
            r1.area(r1.height)
            msg = 'Rectangle.area() takes 1 positional argument\
                but 2 were given'
            self.assertEqual(str(e.exception), msg)

    def test_display_arg(self):
        '''test the argument of display'''
        r1 = Rectangle(3, 2)
        with self.assertRaises(TypeError) as e:
            r1.area(r1.height)
            msg = 'Rectangle.display() takes 1 positional argument\
                but 2 were given'
            self.assertEqual(str(e.exception), msg)

    def test_display(self):
        '''test display'''
        r1 = Rectangle(4, 6)
        res = '''####
####
####
####
####
####
'''
        acutal = io.StringIO()
        with patch('sys.stdout', new=acutal) as out:
            r1.display()
        self.assertEqual(acutal.getvalue(), res)

    def test_display_2(self):
        '''test display'''
        r1 = Rectangle(2, 2)
        res = '''\
##
##
'''
        acutal = io.StringIO()
        with patch('sys.stdout', new=acutal) as out:
            r1.display()
        self.assertEqual(acutal.getvalue(), res)

    def test_display_3(self):
        '''test display'''
        r1 = Rectangle(1, 1)
        res = '''#\n'''
        acutal = io.StringIO()
        with patch('sys.stdout', new=acutal) as out:
            r1.display()
        self.assertEqual(acutal.getvalue(), res)

    def test__str_(self):
        '''check the repersentaion of Rectangle'''
        r1 = Rectangle(3, 5)
        r2 = Rectangle(4, 6, 2, 1, 12)
        res_1 = '[Rectangle] (1) 0/0 - 3/5'
        res_2 = '[Rectangle] (12) 2/1 - 4/6'
        self.assertEqual(str(r1), res_1)
        self.assertEqual(str(r2), res_2)

    def test_display_x_y(self):
        '''test display'''
        r1 = Rectangle(2, 2, 1, 3)
        res = '''\n\n
 ##
 ##
'''
        acutal = io.StringIO()
        with patch('sys.stdout', new=acutal) as out:
            r1.display()
        self.assertEqual(acutal.getvalue(), res)

    def test_display_x(self):
        '''test display'''
        r1 = Rectangle(2, 2, 3)
        res = '''\
   ##
   ##
'''
        acutal = io.StringIO()
        with patch('sys.stdout', new=acutal) as out:
            r1.display()
        self.assertEqual(acutal.getvalue(), res)

    def test_update_1(self):
        '''test update with no args'''
        r1 = Rectangle(10, 10, 10, 10)
        res = '[Rectangle] (1) 10/10 - 10/10'
        self.assertEqual(str(r1), res)
        r1.update()
        res = '[Rectangle] (1) 10/10 - 10/10'
        self.assertEqual(str(r1), res)

    def test_update_1(self):
        '''test update with 1 args'''
        r1 = Rectangle(10, 10, 10, 10)
        res = '[Rectangle] (1) 10/10 - 10/10'
        self.assertEqual(str(r1), res)
        r1.update(89)
        res = '[Rectangle] (89) 10/10 - 10/10'
        self.assertEqual(str(r1), res)

    def test_update_2(self):
        '''test update with 2 args'''
        r1 = Rectangle(10, 10, 10, 10)
        res = '[Rectangle] (1) 10/10 - 10/10'
        self.assertEqual(str(r1), res)
        r1.update(89, 2)
        res = '[Rectangle] (89) 10/10 - 2/10'
        self.assertEqual(str(r1), res)

    def test_update_3(self):
        '''test update with 3 args'''
        r1 = Rectangle(10, 10, 10, 10)
        res = '[Rectangle] (1) 10/10 - 10/10'
        self.assertEqual(str(r1), res)
        r1.update(89, 2, 3)
        res = '[Rectangle] (89) 10/10 - 2/3'
        self.assertEqual(str(r1), res)

    def test_update_4(self):
        '''test update with 4 args'''
        r1 = Rectangle(10, 10, 10, 10)
        res = '[Rectangle] (1) 10/10 - 10/10'
        self.assertEqual(str(r1), res)
        r1.update(89, 2, 3, 4)
        res = '[Rectangle] (89) 4/10 - 2/3'
        self.assertEqual(str(r1), res)

    def test_update_5(self):
        '''test update with 5 args'''
        r1 = Rectangle(10, 10, 10, 10)
        res = '[Rectangle] (1) 10/10 - 10/10'
        self.assertEqual(str(r1), res)
        r1.update(89, 2, 3, 4, 5)
        res = '[Rectangle] (89) 4/5 - 2/3'
        self.assertEqual(str(r1), res)

    def test_update_6(self):
        '''test update with 6 args'''
        r1 = Rectangle(10, 10, 10, 10)
        res = '[Rectangle] (1) 10/10 - 10/10'
        self.assertEqual(str(r1), res)
        r1.update(89, 2, 3, 4, 5, 6)
        res = '[Rectangle] (89) 4/5 - 2/3'
        self.assertEqual(str(r1), res)

    def test_update_7(self):
        '''test update with 1 kwargs'''
        r1 = Rectangle(10, 10, 10, 10)
        res = '[Rectangle] (1) 10/10 - 10/10'
        self.assertEqual(str(r1), res)
        r1.update(height=1)
        res = '[Rectangle] (1) 10/10 - 10/1'
        self.assertEqual(str(r1), res)

    def test_update_8(self):
        '''test update with 2 kwargs'''
        r1 = Rectangle(10, 10, 10, 10)
        res = '[Rectangle] (1) 10/10 - 10/10'
        self.assertEqual(str(r1), res)
        r1.update(height=1, width=1, x=2)
        res = '[Rectangle] (1) 2/10 - 1/1'
        self.assertEqual(str(r1), res)

    def test_update_9(self):
        '''test update with all kwargs'''
        r1 = Rectangle(10, 10, 10, 10)
        res = '[Rectangle] (1) 10/10 - 10/10'
        self.assertEqual(str(r1), res)
        r1.update(x=1, height=2, y=3, width=4, id=89)
        res = '[Rectangle] (89) 1/3 - 4/2'
        self.assertEqual(str(r1), res)

    def test_update_10(self):
        '''test update with all kwargs'''
        r1 = Rectangle(10, 10, 10, 10)
        res = '[Rectangle] (1) 10/10 - 10/10'
        self.assertEqual(str(r1), res)
        r1.update(x=1, height=2, y=3, width=4, id=89, fake=8)
        res = '[Rectangle] (89) 1/3 - 4/2'
        self.assertEqual(str(r1), res)

    def test_update_11(self):
        '''test update with mix kwargs and args'''
        r1 = Rectangle(10, 10, 10, 10)
        res = '[Rectangle] (1) 10/10 - 10/10'
        self.assertEqual(str(r1), res)
        r1.update(89, x=1, height=2, y=3, width=4, id=89)
        res = '[Rectangle] (89) 10/10 - 10/10'
        self.assertEqual(str(r1), res)

    def test_to_dictionary(self):
        '''test to_dictionary function'''
        r1 = Rectangle(10, 2, 1, 9)
        res = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertEqual(sorted(r1.to_dictionary()), sorted(res))

    def test_to_dictionary_type(self):
        '''test to_dictionary function'''
        r1 = Rectangle(10, 2, 1, 9)
        self.assertIsInstance(r1.to_dictionary(), dict)


if __name__ == '__main__':
    unittest.main()
