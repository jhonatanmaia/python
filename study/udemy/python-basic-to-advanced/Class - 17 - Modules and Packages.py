"""
    Random Module
    
Any file.py is a module and can be imported

Random Module -> Generate pseudo random numbers

Importing all the module, everything inside

import random

print(random.random()) -> generate a number between 0 and 1

Import only one or more functions, and not all the package

from random import random, uniform, randint, choice, shuffle

print(random)

for i in range(10):
    print(random())

Generate a number between 2 numbers
for i in range(10):
    print(uniform(3,7)) # 7 is not included

Generate an integer number between 2 numbers
for i in range(6):
    print(randint(1,61),end=', ')

a1=[1,2,3,4,5,6,7,8,9,10,1,1,1,12,3,4]
shuffle(a1)
print(a1)

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    Built-In

dir()

alias

import random as rdm
from random import * # here you dont need to do random.random()
from random import randint as rdi
from random import randint as rdi, random as rdm
from random import random, randint, shuffle, choice
Usually use a tuple
from random import (
    random, 
    randint, 
    shuffle, 
    choice
)

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    Custom Modules

Any file.py is a module, just need to import and use it

import your_module as sm

You can even use a list from there

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    Installing and using external modules

We use a manager package called Pip - Python Installer Package

type pip in the console

Colorama -> Its used to print color text

from colorama import init
from colorama import Fore, Back, Style

print(Fore.RED+'Test')
print(Fore.GREEN+'Test2')
print(Fore.LIGHTBLUE_EX+'Test3')
print(Fore.MAGENTA+'Test4')

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    Packages

Module <> Packages

Module -> Its a file.py
Package -> Its a modules collection

OBS: In Python 2.x it's required the __init__.py file, but 3.x+ it´s optional
but its recommend to have because of compatibily issues

We create the test package

from geek import something1, something2
from geek.testintest import three, four

print(something1.function1())

print(something2.pi)
print(something2.function2(4,5))

print(three.function3())

print(four.function4())

from geek.something1 import function1
from geek.testintest.four import function4

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    Dunder Main and Dunder Name

Dunder -> Double under

Dunder Name -> __name__
Dunder Main -> __main__

Used to creat functions, attributes, properties and more using Double Under
to avoid conflicts

If we execute a module in Python direct in the comand line, python will
give the variable __name__ the value __main__ saying that this module
is the pricipal/main

If you execute this file.py it will become the __main__ but if you import
you wont execute as __main__

if you import the __name__ will be the file name
"""

from geek import testingdunder as td

print(td.sumodd([1,2,3,4,5]))
td.function1()