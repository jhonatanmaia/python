"""
    Common Errors

SyntaxError -> You wrote something wrong or used a reserved word
def function:
    print('something')


def = 1
return

NameError -> When a variable or function wasn't declared

It's common when you're working with global/local variables

TypeError -> When a function/operation/action is apply to a wrong type

print(len(5))
print('Word' + [])

IndexError -> When we try to access an invalid index

list1=[1]
print(list1[1])

ValueError -> It happens when a function/operation built in receive an 
argument correct but with an inappropriate value 

print(int('Wrong'))

KeyError -> It happens when we try to access a dictionary with a key that
doesn't exist

AttributeError -> It happens when a variable doesn't have an attribute/function

tuple1=(11,2,31,4)
tuple1.sort()
print(tuple1)

IndentationError -> It happens when we don't respect Python indentation

def new():
print('function part')


for i in range(10):
i+1

Excepions and errors are synonyms
It's important to read and have attention to the output

-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

    Raise

raise -> It's not a function, its a reserved word. Show an excession

raise ErrorType('Error Mensage')

-> OBS: Raise shutdown the function execution

def color(text,color):
    colors = ('green','yellow','blue','white')
    if type(texto) is not str:
        raise TypeError('Text needs to be a String')
    if type(color) is not str:
        raise TypeError('Color needs to be a string')
    if color not in colors:
        raise ValueError(f'The color needs to be one of {colors}')
    print(f'The text {text} will be print in {color}')


color('a',4)

-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

    Try/Except

try:
    something that is probably wrong
except:
    if goes wrong, do this
    
try:
    function_none()
except:
    print('Somethin went wrong')

try:
    len(5)
except TypeError:
    print('TypeError occurred')

try:
    int('hehe')
except ValueError as err: #You can give any name you want to, but the normal
is err
    print(f'The error was {err}')

try:
    print('a'[3])
except NameError as err:
    print(f'NameError: {err}')
except TypeError as err:
    print(f'TypeError: {err}')
except:
    print('Other error')


-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

    Try Except Else Finally
    
- When should you treat code? EVERY USER INPUT OR ANY INPUT

try:
    num = int(input('Enter a number:'))
except ValueError:
    print('Incorrect Number')
else: #If there was no error, do this
    print(f'Your number: {num}')
finally:
    print('Execute this with or withour an error')    

- Why use finally? To close or deallocate resources | Close database

The Correct Way

def division(a,b):
    try:
        return int(a)/int(b)
    except ValueError:
        print('Incorrent Value')
    except ZeroDivisionError:
        print('Its possible to divide per zero')
    except (ValueError,ZeroDivisionError) as err:
        print(err)


num1=input('First number: ')
num2=input('Second number: ')

print(division(num1,num2))

-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

    Debugging code with PDB Python Debugger
    
We need to import the library pdb

Not a good idea

def division(a,b):
    print('test')
    try:
        print('worked')
        return int(a)/int(b)
    except (ValueError,ZeroDivisionError) as err:
        print(err)


num1=input('First number: ')
num2=input('Second number: ')

print(division(num1,num2))

Select the line and put the red ball

PDB commands

l -> list where we are
n -> next line
p -> print the variable
c -> continuos the 

-> Avoid variables named l n p or c

-> Python 3.7+ has pdb is a buit in and it called breakpoint()
"""

import pdb

pdb.set_trace()
# or
import pdb; pdb.set_trace()
def division(a,b):
    try:
        return int(a)/int(b)
    except (ValueError,ZeroDivisionError) as err:
        print(err)


num1=input('First number: ')
num2=input('Second number: ')

print(division(num1,num2))
