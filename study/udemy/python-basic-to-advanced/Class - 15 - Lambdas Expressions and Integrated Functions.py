"""

    Lambdas Expressions

-> Lambdas: Unamed functions or anonymous functions

Python Function

def calc(x):
    return 3 * x + 1


Lambda Expression

lambda x: 3 * x + 1

How to use?

Non usual
calc = lambda x: 3 * x + 1
number = calc(4)
print(number)

Multiples paramaters/arguments in lambas

name = lambda name, last_n: name.strip().title()+ ' ' + last_n.strip().title()

print(name('ANGELINA       ', '    jolie  '))

test = lambda: 'A lambda without a paramater'
test1 = lambda x: 3*x+1
test2 = lambda x, y: (x*y)**10
test3 = lambda x, y, z: (x*y*z)**z**y+1

author = ['William Shakespeare','Emily Dickinson','H. P. Lovecraft',
          'Arthur Conan Doyle','Leo Tolstoy','Edgar Allan Poe','Seneca',
          'Robert Ervin Howard','Rabindranath Tagore','Rudyard Kipling']

The normal way to use lambda

author = ['William Shakespeare', 'Emily Dickinson',
          'H. P. Lovecraft','Arthur Conan Doyle', 'Leo Tolstoy',
          'Edgar Allan Poe', 'Seneca','Robert Ervin Howard',
          'Rabindranath Tagore', 'Rudyard Kipling']
 
print(author)
author.sort(key=lambda name: name.split(',')[-1].lower())
print("_________")
print(author)
print("_________")

Quadratic Function
f(x)=a*x**2+b*x+c

def fquadratic(a,b,c):
    return lambda x:a*x**2+b*x+c


here we give a b c it will return the lambda with x
test = fquadratic(2,3,-5)

here we give the x value
print(test(0))
print(test(1))
print(test(2))

other way
print(fquadratic(3,0,1)(2))

We use lambda filter and order data

-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

    Map

Map <> dictionary

With map we do mapping of values for function

import math

def area(r):
    Circle area
    return math.pi*(r**2)


print(area(2))
print(area(5.4))

radius = [2,4,2,5,6,3,31,2,5,6,9,399,0.4]

    comun way

areas=[]
for r in radius:
    areas.append(area(r))

print(areas)

    map way

map receive two paramaters, first the function and the second is an interable

areas01=map(area,radius)

print(areas01)
print(type(areas01))

after that we can convert to a list, tuple etc

print(list(areas01))
print(tuple(areas01))

Usually we use a lambda instead a function to map

    lambda map

import math
radius = [2,4,2,5,6,3,31,2,5,6,9,399,0.4]
print(list(map(lambda r: math.pi*(r**2),radius)))

after you use a function map() for the first time using the result,
it will be cleaned

other example

cities = [('Berlim',29),('Cairo',36),('Buenos Aires',10),('Los Angeles',26),
          ('Tokyo',27),('New York',28),('London',22)]

celsius to fahrenheit

c_to_f = lambda dado: (dado[0],(9/5)*dado[1]+32)

print(list(map(c_to_f,cities)))

-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

    Filter

filter() -> you can filter datas in a colection selected

values = (1,2,3,4,5,6)

average = (sum(values) / len(values))
print(average)

Library to work with statistics data

import statistics as st

data = [1.2,2.8,0.9,4.2,9,-1]

Using mean() to get the average

average01 = st.mean(data)

print(average01)

-> Like map(), filter() receive two paramaters, function and interable

-> If above the average is going to be true
res = filter(lambda value: value > average01, data)

-> It's a filter object
print(type(res)) 
print(list(res))

-> Like map(), filter() is going to lost the data after using

countries = ['','Argentina','Portugal','','','','US','Brazil','China']

print(countries)
res01 = filter(None,countries)
res02 = filter(lambda country: len(country) > 0, countries)
print(list(res01))

    Difference between map e filter
    
Map return any type of values to a list
filter retun true or false, if true the value will be added to a list

-> Complex Example

users = [
    {'username':'samuel','tweets':['I love cakes','I like pizzas']},
    {'username':'carla','tweets':['I love cats','I hate pizzas']},
    {'username':'juan','tweets':['I want to travel']},
    {'username':'zezinho','tweets':[]},
    {'username':'antony','tweets':[]},
    {'username':'bruna','tweets':[]}    
]

-> Filter the user inative, without a tweet

print(users)

inative = list(filter(lambda user: len(user['tweets']) == 0 , users))

print(inative)

inative2 = list(filter(lambda user: not user['tweets'] , users))

print(inative2)

names = ['Vanessa','Ana','Maria']

-> Create a list using 'Your teacher is' + name, if the name has more than
5 character

list_01=list(map(lambda name: f'Your teacher is {name}',
                 filter(lambda name: len(name) < 5, names)))

-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

    Reduce

After python3+ its not a built in function anymore
we need to import the functools

Guido van Rossum: Only use reduce() function if you really need, otherwise 
use a for loop to be more legible

reduce receive two paramaters

Use the result of a function as the first paramater of a function
data=[a1,a2,a3,a4, ... an]
def function(x,y):
    return x*y


function(function(function(a1,a2),a3),a4), ...), an)

from fuctools import reduce

data = [2,3,5,11,3,5,9,8,65,2,35]

We need a function that receive two paramaters

multi = lambda x, y: x*y

res = reduce(multi,data) 

print(res)   

loop

res2=1
for n in data:
    res2*=n

print(res2)

-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

All() -> Return true if all the elements are true or if the iterable is empty

It can be a set/list/tuple/string

print(all([0,1,2,3,4])) -> False
print(all([1,2,3,4])) -> True
print(all([])) -> True
print(all('Geek')) -> True

names=['Carlos','Camila','Cedro','Cristina','Cezinho']
print(all([name[0] == 'C' for name in names])) -> True

Empty interable to bollean is False, but all() is True

print(all([num for num in [4,2,10,6,8] if num % 2 == 0]))

any() -> Return True if any element in the interable is true. If its empty
return False

print(any[0,1,2,3,4]) True
print(any[0,False,{},(),[]]) False

-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

    Generator Expression

Tuple Comprehension = Generators

names = ['Carlos','Camila','Cecinho','Cristina','Cristiane','Vanessa']

print(any([name[0] == 'C' for name in names]))
print(any(name[0] == 'C' for name in names))

List Comprehension

res = [name[0] == 'C' for name in names]
print(type(res))

List Generator

res = (name[0] == 'C' for name in names)
print(type(res))

Generator use less memory ressource
If you need the data, use list comprehension, if not use list generator

from sys import getsizeof

list_comp = getsizeof([x*10 for x in range(1000)])
set_comp = getsizeof({x*10 for x in range(1000)})
dic_comp = getsizeof({x: x*10 for x in range(1000)})
gen_comp = getsizeof(x*10 for x in range(1000))

print(list_comp)
print(set_comp)
print(dic_comp)
print(gen_comp)

interating

gen = (x*10 for x in range(1000))
print(gen)
print(type(gen))
for num in gen:
    print(num)
-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

    Sorted

Can be usd with any iterable
Retun a sort list, even if you passed a tuple or set
Doesnt change the original list

numbers = [9,5,6,3,6,2,3]
print(numbers)
print(sorted(numbers))
print(numbers)

numbers = [9,5,6,3,6,2,3]
print(reversed(numbers,reverse=True))

We can use sorted() to more complex things

users = [
    {'username':'samuel','tweets':['I love cakes','I like pizzas']},
    {'username':'carla','tweets':['I love cats','I hate pizzas']},
    {'username':'juan','tweets':['I want to travel']},
    {'username':'zezinho','tweets':[],'colour':'yellow'},
    {'username':'antony','tweets':[]},
    {'username':'bruna','tweets':[]}    
]

print(users)
print(sorted(users)) -> Error
print(sorted(users,key=lambda user: user['username']))
print(sorted(users,key=lambda user: len(user['tweets']) ))

musics=[
    {'title':'Thunderstcuk','played':3}
    {'title':'Dead Skin Mask','played':1}
    {'title':'Back in Black','played':2}
    {'title':'Too old to rock in roll, too young to die','played':32}
]
print(sorted(musics,key=lambda music: music['played']))
print(sorted(musics,key=lambda music: msuic['played'], reverse = True))

-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

    Min e Max

Max() -> Return the max value in a iterable or between two values
list=[1,2,3,5,22,4,5,66]
print(max(list))

tuple=(1,2,3,5,22,4,5,66)
print(max(tuple))

set={1,2,3,5,22,4,5,66}
print(max(set))

dictionary={'a':1,'b':2,'c':3,'d':5,'e':22,'f':4,'g':5,'h':66}
print(max(dictionary.values()))

print(max(3,35))

print(max(4,75,204))

print(max('a','bd','adf'))

print(max('a','b','c','g'))

print(max(3.145,0.4395))

print(max('A sentence is long or are small'))

-> min() is the opposite of the small, everyworks on both

names = ['Arya','Samson','Dora','Tim','Ollivander']

print(max(names)) -> Tim
print(min(names)) -> Arya

print(max(names,key=lambda name: len(namex)))

-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

    Reversed

Its not the same as reverse()

reverse() only works in lists
reversed() works ith any iterable
return an interable list reverse iterator type

list1 = [1,2,3,4,5]
res= reversed(list1)
print(list(res))
print(type(res))

for letter in reversed('a word random cat'):
    print(letter,end='')
    
print(''.join(list(reverse('a word random cat'))))

print('a word random cat'[::-1])

for n in reversed(range(0,10)):
    print(n)

for n in range(9,-1,-1):
    print(n)
    
-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

    Len sum abs round

len() -> Return the lenght of a iterable
- Works for list/tuple/set/dict/range

Dunder len
print('A random cat'.__len__())

abs() -> Return the absolute value of a real number
print(abs(-5))
print(abs(5))
print(abs(3.14))
print(abs(-3.14))

sum() -> Receive an interable and/ or and not a initial value

list2=[1,2,3,4,5]

print(sum(list2))
print(sum(list2,5))

print(sum({'a':1,'b':2,'c':3,'d':4,'e':5}.values()))

round() -> Return a number rounded to a n decimal place, if decimal place
is not informed, will return an integer

print(round(10.234))
print(round(10.43,1))
print(round(10.212121212,3))

-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

    ZIP

zip() -> Mix two lists into odd numbers using the same index of both lists

list1=[1,2,3]
list2=[4,5,6]

zip1=zip(list1,list2)
zip2=zip(list1,list2,'abc')

print(zip1)
print(list(zip1))
print(set(zip1))
print(tuple(zip1))
print(dict(zip(list1,list2)))
print(type(zip1))

-> zip use the lowest lenght of a iterable

list3=[7,8,9,10,11]
print(list(zip(list1,list2,list3)))

data = [[0,1],[1,2],[2,3],[3,4],[4,5]]
print(list(zip(*data)))

grade1=[89,58,90]
grade2=[55,50,80]

student=['maria','pedro','carla']

final={data[0]: max(dado[1],data[2]) for data in zip(student,grade1,grande2)}


"""
