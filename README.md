Calculator
==========

This is simple calculator library with examples of command-line and TornadoWeb applications based around it.

How?
----

Clone this repo and run:

    `$ ./simplecalculator.py -s "1 + 2 / 6 acv 1 + 1 / 33 fmod 0.01"`

then,


    `$ ./simplecalculator.py -s "1 + 2 / 6 acv 1 + 1 / 33 ceil fmod"`

then,


    `$ ./simplecalculator.py -s "1 + 2 / 6 acv 1 + 1 / 33 fmod 0.01 1 2 3 4"`

The calculator is forgiving, it will ignore what it does not know, try to compute what it can treating the given string as a list of keystrokes.  You may see one or more `status` entries after the last result, that's intended.

If you want to implement Calculator as a RESTful API, install [TornadoWeb](http://tornadoweb.org 'TornadoWeb') and run `tornadoweb.py', then use curl:

    `$ curl -X POST http://localhost:8888/v1/calculate -d '1 + 2 / 6 acv 1 + 1 / 33 fmod 0.01 1 2 3 4'`

Why?
----

I got asked to provide samples of my work, proof I know Python, etc.  This project is way more than what I was sked to deliver, but I had more time to spare.

Who?
----

Jacek Artymiak
