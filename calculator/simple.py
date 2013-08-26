# -*- coding: utf-8 -*-

# Simple calculator library

import math

class SimpleCalculator():
    """Simple calculator class."""

    two_arg_funcs = set(['+', '-', '*', '/', 'fmod'])
    one_arg_funcs = set(['abs', 'ceil', 'fabs'])

    def __init__(self):
        """Intialize SimpleCalculator.
        """

        self.clear()

    def clear(self):
        """Reset calculator."""

        # initialize

        self.s = ""
        self.s_list = []

        # registers

        self.r1 = 0
        self.r1_set = False

        self.r2 = 0
        self.r2_set = False

        self.op = ""

        # history log
        self.log = []

        # LCD status
        self.lcd = "0"

    def log_info(self, s):
        """Log a message."""

        self.log.append(s)
        self.lcd = self.r1

    def log_state(self):
        """Log calculator state."""

        state = "state -> r1: %s, op: %s, r2: %s" % (self.r1, self.op, self.r2)
        self.log_info(state)

    def ignore(self, i):
        """Log something calculator ignored.

        :param i: ignored chunk
        """

        self.log_info("ignored: %s" % str(i))

    def compute(self):
        """Perform required computations."""

        self.log_state()

        if not self.r1_set:
            self.r1 = 'NaN'
        if not self.r2_set:
            self.r2 = 'NaN'

        self.log_info("compute:")

        try:
            if not self.op:
                pass
            elif self.op == '+':
                self.r1 = self.r1 + self.r2
            elif self.op == '-':
                self.r1 = self.r1 - self.r2
            elif self.op == '*':
                self.r1 = self.r1 * self.r2
            elif self.op == '/':
                self.r1 = self.r1 / self.r2
            elif self.op == 'abs':
                self.r1 = abs(self.r1)
            elif self.op == 'ceil':
                self.r1 = math.ceil(self.r1)
            elif self.op == 'fabs':
                self.r1 = math.fabs(self.r1)
            elif self.op == 'fmod':
                self.r1 = math.fmod(self.r1, self.r2)

            self.r2_set = False
            self.op = ""

        except:
                self.r1 = 'Error'
                self.r1_set = False
                self.r2_set = False
                self.op = ""

        self.log_state()
        self.log_info("result: %s" % str(self.r1))

    def run(self, s):

        self.s = s
        self.s_list = s.split()

        self.log_info("input string: %s" % self.s)
        self.log_info("input list: %s" % str(self.s_list))

        while 1:

            self.log_state()

            if len(self.s_list) == 0:
                if not self.op:
                    break
                else:
                    self.compute()
                    break

            c = self.s_list[0]
            self.s_list = self.s_list[1:]

            if c in self.two_arg_funcs:

                if self.r1_set and not self.r2_set:
                    self.op = c 

                elif self.r1_set and self.r2_set:
                    self.compute()
                    self.op = c

                else:
                    self.ignore(c)

                #self.log_state()

            elif c in self.one_arg_funcs:

                if self.r1_set and not self.r2_set:
                    self.op = c
                    self.compute()

                elif self.r1_set and self.r2_set:
                    self.compute()
                    self.op = c
                    self.compute()

                else:
                    self.ignore(c)

                #self.log_state()

            else:
                try:
                    f = float(c)

                    if self.r1_set and self.op and not self.r2_set:
                        self.r2 = f
                        self.r2_set = True

                    elif self.r1_set and self.op and self.r2_set:
                        self.compute()
                        self.r1 = f
                        self.r1_set = True
                        self.r2_set = False

                    else:
                        self.r1 = f
                        self.r1_set = True

                    #self.log_state()

                except:
                    self.ignore(c)

                    #self.log_state()
