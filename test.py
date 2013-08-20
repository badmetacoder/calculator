#!/usr/bin/python
# -*- coding: utf-8 -*-

import calculator
import unittest

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.c = calculator.simple.SimpleCalculator()

    def test_addition_000(self):
        self.c.c()
        self.c.run('1 + 1')
        self.assertEqual(self.c.h[-1], 'result: 2.0')

    def test_addition_001(self):
        self.c.c()
        self.c.run('1 + -1')
        self.assertEqual(self.c.h[-1], 'result: 0.0')

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

    def test_long_1(self):
        self.c.c()
        self.c.run("1 + 2 / 6 acv 1 + 1 / 33 fmod 0.01 1 2 3 4")
        self.assertEqual(self.c.h[-1], 'state ->  r1: 4.0')

if __name__ == '__main__':
    unittest.main()
