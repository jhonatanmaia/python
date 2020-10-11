import random

n1=input("Name one: ")
n2=input("Name two: ")
n3=input("Name three: ")
n4=input("Name four: ")

lista=[n1,n2,n3,n4]

print("1 - {} \n2 - {} \n3 - {} \n4 - {}".format(n1, n2,n3,n4))
print("The apresentation order is: {}".format(random.randint(1,4)))

random.shuffle(lista)
print(lista)