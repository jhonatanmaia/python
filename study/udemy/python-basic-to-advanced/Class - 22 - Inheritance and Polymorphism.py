"""

    Inheritance

The idea of inheritance is to reuse and exted our classes
other class can inheritance atributtes from other class

class Client:
    
    def __init__(self,name,lastname,document,salary):
        self.__name = name
        self.__lastname = lastname
        self.__document = document
        self.__salary = salary
    
    
    def full_name(self):
        return f'{self.__name} {self.__lastname}'


class Employee:
    
    def __init__(self,name,lastname,document,registration_number):
        self.__name = name
        self.__lastname = lastname
        self.__document = document
        self.__registration_number = registration_number
    
    
    def full_name(self):
        return f'{self.__name} {self.__lastname}'
    

When a class inheritance from another one, it gets everything, 
all attributes and methods

when a class is inherited, the class inherited is called:
    [Person]
    - Super Class
    - Mother Class
    - Father Class
    - Base Class
    - Generic Class

the class that inherited the other one, its called:
    [Client, Employee]
    - Sub Class
    - Daughter Class
    - Specific Class

class Person:
    def __init__(self,name,lastname,document):
        self.__name = name
        self.__lastname = lastname
        self.__document = document
        
        
        
    def full_name(self):
        return f'{self.__name} {self.__lastname}'
    
   
# client inheritance from person
class Client(Person):
    
    def __init__(self,name,lastname,document,salary):
        Person.__init__(name, lastname, document) # Unusual way
        self.__salary = salary


# client inheritance from person
class Employee(Person):
    
    def __init__(self,name,lastname,document,registration_number):
        super().__init__(name, lastname, document) # Usual way
        self.__registration_number = registration_number


client1 = Client('Maria', 'Test', '123', 1200.00)
employee1 = Employee('Robot', 'Test', '5948', 1)

print(client1.full_name())
print(client1.__dict__)
print(employee1.full_name())
print(employee1.__dict__)

# Overriding

# It happens when we re write the same method from a super class

class Person:
    def __init__(self,name,lastname,document):
        self.__name = name
        self.__lastname = lastname
        self.__document = document
        
        
        
    def full_name(self):
        return f'{self.__name} {self.__lastname}'
    
   
# client inheritance from person
class Client(Person):
    
    def __init__(self,name,lastname,document,salary):
        Person.__init__(name, lastname, document) # Unusual way
        self.__salary = salary
    
    
    def full_name(self):
        print(super().full_name())


# client inheritance from person
class Employee(Person):
    
    def __init__(self,name,lastname,document,registration_number):
        super().__init__(name, lastname, document) # Usual way
        self.__registration_number = registration_number


client1 = Client('Maria', 'Test', '123', 1200.00)
employee1 = Employee('Robot', 'Test', '5948', 1)

print(client1.full_name())

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    Properties

Getter -> Get the values of private attributes
Setter -> Change/Set new value to a private attribute

JAVA WAY

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
        self.__balance -= value
        destiny.__balance += value
    
    
    # Get the value, then we can use it
    def get_number(self):
        return self.__number
    
    
    def get_balance(self):
        return self.__balance
    
    
    def get_limit(self):
        return self.__limit
    
    
    def set_limit(self,limit):
        self.__limit = limit
    
    
    def get_client(self):
        return self.client
    
    
    def set_client(self,client):
        self.__client = client


a1=Account(2000, 100, 'Robot 1')
a2=Account(3000, 500, 'Robot 2')

a1.current_balance()
a2.current_balance()

sum_balance = a1.get_balance()+a2.get_balance()

print(f'Total Money: {sum_balance}')

a1.set_limit(5000)
a1.current_balance()


PYTHON WAY

class Account:
    
    count = 4999
    
    def __init__(self,limit,balance,client):
        self.__number = Account.count + 1
        self.__limit = limit
        self.__balance = balance
        self.__client = client
        Account.count = self.__number
    
    @property
    def number(self):
        return self.__number
    
    
    @property
    def limit(self):
        return self.__limit
    
    
    @limit.setter
    def limit(self,new_limit):
        self.__limit=new_limit
    
    
    @property
    def balance(self):
        return self.__balance
    
    
    @property
    def client(self):
        return self.__client
    
    
    def current_balance(self):
        print(f'The balance is {self.__balance} with limit of {self.__limit}')
    
    
    def deposit(self,value):
        self.__balance += value
    
    
    def withdraw(self,value):
        self.__balance -= value


    def transfer(self,value,destiny):
        self.__balance -= value
        destiny.__balance += value
    
    
    # We can creat our own property
    @property
    def tot(self):
        return self.__limit+self.__balance

    

a1=Account(2000, 100, 'Robot 1')
a2=Account(3000, 500, 'Robot 2')

a1.current_balance()
a2.current_balance()

sum_bank=a1.balance+a1.balance

print(f'Bank Money: {sum_bank}')

print(a1.__dict__)
a1.limit=9999
print(a1.__dict__)

print(a1.tot)

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    super() Method

-> Super Class - super()

class Animal:
    
    def __init__(self,name,species):
        self.__name = name
        self.__species = species
    
    
    def animal_sound(self,sound):
        print(f'The animal {self.__name} says {sound}')


class Cat(Animal):
    
    def __init__(self, name, species, breed):
        # Animal.__init__(self,name,species)
        super().__init__(name, species)
        self.__breed = breed


test = Cat('Felix','Feline','Tiger')

test.animal_sound('meow')

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    Multi inheritance
    
Two ways

Direct multi derivatives 


class Test1:
    pass


class Test2:
    pass


class Test3:
    pass


class MultiDerivations(Test1,Test2,Test3):
    pass


Indirect multi derivatives

class Test1:
    pass


class Test2(Test1):
    pass


class Test3(Test2):
    pass


class MultiDerivations(Test3):
    pass


class Animal:
    
    def __init__(self,name,species):
        self.__name = name
        self.__species = species
    
    
    def animal_sound(self,sound):
        print(f'The animal {self.__name} says {sound}')


class Cat(Animal):
    
    def __init__(self, name, species, breed):
        # Animal.__init__(self,name,species)
        super().__init__(name, species)
        self.__breed = breed


class Aquatic(Animal):
    
    def __init__(self,name,species):
        super().__init__(name, species)
    
    
    def swim(self):
        return f'{self._Animal__name} is swmming.'
    
    
    def hi(self):
        return f'I am {self._Animal__name} from the sea.'
    
    
class Land(Animal):
    
    def __init__(self,name,species):
        super().__init__(name,species)
    
    
    def walk(self):
        return f'{self._Animal__name}.'
    
    
    def hi(self):
        return f'I am {self._Animal__name}.'


# The order that you import matter!
class Penguin(Aquatic,Land):
    
    def __init__(self,name,species):
        super().__init__(name,species)



whale = Aquatic('Wally','Whale')
print(whale.swim())
print(whale.hi())

armadillo = Land('Xim','Armadillo')
print(armadillo.walk())
print(armadillo.hi())

tux = Penguin('Tux','Imperial')
print(tux.swim())
print(tux.walk())
print(tux.hi())

print(f'Tux is intance of Penguin? {isinstance(tux,Penguin)}')
print(f'Tux is intance of Aquatic? {isinstance(tux,Aquatic)}')
print(f'Tux is intance of Land? {isinstance(tux,Land)}')
print(f'Tux is intance of Animal? {isinstance(tux,Animal)}')
print(f'Tux is intance of object? {isinstance(tux,object)}')
# A class without inheritance has object inherited example
class Test1:
    pass


class Test2(object):
    pass


-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    MRO - Method Resolution Order
    
Its about of who is going to execute first
To see the order use Penguin/ClassName.__filename__ in print()
Other way is ClassName.filename()
other way is help(ClassName)
 
class Animal:
    
    def __init__(self,name,species):
        self.__name = name
        self.__species = species
    
    
    def animal_sound(self,sound):
        print(f'The animal {self.__name} says {sound}')


class Cat(Animal):
    
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.__breed = breed


class Aquatic(Animal):
    
    def __init__(self,name,species):
        super().__init__(name, species)
    
    
    def swim(self):
        return f'{self._Animal__name} is swmming.'
    
    
    def hi(self):
        return f'I am {self._Animal__name} from the sea.'
    
    
class Land(Animal):
    
    def __init__(self,name,species):
        super().__init__(name,species)
    
    
    def walk(self):
        return f'{self._Animal__name}.'
    
    
    def hi(self):
        return f'I am {self._Animal__name}.'


# The order that you import matter!
class Penguin(Aquatic,Land):
    
    def __init__(self,name,species):
        super().__init__(name,species)



tux = Penguin('Tux','Imperial')
print(tux.hi())

class Penguin2(Land,Aquatic):
    
    def __init__(self,name,species):
        super().__init__(name,species)


tux2 = Penguin2('Tux','Imperial')
print(tux2.hi())


   
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    Polymorphism

Poly -> Manys
Morphis -> Forms/Shapes/Something like that from Latin

Basicaly polumorphism is override

class Animal:
    
    def __init__(self,name):
        self.__name = name
    
    
    def animal_sound(self):
        raise NotImplementedError('Sub Class needs to implement this method')
        
    
    def eat(self):
        print(f'{self.__name} is eating.')


class Dog(Animal):
    
    def __init__(self,name):
        super().__init__(name)
    
    
    def speaks(self):
        print(f'{self._Animal__name} speaks au au')
    

class Cat(Animal):
    
    def __init__(self,name):
        super().__init__(name)
    
    
    def speaks(self):
        print(f'{self._Animal__name} speaks meow')


class Rat(Animal):
    
    def __init__(self,name):
        super().__init__(name)
    
    
    def speaks(self):
        print(f'{self._Animal__name} say something')



dog1 = Dog('Test Dog')
cat1 = Cat('Test Cat')
rat1 = Rat('Test Rat')

dog1.speaks()
cat1.speaks()
rat1.speaks()

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    Magic Methods
    
Its all the methods with __ dunder

You can find by using dir(__builtins__) or dir(objects)

dunder init -> __init__
dunder repr -> Object Representation
class Book2:
    
    def __init__(self,title,author,pages):
        self.title =  title
        self.author = author
        self.pages = pages
    
    
    # Representation, apresentation of your object
    def __repr__(self):
        return self.title

dunder __str__ -> Its the same as repr, but its for the user and has priority
class Book:
    
    def __init__(self,title,author,pages):
        self.title =  title
        self.author = author
        self.pages = pages

    
    def __str__(self):
        return self.title


book1 = Book('Python Rocks','Someone',10)
book2 = Book('Math','Its already dead',200)

print(book1)
print(book2)


dunder __len__ -> You define the lenght of your object
class Book:
    
    def __init__(self,title,author,pages):
        self.title =  title
        self.author = author
        self.pages = pages

    
    def __str__(self):
        return self.title


    def __len__(self):
        return self.pages


book1 = Book('Python Rocks','Someone',10)
book2 = Book('Math','Its already dead',200)

print(book1)
print(book2)
print(len(book1))
print(len(book2))

dunder __del__ -> You can print or do something when a object is removed

class Book:
    
    def __init__(self,title,author,pages):
        self.title =  title
        self.author = author
        self.pages = pages

    
    def __str__(self):
        return self.title


    def __len__(self):
        return self.pages
    
    
    def __del__(self):
        print('A object was deleted from the memory')


book1 = Book('Python Rocks','Someone',10)
book2 = Book('Math','Its already dead',200)

del book1


dunder __add__ -> You can add two strings or something you want to

class Book:
    
    def __init__(self,title,author,pages):
        self.title =  title
        self.author = author
        self.pages = pages

    
    def __str__(self):
        return self.title


    def __len__(self):
        return self.pages
    
    
    def __del__(self):
        print('A object was deleted from the memory')


    def __add__(self,other):
        return f'{self} - {other}'



book1 = Book('Python Rocks','Someone',10)
book2 = Book('Math','Its already dead',200)

print(book1+book2)


dunder __mul__ -> You can multiply something

class Book:
    
    def __init__(self,title,author,pages):
        self.title =  title
        self.author = author
        self.pages = pages

    
    def __str__(self):
        return self.title


    def __len__(self):
        return self.pages
    
    
    def __del__(self):
        print('A object was deleted from the memory')


    def __add__(self,other):
        return f'{self} - {other}'


    def __mul__(self,other):
        if isinstance(other,int):
            msg=''
            for n in range(other):
                msg += ' ' + str(self)
            return msg
        return 'I cant multiply'



book1 = Book('Python Rocks','Someone',10)
book2 = Book('Math','Its already dead',200)

print(book1*2)

"""
