# -*- coding: utf-8 -*-

"""
simplecalculator library
-------------------------

This is a proof of concept of a simple calculator library, written in Python.

It mimick the behavior of a very simple desktop calculator. You give it a list
of numbers and operations as a string and it will create a trace of the
operations performed.  That trace is stores in SimpleCalculator.log. The most
recent state of the LCD display is stored in SimpleCalculator.lcd.
"""

__title__ = 'calculator'
__version__ = '0.0.3'
__build__ = 0x000003
__author__ = 'Jacek Artymiak'
__license__ = 'The BSD 3-Clause License'
__copyright__ = 'Copyright 2013 Jacek Artymiak'

from . import simple
