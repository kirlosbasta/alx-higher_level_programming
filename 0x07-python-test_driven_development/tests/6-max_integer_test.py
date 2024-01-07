#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests for max_integer function"""

    def test_normal(self):
        """test the normal case scenario"""
        list_1 = [1, 2, 3, 4]
        list_2 = [1, 3, 4, 2]

        self.assertEqual(max_integer(list_1), 4)
        self.assertEqual(max_integer(list_2), 4)

    def test_negative(self):
        """test the negative case scenario"""
        list_1 = [-1, -2, 3, -4]
        list_2 = [-1, -3, -4, -2]

        self.assertEqual(max_integer(list_1), 3)
        self.assertEqual(max_integer(list_2), -1)

    def test_float(self):
        """test for float"""
        list_1 = [1.3, 2.1, 3.2, 1.2]
        self.assertEqual(max_integer(list_1), 3.2)

    def test_one(self):
        """test one item list"""
        list_1 = [4]
        self.assertEqual(max_integer(list_1), 4)

    def test_empty(self):
        """test empty list"""

        list_1 = []
        self.assertIsNone(max_integer(list_1))

    def test_none(self):
        """Tests for passing none as argument"""
        with self.assertRaises(TypeError):
            max_integer(None)


if __name__ == '__main__':
    unittest.main()
