#!/usr/bin/python3
'''Test max_integer module'''
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxClass(unittest.TestCase):
    '''Test case class'''

    def test_max_integer(self):
        self.assertAlmostEqual(max_integer([1, 8, 3, 5]), 8)
        self.assertAlmostEqual(max_integer([6, 10, 60, -70]), 60)
        self.assertAlmostEqual(max_integer([40.4, 32, 12, 0.5]), 40.4)
    
    def test_assert(self):
        self.assertRaises(TypeError, max_integer, [2, '3', 34, 3])
        self.assertRaises(TypeError, max_integer, 78)
        self.assertRaises(KeyError, max_integer, {'name': 23, 'no': 3})
        self.assertRaises(TypeError, max_integer, [3, 5, 6j, 4e6])

