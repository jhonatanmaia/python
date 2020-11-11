"""
Lists

List is like a vector or matriz, but its dynamic and accept any value

Dynamic -> It can be of any size

list01=[1,2,'Something',True]

You can split every word in a sentence
test01=list('String')

teste02=[1,2,3,4,5]

if 5 in teste02:
    print('There is 5')
    
list.sort() -> Sorte a list even a string

list.count('number/letter') -> Count how many times the specific parameters
appears in the list

list.append(otherlist/number/string) -> Add something to a list in the
the last index

list.append([1,2,3]) -> Add a lsit inside a list

list.extend([1,2,3]) -> Add only the numbers inside a list
- Extend only accept a list/tuple

list.insert(index to insert, value) -> Add a value in a specific index

list.reverse() -> Reverse the whole list, its the same as list[::-1]

list0 = list.copy() -> Copy a list

len(list) -> List length

list.pop() -> Remove the last element of a list and return the removed element
list.pop(index) -> Remove a specific index and return it
- If there is no element in a specific index, return a error

list.clear() -> Clean all the list

To repeat the elemtns in a list we use
new=[1,2,3]
new *=3

String to list
str='A string'
str=str.split()

Get together a list with a space
list6=['one','two','three']
course= ' '.join(lista6)
print(course)

for index, value in enumerate(list):
    print(index,value)

a list accept a repated value

list.index(value,start,end) -> Find the index of a value

List slice
list(begin:end:step)

converting a lsit to tuple
tuple(list)

unpacking a list
list=[1,2,3]
num1,num2,num3 = list

Deep Copy

list=[1,2,3]
new = list.copy()
after the copy, the two lists are independents

Shallow Copy
list=[1,2,3]
new_list=list
its a mirror of a copy, if you change one, the other one will change

"""
