#!/usr/bin/python
# -*- coding: utf-8 -*-

import calculator
import unittest

class TestSimpleCalculatorAddition(unittest.TestCase):

    def setUp(self):
        self.c = calculator.simple.SimpleCalculator()

    def test_addition_000(self):
        self.c.clear()
        self.c.run('1 + 1')
        self.assertEqual(self.c.log[-1], 'result: 2.0')

    def test_addition_001(self):
        self.c.clear()
        self.c.run('1 + 1')
        self.assertEqual(self.c.lcd, 2.0)

    def test_addition_002(self):
        self.c.clear()
        self.c.run('1 + -1')
        self.assertEqual(self.c.log[-1], 'result: 0.0')

    def test_addition_003(self):
        self.c.clear()
        self.c.run('1 + -1')
        self.assertEqual(self.c.lcd, 0.0)

class TestSimpleCalculatorSubtraction(unittest.TestCase):

    def setUp(self):
        self.c = calculator.simple.SimpleCalculator()

    def test_subtraction_000(self):
        self.c.clear()
        self.c.run('1 - 2')
        self.assertEqual(self.c.log[-1], 'result: -1.0')

    def test_subtraction_001(self):
        self.c.clear()
        self.c.run('1 - 2')
        self.assertEqual(self.c.lcd, -1.0)

class TestSimpleCalculatorMultiplication(unittest.TestCase):

    def setUp(self):
        self.c = calculator.simple.SimpleCalculator()

    def test_multiplication_000(self):
        self.c.clear()
        self.c.run('1 * 1')
        self.assertEqual(self.c.log[-1], 'result: 1.0')

    def test_multiplication_001(self):
        self.c.clear()
        self.c.run('1 * 1')
        self.assertEqual(self.c.lcd, 1.0)

class TestSimpleCalculatorDivision(unittest.TestCase):

    def setUp(self):
        self.c = calculator.simple.SimpleCalculator()

    def test_division_000(self):
        self.c.clear()
        self.c.run('1 / 1')
        self.assertEqual(self.c.log[-1], 'result: 1.0')

    def test_division_001(self):
        self.c.clear()
        self.c.run('1 / 1')
        self.assertEqual(self.c.lcd, 1.0)

    def test_division_by_zero_000(self):
        self.c.clear()
        self.c.run('1 / 0')
        self.assertNotEqual(self.c.log[-1], 'result: 1.0')

    def test_division_by_zero_001(self):
        self.c.clear()
        self.c.run('1 / 0')
        self.assertNotEqual(self.c.lcd, 1.0)

class TestSimpleCalculatorMix(unittest.TestCase):

    def setUp(self):
        self.c = calculator.simple.SimpleCalculator()

    def test_long_1_000(self):
        self.c.clear()
        self.c.run("1 + 2 / 6 acv 1 + 1 / 33 fmod 0.01 1 2 3 4")
        self.assertEqual(self.c.log[-1], 'state -> r1: 4.0, op: , r2: 0.01')

    def test_long_1_001(self):
        self.c.clear()
        self.c.run("1 + 2 / 6 acv 1 + 1 / 33 fmod 0.01 1 2 3 4")
        self.assertEqual(self.c.lcd, 4.0)

class TestSimpleCalculatorAbs(unittest.TestCase):

    def setUp(self):
        self.c = calculator.simple.SimpleCalculator()

    def test_abs_000(self):
        self.c.clear()
        self.c.run('1 abs')
        self.assertEqual(self.c.lcd, 1)

    def test_abs_001(self):
        self.c.clear()
        self.c.run('-1 abs')
        self.assertEqual(self.c.lcd, 1)

    def test_abs_002(self):
        self.c.clear()
        self.c.run('0 abs')
        self.assertNotEqual(self.c.lcd, 1.0)

    def test_abs_003(self):
        self.c.clear()
        self.c.run('-2 abs - 2')
        self.assertNotEqual(self.c.lcd, -1.0)

if __name__ == '__main__':
    unittest.main()
