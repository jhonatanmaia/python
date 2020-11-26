"""

    HOF - Higher Order Function

- When a language supports a HOF, you can pass function as argumetns to
another function
- We can return a function in a function
- We can creat a type function varible

In python, functions are First Class Citizen

def sum(a,b):
    return a+b


def sub(a,b):
    return a-b


def mult(a,b):
    return a*b


def div(a,b):
    return a/b


def calc(num1,num2,function):
    return function(num1,num2)


    Nested Functions

Functions in functions are called Nested Functions or Inner Functions

from random import choice, random

def hi(person):
    def humor():
        return choice(('Whats up','Get out of here','I like you'))
    return humor() + person


Returning functions from another functions

def some_name(paramater):
    def someing():
        return random() + paramater
    return something


test = some_name()
print(test())

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    Decorators

- Decorators are functions
- Decorators use others functions and improve it
- Decorators are examples of HOF
- Decorators have own syntax, using @: Sugar Sytax

Not recommended

def something(function):
    def some():
        print('testing...')
        function()
        print('Failed!')
    return some


def some_function():
    print('80%...')


test = something(some_function)
test()    


Recommended with Syntx Sugar

def something_good(function):
    def some():
        print('testing...')
        function()
        print('Completed!')
    return some()


@something_good
def some_function_good():
    print('80%...')


some_function_good()


-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    Decorators with differents signatures

We use Decorator Pattern
Function signature is represented by its return, name and entry paramaters

def a1(function):
    def up(name):
        return function(name).upper()
    return up


@a1
def hello(name):
    return f'Hi, I am {name}'


@a1
def order(main,side_dish):
    return f'Hi, i would like a {main} with {side_dish}, please'


print(hello('Jose'))
print(order('Fish','Fries'))

Solving the problem

def a1(function):
    def up(*args,**kwargs):
        return function(*args,**kwargs).upper()
    return up


@a1
def hello(name):
    return f'Hi, I am {name}'


@a1
def order(main,side_dish):
    return f'Hi, i would like a {main} with {side_dish}, please'


print(hello('Jose'))
print(order('Fish','Fries'))

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    Preserving Metadata

Metadata -> Its intrinsic datas: modify date, size, resolution, duration...
Wraps -> Its functions use elements with any uses
- You can access the function doc without problems

def ver_log(function):
    def logging(*args,**kwargs):
        '''Im a function {loging} inside another'''
        print(f'You are calling {function.__name__}')
        print(f'Here is the documentation {function.__doc__}')
        return function(+args,**kwargs)
    return logging


@ver_log
def sum(a,b):
    ''' sum two numbers '''
    return a+b


print(sum.__name__)
print(sum.__doc__)

from functools import wraps

def ver_log(function):
    @wraps(function)
    def logging(*args,**kwargs):
        '''Im a function {loging} inside another'''
        print(f'You are calling {function.__name__}')
        print(f'Here is the documentation {function.__doc__}')
        return function(+args,**kwargs)
    return logging


@ver_log
def sum(a,b):
    ''' sum two numbers '''
    return a+b


print(sum.__name__)
print(sum.__doc__)

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    Forcing Data Types
    
def forcing_type(*types):
    def decorator(function):
        def convert(*args,**kwargs):
            new_args=[]
            for(value,type1) in zip(args,types):
                new_args.append(type1(value)) #str('a'), int('3')
            return function(*new_args,**kwargs)
        return convert
    return decorator


@forcing_type(str,int)
def msg_repeat(msg,times):
    for n in range(times):
        print(msg)


msg_repeat('a','3')

@forcing_type(float, float)
def division(a,b):
    pritn(a/b)


division('1',5)

"""
