"""
Module Collections - Counter

Collections -> High-performance Container Datetypes

Counter -> Receive an interable as a parameter and create a Collections Counter
type, that is similar as a dict. Contains the key, that is the element or
parameter entered. And the value is the appearance frequency

from collections import Counter
a=[1,1,1,12,3,4,5,5,6,5,3,5,7,8,6,5,5,44,5,7,20,3,5,6,7,4,40]
res=Counter(a)
print(type(res))
print(res)

print(Counter('A String of Something Else Repeated Two Three Four'))

text = '''Ida Tarbell (November 5, 1857 – January 6, 1944) was an American 
writer, journalist, biographer and lecturer. One of the leading muckrakers of 
the Progressive Era of the late 19th and early 20th centuries, she pioneered 
investigative journalism. Her best-known exposé was of the Standard Oil 
Company, run at the time by oil tycoon John D. Rockefeller. This inspired other 
journalists to investigate and write about trusts, large businesses that 
(in the absence of strong antitrust laws in the 19th century) attempted to 
gain monopolies in various industries. She also wrote biographies of 
businessmen Elbert Henry Gary, chairman of U.S. Steel, and Owen D. Young, 
president of General Electric.'''

words = text.split()
rest=Counter(words)
print(rest)

Printing the msot commons words
print(rest.most_commons(5))

-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

Module Collections - Default Dict

dict1={'one':1,'two':2}
print(dict1['one'])
print(dict1['three']) -> KeyError

Default Dict -> A default value informed will be print if not find it. If
the key doesnt exist, will create and the default value will be assigned

from collections import defaultdict

dict2=defaultdict(lambda:0)

dict2['a']=10

print(dict2['b'])

-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

Module Collections: Ordered Dict

from collections import OrderedDict

In dictionary. the order is not garanted
dictionary = {'a':1,'b':2,'c':3,'d':4,'e':5}

dictionary2 = OrderedDict({'a':1,'b':2,'c':3,'d':4,'e':5})

dict_1 = {'a':1,'b':2}
dict_2 = {'b':2,'a':1}

print(dict_1 == dict_2) -> True

odict1 = OrderedDict({'b':2,'a':1})
odict2 = OrderedDict({'a':1,'b':2})

print(odict1 == odict2) -> False

-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

Module Collections: Named Tuple

Convenient way to access the index

from collections import namedtuple

Declaration 1

dog1 = namedtuple('dog','age breed name')

Declaration 2

dog2 = namedtuple('dog','age, breed, name')

Declarion 3

dog3 = namedtuple('dog',['age','breed','name'])

a1=dog3(age=2,breed='Golden Retriver',name='Tucker')

print(a1[0]) -> Age
print(a1[1]) -> Breed
print(a1[2]) -> Name

print(a1.age) -> Age
print(a1.breed) -> Breed
print(a1.name) -> Name

print(a1.index('Tucker'))

print(a1.count('Golden Retriver'))

-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

Module Collections: Deque

from collections import deque

It's a list of high performance

deq = daque('geek')
print(deq)

Adding elemnts

deq.append('y') -> Add at the end

deq.appendleft('k') -> Add the first position

Removing elements

print(deq.pop()) -> Remove and return the last element

print(deq.popleft()) -> Remove and return the first element



"""
