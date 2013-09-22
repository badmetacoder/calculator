# -*- coding: utf-8 -*-

"""Simple calculator.
"""

# Simple calculator library

import math


class SimpleCalculator():
    """Simple calculator class."""

    def __init__(self):
        """Intialize SimpleCalculator.
        """

        self.two_arg_funcs = set(['+', '-', '*', '/', 'fmod'])
        self.one_arg_funcs = set(['abs', 'ceil', 'fabs'])
        self.raw_str = ""
        self.operand = ""
        self.log = []
        self.s_list = []
        self.lcd = 0
        self.reg_1 = 0
        self.reg_2 = 0
        self.reg_1_set = False
        self.reg_2_set = False

        self.clear()

    def clear(self):
        """Reset calculator."""

        # initialize

        self.raw_str = ""
        self.s_list = []

        # registers

        self.reg_1 = 0
        self.reg_1_set = False
        self.reg_2 = 0
        self.reg_2_set = False

        self.operand = ""

        # history log
        self.log = []

        # LCD status
        self.lcd = "0"

    def log_info(self, message):
        """Log a message."""

        self.log.append(message)
        self.lcd = self.reg_1

    def log_state(self):
        """Log calculator state."""

        state_str = "state -> r1: %s, op: %s, r2: %s"
        state = state_str % (self.reg_1, self.operand, self.reg_2)
        self.log_info(state)

    def ignore(self, i):
        """Log something calculator ignored.

        :param i: ignored chunk
        """

        self.log_info("ignored: %s" % str(i))

    def compute(self):
        """Perform required computations."""

        self.log_state()

        if not self.reg_1_set:
            self.reg_1 = 'NaN'
        if not self.reg_2_set:
            self.reg_2 = 'NaN'

        self.log_info("compute:")

        try:
            if not self.operand:
                pass
            elif self.operand == '+':
                self.reg_1 = self.reg_1 + self.reg_2
            elif self.operand == '-':
                self.reg_1 = self.reg_1 - self.reg_2
            elif self.operand == '*':
                self.reg_1 = self.reg_1 * self.reg_2
            elif self.operand == '/':
                self.reg_1 = self.reg_1 / self.reg_2
            elif self.operand == 'abs':
                self.reg_1 = abs(self.reg_1)
            elif self.operand == 'ceil':
                self.reg_1 = math.ceil(self.reg_1)
            elif self.operand == 'fabs':
                self.reg_1 = math.fabs(self.reg_1)
            elif self.operand == 'fmod':
                self.reg_1 = math.fmod(self.reg_1, self.reg_2)

            self.reg_2_set = False
            self.operand = ""

        except:

            self.reg_1 = 'Error'
            self.reg_1_set = False
            self.reg_2_set = False
            self.operand = ""

        self.log_state()
        self.log_info("result: %s" % str(self.reg_1))

    def run(self, input_str):

        self.raw_str = input_str
        self.s_list = input_str.split()

        self.log_info("input string: %s" % self.raw_str)
        self.log_info("input list: %s" % str(self.s_list))

        while 1:

            self.log_state()

            if len(self.s_list) == 0:
                if not self.operand:
                    break
                else:
                    self.compute()
                    break

            chunk = self.s_list[0]
            self.s_list = self.s_list[1:]

            if chunk in self.two_arg_funcs:

                if self.reg_1_set and not self.reg_2_set:
                    self.operand = chunk

                elif self.reg_1_set and self.reg_2_set:
                    self.compute()
                    self.operand = chunk

                else:
                    self.ignore(chunk)

            elif chunk in self.one_arg_funcs:

                if self.reg_1_set and not self.reg_2_set:
                    self.operand = chunk
                    self.compute()

                elif self.reg_1_set and self.reg_2_set:
                    self.compute()
                    self.operand = chunk
                    self.compute()

                else:
                    self.ignore(chunk)

            else:

                try:
                    number = float(chunk)

                    if self.reg_1_set and self.operand and not self.reg_2_set:
                        self.reg_2 = number
                        self.reg_2_set = True

                    elif self.reg_1_set and self.operand and self.reg_2_set:
                        self.compute()
                        self.reg_1 = number
                        self.reg_1_set = True
                        self.reg_2_set = False

                    else:
                        self.reg_1 = number
                        self.reg_1_set = True

                except:

                    self.ignore(chunk)
