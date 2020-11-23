"""

    List Comprehension

We can creat a list from other processed interable

Sintax

[data for data in interable]

numbers = [1,2,3,4,5]

do something with each number in that list
rest = [number * 10 for number in numbers]

The same result as a loop

new_number=[]

for number in [1,2,3,4,5]:
    new_number.append(number*10)

print(new_number)

-=-

print(rest)

rest = [number / 2 for number in numbers]

print(rest)

rest = [number ** 100_000
        for number in numbers]

print(rest)

name = 'a little big something'

print([letter.upper() for letter in name])

def upper(name):
    name = name.replace(name[0],name[0].upper())
    return name


friends = ['maria','jose','zezão','jojo','clodoalda']

print(upper(friend) for friend in friends)

print([number * 3 for number in range(1,100)])


-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

Conditionals

Examples

n=[1,2,3,4,5]

even_numbers=[nu for nu in n if nu % 2 == 0]
odd_numbers=[nu for nu in n if nu % 2 != 0]

print(even_numbers)
print(odd_numbers)


-> Better way

# Any even number module of 2 is 0, and 0 in pytho nis false, not False = True
even=[number for number in n if not number % 2]
odd=[number for number in n if number % 2]

res = [number * 2 if number % 2 == 0 else number / 2 for number in n]

-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

    Nested List

- Some programing languages have array:
    unimensional (array/vectors)
    Multidimensional (matrizes)

In python we call list

lists = [[1,2,3],[4,5,6],[7,8,9]] # Matriz 3x3

-> Line 0 column 1
print(lists[0][1])

for l in lists:
    print(l)

for l in lists:
    for l1 in l:
        print(li)

[[print(value) for value in l] for l in lists]

generating a board

board = [[number for number in range(1,4)] for value in range(1,4)]
print(board)

hash_game=[['X' if number % 2 == 0 else 'O' for number in range(1,4)] for value in range(1,4)]
print(hash_game)

print([['*' for i in range(1,4)] for j in range(1,4)])

-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

    Dictionary comprehension

dictionary_1 = {'a':1,'b':2,'c':3,'d':4,'e':5}

double={key: value * 2 for key, value in dictionary_1.items()} 

print(double)

numbers = [1,2,3,4,5,1,2]

power = {value: value ** 2 for value in numbers}
print(power)

keys='abcde'
values=[1,2,3,4,5]

mix={keys[i]: values[i] for i in range(0, len(keys))}
print(mix)


numbers = [1,2,3,4,5]

res = {num: ('even' if num % 2 == 0 else 'odd') for num in numbers}

-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/

    Set Comprehension

numbers = {num for num in range(1,7)}
print(numbers)

numbers_2 = {x**2 for x in range(10)}
print(numbers_2)

numbers_2 = {x: x**2 for x in range(10)}

letters = {letters for letters in 'Something in the wall and the sky'}
print(letters)


"""
