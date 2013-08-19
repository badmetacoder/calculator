# -*- coding: utf-8 -*-

# Simple calculator library

import math
import sys

class SimpleCalculator():
    """Simple calculator class."""

    s = ""
    sList = []

    # registers

    r1 = 0
    r1Set = False

    r2 = 0
    r2Set = False

    op = ""

    # history log
    h = []

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

    def ignore(self, i):
        """Log something calculator ignored.

        :param i: ignored chunk
        """

        self.h.append("ignored: %s" % str(i))

    def logState(self):
        """Log calculator state."""

        state = "state -> "

        if self.r1Set == True:
            state = "%s r1: %s" % (state, self.r1)
        if self.op != "":
            state = "%s op: %s" % (state, self.op)
        if self.r2Set == True:
            state = "%s r2: %s" % (state, self.r2)

        self.h.append(state)

    def compute(self):
        """Perform required computations."""

        self.logState()

        if self.r1Set == False:
            self.r1 = 'NaN'
        if self.r2Set == False:
            self.r2 = 'NaN'

        self.h.append("compute:")

        try:
            if self.op == '':
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

        self.h.append("result: %s" % str(self.r1))

    def run(self, s):

        self.s = s
        self.sList = s.split()

        self.h.append("input string: %s" % self.s)
        self.h.append("input list: %s" % str(self.sList))

        while 1:

            self.logState()

            if len(self.sList) == 0:
                if self.op == "":
                    break
                else:
                    self.compute()
                    break

            c = self.sList[0]
            self.sList = self.sList[1:]

            # math functions that take two arguments
            if c in ['+', '-', '*', '/', 'fmod']:

                if (self.r1Set == True) and (self.r2Set == False):
                    self.op = c 

                elif (self.r1Set == True) and (self.r2Set == True):
                    self.compute()
                    self.op = c

                else:
                    self.ignore(c)

            # math functions that take one argument
            elif c in ['ceil', 'fabs']:

                if (self.r1Set == True) and (self.r2Set == False):
                    self.op = c
                    self.compute()

                elif (self.r1Set == True) and (self.r2Set == True):
                    self.compute()
                    self.op = c
                    self.compute()

                else:
                    self.ignore(c)

            else:
                try:
                    f = float(c)

                    if (self.r1Set == True) and (self.op != "") and (self.r2Set == False):
                        self.r2 = f
                        self.r2Set = True

                    elif (self.r1Set == True) and (self.op != "") and (self.r2Set == True):
                        self.compute()
                        self.r1 = f
                        self.r1Set = True
                        self.r2Set = False

                    else:
                        self.r1 = f
                        self.r1Set = True

                except:
                    self.ignore(c)
