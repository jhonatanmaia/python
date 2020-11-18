"""
loop -> repetition structure
for -> one of these structures

for item in variable:
    execute this

we use loops to iterate string sequence or interate other values
examples
- String
nome = 'Python'
- Lista
lista = [1,2,3,4,5]
- range
numbers = range(1,10)

name = 'Python'
for letters in name:
    print(letters)

number_list=[1,2,3,4,5]
for numbers in number_list:
    print(numbers)

range_number=range(1,10) # -> It will be a list
for numbers in range_number:
    print(numbers)

range(initial value, final value -1)
range will always finish with a value of minus 1
range(1,5) -> 1,2,3,4

    Index of a loop

to get the index and the value we do
for index, value in enumerate(variable)
name='Nice'
for index,value in enumerate(name):
    print(index)
    print(value)

We can discard a number using _
for _,value in enumerate(variable)

ITS DIFERENT
for value in enumerate(varible)
this will generate a dict

limit=int(input('Enter a number'))
for i in range(0,limit):
    print(i)


if you dont want a new line in print
for i in range(0,10):
    print(i,end='')
    
Emoji list https://www.unicode.org/emoji/charts/full-emoji-list.html
U+1F60D
change to U0001F60D
print('\U0001F60D')

Range always starts in zero
for num in range(11):
    print(num)

The third number is the step of range
fo num in range(5,55,5):
    print(num)

To convert a lsit to range use
list = list(range(10))

loop While

while boolean_expression:
    loop

While true, it will happening

Robots and games use

We use the break to finish a While loop 
"""
