Calculator
==========

A simple calculator library.

Examples of usage:

 * `simplecalculator.py` -- a command-line utility

 * `tornadoweb.py` -- a TornadoWeb applications with a minimalistic RESTful API. Do you math with curl!

How?
----

Clone this repo and tests:

    $ python -m unittest test

All good?

Usage
-----

import calculator

c = calculator.simple.SimpleCalculator()

c.run('1 + 1')
print c.get_tape()

Run:

    $ ./simplecalculator.py -s "1 + 2 / 6 acv 1 + 1 / 33 fmod 0.01"

then


    $ ./simplecalculator.py -s "1 + 2 / 6 acv 1 + 1 / 33 ceil fmod"

then


    $ ./simplecalculator.py -s "1 + 2 / 6 acv 1 + 1 / 33 fmod 0.01 1 2 3 4"

This calculator is as forgiving as a simple desktop calculator, it will ignore what it does not know, try to compute what it can treating the given string as a list of keystrokes.  You may see one or more `status` entries after the last result, that's intended.

If you want to implement this alculator as a RESTful API, install [TornadoWeb](http://tornadoweb.org 'TornadoWeb') and run `tornadoweb.py', then use curl:

    $ curl -X POST http://localhost:8888/v1/calculate -d '1 + 2 / 6 acv 1 + 1 / 33 fmod 0.01 1 2 3 4'

You can easily extend this calculator to support any number of one- and two-argument functions, search calculator/simple.py for `fmod` and `ceil` to see what modifications you need to make.

Why?
----

I got asked to provide samples of my work, proof I know Python, etc.  This project is way more than what I was asked to deliver, but I had more time to spare.  There is more coming.

Who?
----

Jacek Artymiak
