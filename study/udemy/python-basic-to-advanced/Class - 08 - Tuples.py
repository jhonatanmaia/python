"""
Tuples

Its similar to a list

There only two differences

1 - Tuple we use () not []

tuple1 = (1,2,3,4,5,6)
tuple2 = 1,2,3,4,5,6

2 - You can´t change a tuple after declared

tuple3 = (4) -> This isnt a tuple
tuple4 = (4,) -> This is a tuple

Obs: Tuples are defined by the comma not the parentheses

You can unpacking a tuple
tuple5 = (1,2)
a, b = tuple5

You cant delet elements of a tuple, but you can use the follows functions
sum(tuple5)
max(tuple5)
min(tuple5)
len(tuple5)

You can sum two tuples
tuple1 += tuple5

for index, value in enumerate(tuple1):
    print(index)

for n in tuple1:
    print(n)

tuple.count(element)

Why use tuples?
1 - Tuples are faster than lists
2 - Tuples make your code more secure*
* Like declaring months for example.

In tuples we dont have the problem of shallow copy 

"""
