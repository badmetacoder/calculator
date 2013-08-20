# -*- coding: utf-8 -*-

# Simple calculator library

import math

class SimpleCalculator():
    """Simple calculator class."""


    two_arg_funcs = set(['+', '-', '*', '/', 'fmod'])
    one_arg_funcs = set(['ceil', 'fabs'])

    def __init__(self):
        """Intialize SimpleCalculator.

        :param s: numbers.
        :param v: verbosity.
        """

        self.c()

    def c(self):
        """Reset calculator."""

        # initialize

        self.s = ""
        self.sList = []

        # registers

        self.r1 = 0
        self.r1Set = False

        self.r2 = 0
        self.r2Set = False

        self.op = ""

        # history log
        self.h = []

        self.r = ""

    def logInfo(self, s):
        """Log a message."""

        self.h.append(s)

    def logState(self):
        """Log calculator state."""

        state = "state -> "

        if self.r1Set:
            state = "%s r1: %s" % (state, self.r1)
        if self.op:
            state = "%s op: %s" % (state, self.op)
        if self.r2Set:
            state = "%s r2: %s" % (state, self.r2)

        self.logInfo(state)

    def ignore(self, i):
        """Log something calculator ignored.

        :param i: ignored chunk
        """

        self.logInfo("ignored: %s" % str(i))

    def compute(self):
        """Perform required computations."""

        self.logState()

        if not self.r1Set:
            self.r1 = 'NaN'
        if not self.r2Set:
            self.r2 = 'NaN'

        self.logInfo("compute:")

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
            elif self.op == 'ceil':
                self.r1 = math.ceil(self.r1)
            elif self.op == 'fabs':
                self.r1 = math.fabs(self.r1)
            elif self.op == 'fmod':
                self.r1 = math.fmod(self.r1, self.r2)

            self.r2Set = False
            self.op = ""

        except:
                self.r1 = 'Error'
                self.r1Set = False
                self.r2Set = False
                self.op = ""

        self.logInfo("result: %s" % str(self.r1))

    def run(self, s):

        self.s = s
        self.sList = s.split()

        self.logInfo("input string: %s" % self.s)
        self.logInfo("input list: %s" % str(self.sList))

        while 1:

            self.logState()

            if len(self.sList) == 0:
                if not self.op:
                    break
                else:
                    self.compute()
                    break

            c = self.sList[0]
            self.sList = self.sList[1:]

            if c in self.two_arg_funcs:

                if self.r1Set and not self.r2Set:
                    self.op = c 

                elif self.r1Set and self.r2Set:
                    self.compute()
                    self.op = c

                else:
                    self.ignore(c)

            elif c in self.one_arg_funcs:

                if self.r1Set and not self.r2Set:
                    self.op = c
                    self.compute()

                elif self.r1Set and self.r2Set:
                    self.compute()
                    self.op = c
                    self.compute()

                else:
                    self.ignore(c)

            else:
                try:
                    f = float(c)

                    if self.r1Set and self.op and not self.r2Set:
                        self.r2 = f
                        self.r2Set = True

                    elif self.r1Set and self.op and self.r2Set:
                        self.compute()
                        self.r1 = f
                        self.r1Set = True
                        self.r2Set = False

                    else:
                        self.r1 = f
                        self.r1Set = True

                except:
                    self.ignore(c)
