#!/usr/bin/python
# -*- coding: utf-8 -*-
# pylint: disable=R0904

"""Unit tests for calculator
"""

import calculator
import unittest


class TestSimpleCalculatorAddition(unittest.TestCase):

    """Unit tests for addition.
    """

    def setUp(self):
        self.calculator = calculator.simple.SimpleCalculator()

    def test_addition_000(self):

        """Addition test 000.
        """

        self.calculator.clear()
        self.calculator.run('1 + 1')
        self.assertEqual(self.calculator.log[-1], 'result: 2.0')

    def test_addition_001(self):

        """Addition test 001.
        """

        self.calculator.clear()
        self.calculator.run('1 + 1')
        self.assertEqual(self.calculator.lcd, 2.0)

    def test_addition_002(self):

        """Addition test 002.
        """

        self.calculator.clear()
        self.calculator.run('1 + -1')
        self.assertEqual(self.calculator.log[-1], 'result: 0.0')

    def test_addition_003(self):

        """Addition test 003.
        """

        self.calculator.clear()
        self.calculator.run('1 + -1')
        self.assertEqual(self.calculator.lcd, 0.0)


class TestSimpleCalculatorSubtraction(unittest.TestCase):

    """Unit tests for subtraction.
    """

    def setUp(self):
        self.calculator = calculator.simple.SimpleCalculator()

    def test_subtraction_000(self):

        """Subtraction test 000.
        """

        self.calculator.clear()
        self.calculator.run('1 - 2')
        self.assertEqual(self.calculator.log[-1], 'result: -1.0')

    def test_subtraction_001(self):

        """Subtraction test 002.
        """

        self.calculator.clear()
        self.calculator.run('1 - 2')
        self.assertEqual(self.calculator.lcd, -1.0)


class TestSimpleCalculatorMultiplication(unittest.TestCase):

    """Unit tests for multiplication.
    """

    def setUp(self):
        self.calculator = calculator.simple.SimpleCalculator()

    def test_multiplication_000(self):

        """Multiplication test 000.
        """

        self.calculator.clear()
        self.calculator.run('1 * 1')
        self.assertEqual(self.calculator.log[-1], 'result: 1.0')

    def test_multiplication_001(self):

        """Multiplication test 001.
        """

        self.calculator.clear()
        self.calculator.run('1 * 1')
        self.assertEqual(self.calculator.lcd, 1.0)


class TestSimpleCalculatorDivision(unittest.TestCase):

    """Unit tests for division.
    """

    def setUp(self):
        self.calculator = calculator.simple.SimpleCalculator()

    def test_division_000(self):

        """Division test 000.
        """

        self.calculator.clear()
        self.calculator.run('1 / 1')
        self.assertEqual(self.calculator.log[-1], 'result: 1.0')

    def test_division_001(self):

        """Division test 001.
        """

        self.calculator.clear()
        self.calculator.run('1 / 1')
        self.assertEqual(self.calculator.lcd, 1.0)

    def test_division_by_zero_000(self):

        """Division by zero test 000.
        """

        self.calculator.clear()
        self.calculator.run('1 / 0')
        self.assertNotEqual(self.calculator.log[-1], 'result: 1.0')

    def test_division_by_zero_001(self):

        """Division by zero test 001.
        """

        self.calculator.clear()
        self.calculator.run('1 / 0')
        self.assertNotEqual(self.calculator.lcd, 1.0)


class TestSimpleCalculatorMix(unittest.TestCase):

    """Unit tests for mix.
    """

    def setUp(self):
        self.calculator = calculator.simple.SimpleCalculator()

    def test_long_1_000(self):

        """Long input string test 000.
        """

        slug = 'state -> r1: 4.0, op: , r2: 0.01'
        self.calculator.clear()
        self.calculator.run("1 + 2 / 6 acv 1 + 1 / 33 fmod 0.01 1 2 3 4")
        self.assertEqual(self.calculator.log[-1], slug)

    def test_long_1_001(self):

        """Long input string test 001.
        """

        self.calculator.clear()
        self.calculator.run("1 + 2 / 6 acv 1 + 1 / 33 fmod 0.01 1 2 3 4")
        self.assertEqual(self.calculator.lcd, 4.0)


class TestSimpleCalculatorAbs(unittest.TestCase):

    """Unit tests for abs.
    """

    def setUp(self):
        self.calculator = calculator.simple.SimpleCalculator()

    def test_abs_000(self):

        """ABS test 000.
        """

        self.calculator.clear()
        self.calculator.run('1 abs')
        self.assertEqual(self.calculator.lcd, 1)

    def test_abs_001(self):

        """ABS test 001.
        """

        self.calculator.clear()
        self.calculator.run('-1 abs')
        self.assertEqual(self.calculator.lcd, 1)

    def test_abs_002(self):

        """ABS test 002.
        """

        self.calculator.clear()
        self.calculator.run('0 abs')
        self.assertNotEqual(self.calculator.lcd, 1.0)

    def test_abs_003(self):

        """ABS test 003.
        """

        self.calculator.clear()
        self.calculator.run('-2 abs - 2')
        self.assertNotEqual(self.calculator.lcd, -1.0)

if __name__ == '__main__':
    unittest.main()
