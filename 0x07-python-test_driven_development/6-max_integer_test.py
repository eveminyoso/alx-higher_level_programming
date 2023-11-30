#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxIntegerFunction(unittest.TestCase):

    def test_regular_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -5, -2, -8]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-1, 5, 2, -8]), 5)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_single_element_list(self):
        self.assertEqual(max_integer([42]), 42)

    def test_float_numbers(self):
        self.assertEqual(max_integer([1.5, 2.5, 1.0, 0.5]), 2.5)

    def test_strings(self):
        self.assertEqual(max_integer(["apple", "banana", "orange"]), "orange")

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            max_integer([1, "two", 3])

if __name__ == '__main__':
    unittest.main()
