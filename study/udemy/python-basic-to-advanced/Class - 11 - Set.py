"""
Set

-> Any language, Set Theory is the same as math
-> Python are the Sets

-> Sets doesn't have duplicate values instead keys of dict
-> Sets aren't ordered
-> It doen't have an index

Different between Sets and Maps(dict)

-> Dict has key/value
-> Sets has only value

s = set({1,2,3,4,5,5,6,7,8,2})
print(s)
print(type(s))
-> Repeated values are deleted

a = set('A String Of Something')

s.add(4)
s.add(4) -> It won't add and generate an error

s.remove(3) -> Not index, but value
If you remove a value that doesnt exist, will return a keyerror

s.discard(2) -> The same as remove but doesnt return error if not find a value

s.clear()

Deep Copy

b = s.copy()

Shallow Copy

c = s.copy()

Set Theory

Union

one={1,2,3,4,5,10,20}
two={10,20,30,40,50,2,3}
three=one.union(two)
print(three)

Using pipe |
four = one | two
print(four)

Intersection

five = one.intersection(two)
print(five)

Using &
six = one & two
print(six)

Opposite intersection

seven=one.difference(two)
print(seven)
eight=two.difference(one)
print(eight)

Last things if the values are real

print(sum(s))
print(min(s))
print(max(s))
print(len(s))
"""
