"""

    OOP

- OOP is a coding paradigm what uses real world object mappings for
computers models
- Coding paradigm is the way/methodology used to think/develop systems

OOP
- Class -> Real world object represented in a computer
- Atribute -> Object characteristics
- Method -> Object behavior, functions
- Constructor -> Especial methods to creat objects
- Object -> Classes instances

c = 10
print(c)
print(type(c))

d='a'
print(d)
print(type(d))

class Product:
    pass # A real continue


ps4 = Product()
print(ps4)
print(type(ps4))

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    Classes

-> Its objects to a computer

Example Lamp
- Atributes - Its the object characteristics. Lamp: 110v or 220v, white/black
/yellow/red or other color, is it led?
- Methods - Its functions about the object behavior. Lamp: On and Off

In python to declare a class we use the restrict word class

We use pass when we didnt finished a class but we want to use it

The class name is always title name: class NameClass

class Lamp:
    pass


class Something:
    pass


led_lamp=Lamp()
print(type(led_lamp))

Python has classes in lower case

A object that we will mapping to our classe we call it entity

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    Atributes

- It is the object characteristics

Three types of atributes
- Instance Atributes
- Class Atributes
- Dynamic Atributes

    -> Instance Atributes - Its the constructor -> __init__
    - Special method used to build the object

class Lamp:
    
    def __init__(self,volt,color):
        # self = object. At the begin we say: the object(self) receives
        # in the atribute volt the value volt, the atribute color receive
        # the value color and so on
        self.volt = volt
        self.color = color
        self.on = False
    

class BankAccount:
    
    def __init__(self, number,limit,balance):
        self.number = number
        self.limit = limit
        self.balance = balance


class Product:
    
    def __init__(self,name,description,value):
        self.name = name
        self.description = description
        self.value = value


class User:
    
    def __init__(self,name,email,password):
        self.name = name
        self.email = email
        self.password = password


In python, by convention every class atributte is public, it can be accessed
everywhere
If we want a private atributte we use __nameAtribute or Name Mangling

class Access:
    
    def __init__(self,email,password):
        self.email = email
        self.__password = password
    
    
    def show_password(self):
        print(self.__password)
    
    
    def show_email(self):
        print(self.email)


user = Access('test@test.com','tooeasytobreak')

print(user.email)
#print(user.__password) #AttributeError
print(user._Access__password) # you can use private atributes
user.show_password()
user.show_email()

# Instance Atributes means that when we creat a object/instance of a class,
# every instance will have this atributes

user1 = Access('user1@test.com', '123')
user2 = Access('user2@test.com', '456')

user1.show_email()
user2.show_email()

    # Class Atribute

p1 = Product('PS4', 'Video Game', 200)
p2 = Product('Xbox', 'Video Game', 190)

# Class Atribute are declared in class, out of the constructor.
# Usually we give them a value and its shared with whole class

class ProductClassAtribute:
    
    # Class Atribute
    tax = 1.05
    count = 0
    
    # You dont pass the id value in the function because its not the user
    # that will define the product id
    def __init__(self,name,description,value):
        self.id = ProductClassAtribute.count + 1
        self.name = name
        self.description = description
        self.value = (value * ProductClassAtribute.tax)
        ProductClassAtribute.count = self.id


p11 = ProductClassAtribute('PS4', 'Video Game', 200)
p22 = ProductClassAtribute('Xbox', 'Video Game', 190)

print(p1.value)
print(p11.value)
print(p2.value)
print(p22.value)

# Possible way, but not the correct one to access a class attribute
print(p11.tax)
# Correct way
print(ProductClassAtribute.tax)

print(p11.id)
print(p22.id)

class Lamp:
    
    def __init__(self,volt,color):
        # self = object. At the begin we say: the object(self) receives
        # in the atribute volt the value volt, the atribute color receive
        # the value color and so on
        self.volt = volt
        self.color = color
        self.on = False
    

class BankAccount:
    
    def __init__(self, number,limit,balance):
        self.number = number
        self.limit = limit
        self.balance = balance


class Product:
    
    def __init__(self,name,description,value):
        self.name = name
        self.description = description
        self.value = value


# Public atributes
class UserPublic:
    
    def __init__(self,name,email,password):
        self.name = name
        self.email = email
        self.password = password
        

# Private atributes
class UserPrivate:
    
    def __init__(self,name,email,password):
        self.__name = name
        self.__email = email
        self.__password = password


class Access:
    
    def __init__(self,email,password):
        self.email = email
        self.__password = password
    
    
    def show_password(self):
        print(self.__password)
    
    
    def show_email(self):
        print(self.email)


# Dynamic Atributes
# Its an instance atribute that can be created when executed
# The dynamic atribute will be private only to that instance

class ProductClassAtribute:
    
    # Class Atribute
    tax = 1.05
    count = 0
    
    # You dont pass the id value in the function because its not the user
    # that will define the product id
    def __init__(self,name,description,value):
        self.id = ProductClassAtribute.count + 1
        self.name = name
        self.description = description
        self.value = (value * ProductClassAtribute.tax)
        ProductClassAtribute.count = self.id


p1 = ProductClassAtribute('Product','Something',100)
p2 = ProductClassAtribute('Other','a',500)

# Dynamic Atribute

p1.weight = '5kg'

print(f'Product {p1.name}, Description {p1.description}, Price {p1.value} Weight {p1.weight}')
#print(f'Product {p2.name}, Description {p2.description}, Price {p2.value} Weight {p2.weight}')

print(p1. __dict__)
print(p2.__dict__)
print(ProductClassAtribute.__doc__)

# Dynamic Delet
del p1.weight
del p2.value
del p2.description

print(p1. __dict__)
print(p2.__dict__)

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    Methods

Its functions inside a class. Its the object behavior in its systens

Instance Method
Class Method

# The method __init__ dundle init, its a special method called constructor
# its function is to creat the object in the class
# Methods/functions called dunder its magic method

# You can creat a magic method __something__ but its not recommended

class Dog:
    
    def __init__(self,breed,color,age):
        self.__breed = breed
        self.__color = color
        self.age = age
        self.sleeping = False
 

class Cat:
    
    def __init__(self,breed,color,age):
        self.__breed = breed
        self.__color = color
        self.age = age
        self.sleeping = False
    
    
    def information(self,name):
        self.name = name
        return print(f'Cat Name: {self.name}')
    

from passlib.hash import pbkdf2_sha256 as cryp # cryptography password
    
class PetShop:
    
    animals = 0
    shower_price = 30
    
    #Here we dont access atributes. Class Method are called Static Methods
    # in other programing languages
    @classmethod
    def count_users(cls):
        print(f'CLS: {cls}')
        print(f'We have {cls.animals} animals in this PetShop')
    
    
    # we dont access anything
    @staticmethod
    def definition():
        return 'Starting'
    
    
    # Here we access the class atribute with self
    def __init__(self,useremail,password):
        self.__useremail = useremail
        self.__password = cryp.hash(password, rounds=200000,salt_size=16)
        print(f'User: {self.__generate_user()} created.')
    
    
    def check_login(self,password):
        if cryp.verify(password,self.__password):
            return True
        return False
        
    
    def animal_register(self,species,breed,color):
        self.__space = PetShop.animals = +1
        self.__species = species
        self.__breed = breed
        self.__color = color
        PetShop.animals = self.__space
       
        
    def discount(self,percentage):
        '''Return a prince with discount'''
        return PetShop.shower_price - PetShop.shower_price * (percentage/100)
    
    
    #private methods
    def __generate_user(self):
        return self.__useremail.split('@')[0]
    
    
mycat = Cat('British Shorthair', 'Gray', 2)

mycat.information('Jose')

user1 = PetShop('jose@test.com', '12345')

# wrong way, the correct way is inside the clas
print(user1._PetShop__generate_user())

print(user1.check_login('12345'))
# if the login is wrong we can use exit(code error we want) to stop the program
print(user1.discount(20))

print(user1._PetShop__password)

user1.animal_register('Cat', 'British Shorthair', 'Gray')
user1.animal_register('Dog', 'Golden Retriver', 'Caramel')

# Wrong way to access the class method
user1.count_users()
# Correct way
PetShop.count_users()

# Statical Method

print(user1.definition())

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    Objects

Objects are classes instances
We can creat as many as we want to

class AnyAnimal:
    pass


The dog is the object/instance
dog = AnyAnimal(whatever)

class Account:
    
    count = 4999
    
    def __init__(self,limit,balance,client):
        self.__number = Account.count + 1
        self.__limit = limit
        self.__balance = balance
        self.__client = client
        Account.count = self.__number
    
    
    def show_client(self):
        print(f'The cliente is {self.__client._User__name}')
        

class User:
    
    def __init__(self,name,lastname,email,password):
        self.__name = name
        self.__lastname = lastname
        self.__email = email
        self.__password = password
        
        

client1 = User('Jose','Santos','a@test.com','123')

account_cliente=Account(5000, 1000, client1)

account_cliente.show_client()

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    Abstraction and Encapsulation

The class is like a capsule and the attributes and methods are what is inside

Abstracion -> We hide datas(methods) irrelevants from the user and show only 
the methods we want 

class Account:
    
    count = 4999
    
    def __init__(self,limit,balance,client):
        self.number = Account.count + 1
        self.limit = limit
        self.balance = balance
        self.client = client
        Account.count = self.number
    
    
    def current_balance(self):
        print(f'The balance is {self.balance} with limit of {self.limit}')
    
    
    def deposit(self,value):
        self.balance += value
    
    
    def withdraw(self,value):
        self.balance -= value


account01 = Account(2000, 100, 'Jose')

print(account01.number)
print(account01.client)
print(account01.limit)
print(account01.balance)

account01.number = 42
account01.client = 'Dog'
account01.limit = 99999
account01.balance = 999999999

print(account01.__dict__)

account01.current_balance()

class Account:
    
    count = 4999
    
    def __init__(self,limit,balance,client):
        self.__number = Account.count + 1
        self.__limit = limit
        self.__balance = balance
        self.__client = client
        Account.count = self.__number
    
    
    def current_balance(self):
        print(f'The balance is {self.__balance} with limit of {self.__limit}')
    
    
    def deposit(self,value):
        self.__balance += value
    
    
    def withdraw(self,value):
        self.__balance -= value


    def transfer(self,value,destiny):
        # removing the balance
        # we can add a transfer tax
        self.__balance -= value
        # adding the value
        destiny.__balance += value
        
        
account01 = Account(2000, 100, 'Jose')

print(account01.__dict__)

account01.current_balance()

print(account01._Account__client)

account01._Account__client = 'Dog'

print(account01.__dict__)

account01.deposit(200)

print(account01.__dict__)

account01 = Account(2000, 100, 'Jose')
account02 = Account(1000, 300, 'Maria')

account02.transfer(100, account01)

account01.current_balance()
account02.current_balance()

"""
