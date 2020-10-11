import random

n1=input("Enter name one: ")
n2=input("Enter name two: ")
n3=input("Enter name three: ")
n4=input("Enter name four: ")
nameList=[n1,n2,n3,n4]
print("The choosed one is: {}".format(random.choice(nameList)))