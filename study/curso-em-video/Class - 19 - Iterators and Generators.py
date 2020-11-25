"""

    Understanding Interators and Itarables

Iterator -> It's a object that can be interable
         -> A object that returns a data, when next() function is called
- String # its a itarable not an interator
- List # the same
- Tuple
- Dictionary


Iterable -> A object that returns an interator when iter() function is called

Iterable return an interator that returns a data

name = 'ab'
print(next(name))
numbers = [1,2,3,4,5]
print(next(numbers))

it1 = iter(name)
it2 = iter(numbers)

print(next(it1))
print(next(it1))

print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))

for letter in name:
    print(letter)
    
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    Creating your own loop version

def my_for(iterable):
    it = iter(iterable)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break


my_for([1,2,3,4,5])
my_for('a string to print')

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    Writing a custom iterator

class Count:
    def__init_(self,less,higher):
        self.less = less
        self.higher = higher
    
    def__iter__(self):
        return self
    
    def__next__(self):
        if self.less < self.higher:
            number = self.menor + 1
            return number
        raise StopIteration
            


for n in Count(1,61):
    print(n)

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    Generators

-> Generators are Iterators but not all iterator is a generator
-> Generators can be created with generators functions
-> Generators functions use the reserved word yield
-> Generators can be created with generators expressions

-------------------------------------------------------------------------------
/ Functions                             / Generators Functions                /
------------------------------------------------------------------------------
Use return                              Use yield
return only one time                    Multiples yields
When executed, return a value           return a generator

Examples

Generator Function
Generate a generator, its not a generator

def cont(max_value):
    c = 1
    while c <= max_value:
        yield c
        c += 1


gen=cont(5)
print(type(gen))

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

you can put everything in a list

a = list(next(cont(10)))

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    Memory Test with Generators

def fib_list(max):
    num = []
    a, b = 0, 1
    while len(num) < max:
        num.append(b)
        a,b = b, a+b
    return num


for i in fib_list(100):
    print(i,end=' ')

def fib_gen(max):
    a, b, count = 0,1,0
    while count < max:
        a,b = b, a+b
        yield a
        count += 1
        

for i in fib_gen(100_00):
    print(i,end=' ')
    
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    Speed Test

# Generators
def num1():
    for num in range(1,10):
        yield num


ge1 = num1()
print(ge1)
print(next(g1))
print(next(g1))

Generator Expression
ge2 = (num for num in range(1,10))

print(ge2)

print(next(ge2))
print(next(ge2))


import time

Generator Expression

gen_init = time.time()
print(sum(num for num in range(100_000_000)))
gen_time= time.time()-gen_init

List Comprehension

list_init = time.time()
print(sum([num for num in range(100_000_000)]))
list_time = time.time() - list_init

print(f'Generator {gen_time}')
print(f'List {list_time}')

"""
