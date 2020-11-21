"""
- May can receive a input paramater or may not

Function = DRY - Don't Repeat Yourself

-> ALWAYS LOWER CASE AND SNAKE CASE

def function_name(input_paramater = optional or not):
    function
    return -> Optional


def say_hello():
    print('Hello!')


say_hello()

for n in range(5):
    say_hello()

# Unusual
say = say_hello
say()


-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

Functions with return

numbers = [1,2,3]
ret_pop = numbers.pop()

ret_print=print('something')
print(ret_print)

def name():
    return something


def some_of_two():
    return 2+2


OBS: Return word

1 - It finishes the functions
2 - We can, in one function, have more than one return
3 - We can, in one function, return any type of data or even multiples values

def new_function():
    x=int(input('Number: '))
    
    if x > 0:
        return x
    elif x == 0:
        return x+1
    return x*0


def something():
    return 2,3,4,5


num1, num2, num3,num4 = something()
print(num1, num2,num3,num4)


-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

Functions with paramaters

- Functions process teh paramaters/data

def a_name(paramater):
    return something


a_name(argument)

def sum(number):
    return number+number


-> Always use explicit names in the parameters

-> Parameters are the variable declared in the function definition
-> Arguments are data pass during the run of a function

-> We can force the arguments

def multiplication(number_1,number_2):
    return number_1*number_2


multiplication(number_2=10,number_1=20)

We can pass a lis/tuple as an argument

-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

    Optional Paramaters
    
def exponential(number,power=2):
    return number ** power


print(exponential(2))
print(exponential(2,100_000))

-> Default paramaters NEEDS to be after the non default parameters
- We can use any type of data as a paramater
    number,strings,floats,booleans,list,tuples,dict,functions and etc
    
-> Local variables > global varaible

total = 0

def up():
    global total -> We say that we want the global variable
    total += 1
    return total


-> You can have a function inside a function

-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

    Docstrings

-> Comment a function

def say_hello():
    '''
    A function that prints Hello!
    '''
    print('Hello!')


-> Always use 3x""

-> We can have the function documentation using special property __doc__
print.__doc__
help.__doc__

-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

    Understanding *args

-> It's a paramater. It can be anything, justneed to start with *

-> Communit call as *args

-> What does mean *args?
- Put the extra values into a tuple, for multiples arguments

def sum_everything(*number):
    return sum(args)
    # or
    sum=0
    for n in number:
        sum+=n
    return sum


Automatic unpacking

numbers_list=[1,2,3,4,5,6,7,8,9,10]
sum_everything(*numbers_list) -> Automatic unpack the list

-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

    Understanding **kwargs
    
- Transform the arguments into a dictionary
- Args and Kwargs are not required

def favorite_colours(**kwargs):
    print(kwargs)
    # or
    for letter,colour in kwargs.items():
        print(f'{letter} = {colour.title()}')


favorite_colours(a='green',b='yellow',c='blue',d='white')

    FUNCTION ORDER
    
- Required paramaters
- *args
- Default paramaters
- **kwargs

    Unpacking a **kwargs

def show_names(**kwargs):
    return f'{kwargs['name']} {kwargs['lastname']}'


names = {'name':'Felicity','lastname':'Jones'}

print(show_names(**names))

def sum(a:,b,c):
    print(a+b+c)
    

dictionary = dict(a=1,b=2,c=3)
sum(*dict)
-> If you put a string will show an error

TYPE HITING

def mesage(text: str) -> str:
    # type: (str) -> str
    # You can also do this
    return f'You text: {text}'


# type (as, many, type, of, variables, you, want, to) -> return


a=mesage('hi')
print(a)

print(mesage.__annotations__)

name: str = 'Jose'
weight: float = 85.4
active: bool = True

class Person:
    
    # Paramaters
    def __init__(self, name: str, age: int, weight: float) -> None:
        self.__name: str = name #Attribute
        self.__age: int = age
        self.__weight: float = weight
    
    
    def walk(self) -> str:
        return f'{self.__name} is walking.'


-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

names: list = ['a','b']
versions: tuple = (3,4,5)
options: dict = {'air':True,'OS':False}
values: set = {3,4,5,6}
age: int = 40
name: str = 'c'
on: bool = True
weight: float = 40.5

"""

names: list = ['a','b']
versions: tuple = (3,4,5)
options: dict = {'air':True,'OS':False}
values: set = {3,4,5,6}
age: int = 40
name: str = 'c'
on: bool = True
weight: float = 40.5

from typing import Dict, List, Tuple, Set

names2: List[str] = ['e','f']
versions2: Tuple[int, int, int] = (5,7,3)
options2: Dict[str, bool] = {'z':True,'y':False}
values2: Set[int] = {9,0,5,1}