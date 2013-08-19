#!/usr/bin/python
# -*- coding: utf-8 -*-

import calculator
import sys
import unittest

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.c = calculator.simple.SimpleCalculator()

    def test_addition(self):
        self.c.c()
        self.c.run('1 + 1')
        self.assertEqual(self.c.h[-1], 'result: 2.0')

    def test_subtraction(self):
        self.c.c()
        self.c.run('1 - 2')
        self.assertEqual(self.c.h[-1], 'result: -1.0')

    def test_multiplication(self):
        self.c.c()
        self.c.run('1 * 1')
        self.assertEqual(self.c.h[-1], 'result: 1.0')

    def test_division(self):
        self.c.c()
        self.c.run('1 / 1')
        self.assertEqual(self.c.h[-1], 'result: 1.0')

    def test_division_by_zero(self):
        self.c.c()
        self.c.run('1 / 0')
        self.assertNotEqual(self.c.h[-1], 'result: 1.0')

if __name__ == '__main__':
    unittest.main()
