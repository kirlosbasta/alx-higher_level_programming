#!/usr/bin/python3
'''Test for Rectangle class attribute'''
from models.square import Square
from models.base import Base
from unittest.mock import patch
import unittest
import io
import sys


class TestSquare(unittest.TestCase):
    '''Tests for Square class attribute'''

    def setUp(self):
        Base._Base__nb_objects = 0

    def tearDown(self):
        pass

    def test_no_arg(self):
        with self.assertRaises(TypeError) as e:
            r1 = Square()
            self.assertEqual(str(e.exception), 'Square() takes 1 positional argument\
                but 0 were given')
            
    def test_no_x_or_y_or_id(self):
        r1 = Square(10)
        self.assertEqual(r1.size, 10)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 1)

    def test_no_id(self):
        r2 = Square(10, 2, 3, 4)
        self.assertEqual(r2.size, 10)
        self.assertEqual(r2.x, 2)
        self.assertEqual(r2.y, 3)
        self.assertEqual(r2.id, 4)

    def test_all(self):
        r3 = Square(10, 0, 0, 12)
        self.assertEqual(r3.size, 10)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)
        self.assertEqual(r3.id, 12)

    def test_validation_size(self):
        '''test the width validation for type'''
        with self.assertRaises(TypeError) as e:
            r1 = Square('3')
            self.assertEqual(str(e.exception), 'width must be an integer')

    def test_validation_x(self):
        '''test the x validation for type'''
        with self.assertRaises(TypeError) as e:
            r1 = Square(3, '2', 8)
            self.assertEqual(str(e.exception), 'x must be an integer')

    def test_validation_y(self):
        '''test the y validation for type'''
        with self.assertRaises(TypeError) as e:
            r1 = Square(3, 8, '1')
            self.assertEqual(str(e.exception), 'y must be an integer')

    def test_value_validation_size(self):
        '''test the values'''
        with self.assertRaises(ValueError) as e:
            r1 = Square(-1)
            self.assertEqual(str(e.exception), 'width must be > 0')

    def test_value_validation_x(self):
        '''test the values'''
        with self.assertRaises(ValueError) as e:
            r1 = Square(3, -2, 0)
            self.assertEqual(str(e.exception), 'x must be >= 0')

    def test_value_validation_y(self):
        '''test the values'''
        with self.assertRaises(ValueError) as e:
            r1 = Square(3, 9, -2)
            self.assertEqual(str(e.exception), 'y must be >= 0')

    def test_area(self):
        '''test the area of rectangle'''
        r1 = Square(3)
        r2 = Square(2)
        r3 = Square(7, 0, 0, 40)
        self.assertEqual(r1.area(), 9)
        self.assertEqual(r2.area(), 4)
        self.assertEqual(r3.area(), 49)

    def test_area_arg(self):
        '''pass some arg to area'''
        r1 = Square(3)
        with self.assertRaises(TypeError) as e:
            r1.area(r1.height)
            msg = 'Square.area() takes 1 positional argument\
                but 2 were given'
            self.assertEqual(str(e.exception), msg)

    def test_display_arg(self):
        '''test the argument of display'''
        r1 = Square(3)
        with self.assertRaises(TypeError) as e:
            r1.area(r1.height)
            msg = 'Square.display() takes 1 positional argument\
                but 2 were given'
            self.assertEqual(str(e.exception), msg)

    def test_display(self):
        '''test display'''
        r1 = Square(4)
        res = '''####
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
        r1 = Square(2)
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
        r1 = Square(1)
        res = '''#\n'''
        acutal = io.StringIO()
        with patch('sys.stdout', new=acutal) as out:
            r1.display()
        self.assertEqual(acutal.getvalue(), res)

    def test__str_(self):
        '''check the repersentaion of Rectangle'''
        r1 = Square(3)
        r2 = Square(4, 2, 1, 12)
        res_1 = '[Square] (1) 0/0 - 3'
        res_2 = '[Square] (12) 2/1 - 4'
        self.assertEqual(str(r1), res_1)
        self.assertEqual(str(r2), res_2)

    def test_display_x_y(self):
        '''test display'''
        r1 = Square(2, 1, 3)
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
        r1 = Square(2, 3)
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
        r1 = Square(10, 10, 10)
        res = '[Square] (1) 10/10 - 10'
        self.assertEqual(str(r1), res)
        r1.update()
        res = '[Square] (1) 10/10 - 10'
        self.assertEqual(str(r1), res)

    def test_update_1(self):
        '''test update with 1 args'''
        r1 = Square(10, 10, 10)
        res = '[Square] (1) 10/10 - 10'
        self.assertEqual(str(r1), res)
        r1.update(89)
        res = '[Square] (89) 10/10 - 10'
        self.assertEqual(str(r1), res)

    def test_update_2(self):
        '''test update with 2 args'''
        r1 = Square(10, 10, 10)
        res = '[Square] (1) 10/10 - 10'
        self.assertEqual(str(r1), res)
        r1.update(89, 2)
        res = '[Square] (89) 10/10 - 2'
        self.assertEqual(str(r1), res)

    def test_update_3(self):
        '''test update with 3 args'''
        r1 = Square(10, 10, 10)
        res = '[Square] (1) 10/10 - 10'
        self.assertEqual(str(r1), res)
        r1.update(89, 2, 3)
        res = '[Square] (89) 3/10 - 2'
        self.assertEqual(str(r1), res)

    def test_update_4(self):
        '''test update with 4 args'''
        r1 = Square(10, 10, 10)
        res = '[Square] (1) 10/10 - 10'
        self.assertEqual(str(r1), res)
        r1.update(89, 2, 3, 4)
        res = '[Square] (89) 3/4 - 2'
        self.assertEqual(str(r1), res)

    def test_update_5(self):
        '''test update with 5 args'''
        r1 = Square(10, 10, 10)
        res = '[Square] (1) 10/10 - 10'
        self.assertEqual(str(r1), res)
        r1.update(89, 2, 3, 4, 5)
        res = '[Square] (89) 3/4 - 2'
        self.assertEqual(str(r1), res)

    def test_update_6(self):
        '''test update with 1 kwargs'''
        r1 = Square(10, 10, 10)
        res = '[Square] (1) 10/10 - 10'
        self.assertEqual(str(r1), res)
        r1.update(size=1)
        res = '[Square] (1) 10/10 - 1'
        self.assertEqual(str(r1), res)

    def test_update_8(self):
        '''test update with 2 kwargs'''
        r1 = Square(10, 10, 10)
        res = '[Square] (1) 10/10 - 10'
        self.assertEqual(str(r1), res)
        r1.update(size=1, x=2)
        res = '[Square] (1) 2/10 - 1'
        self.assertEqual(str(r1), res)

    def test_update_9(self):
        '''test update with all kwargs'''
        r1 = Square(10, 10, 10)
        res = '[Square] (1) 10/10 - 10'
        self.assertEqual(str(r1), res)
        r1.update(x=1, y=3, size=4, id=89)
        res = '[Square] (89) 1/3 - 4'
        self.assertEqual(str(r1), res)

    def test_update_10(self):
        '''test update with all kwargs'''
        r1 = Square(10, 10, 10)
        res = '[Square] (1) 10/10 - 10'
        self.assertEqual(str(r1), res)
        r1.update(x=1, y=3, size=4, id=89, fake=8)
        res = '[Square] (89) 1/3 - 4'
        self.assertEqual(str(r1), res)

    def test_update_11(self):
        '''test update with mix kwargs and args'''
        r1 = Square(10, 10, 10)
        res = '[Square] (1) 10/10 - 10'
        self.assertEqual(str(r1), res)
        r1.update(89, x=1, size=2, y=3, width=4, id=89)
        res = '[Square] (89) 10/10 - 10'
        self.assertEqual(str(r1), res)

    def test_to_dictionary(self):
        '''test to_dictionary function'''
        r1 = Square(10, 2, 1)
        res = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertEqual(r1.to_dictionary(), res)

    def test_to_rectangle(self):
        '''test to_dictionary function'''
        r1 = Square(10, 2, 1, 9)
        self.assertIsInstance(r1.to_dictionary(), dict)

    


if __name__ == '__main__':
    unittest.main()
