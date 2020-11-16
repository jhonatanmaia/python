"""
import this -> the zen of python
pep 8 -> Python Enhancement Proposals
Developers can improve the way we can program in python
The general idea of pep 8 is that we can 
develop programs better and more beautiful

[1] - Use Camel Case names for class names


class Calc:
    pass


not
class calc_code:
    pass

[2] - Use snake case names for functions or variables


def sum():
    pass


or


def sum_two():
    pass


number=4
second_number=8
odd_number=1

[3] - Use 4 spaces for indentation
if 'a' in 'banana':
    print('It has')
    
[4] - Empty lines
- functions and definitions of classes - 2 lines
- methods inside a class - 1 lines

[5] - Imports
- Imports need to be in separated lines

not
import sys, os

use
import sys
import os

also
from types import StringType, ListType

if you many imports, use
from types import (
    StringType,
    ListType,
    SetType,
    OutroType
)

also
Imports need to be the first line

[6] - Spaces in expressions and instructions

not
function( something[ 1 ] ), { two: 2} )
function (1)
dict ['key'] = list [indice]
x           = 1
y           = 3
even_number = 2
use
function(something[1]), {two: 2})
function(1)
dict['key'] = list[indice]
x = 1
y = 3
even_number = 2

[7] - Always finish a strunction with a new line

"""
import this

print('something')
