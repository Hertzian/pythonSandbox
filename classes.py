# A class is like a blueprint for crfeating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Creae class
class User:
    # Contructor
    def __init__(self, name, email,age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'

    def hasBirthday(self):
        self.age += 1

# Customer class
class Customer(User):
    def __init__(self, name, email,age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def setBalance(self,balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and I owe a balance of {self.balance}'
        

# Init user object
lalo = User('Lalo Aguilar','tallitosan@gmail.com',36)
brad = User('Brad Traversy','brad@gmail.com',37)

# edit property
lalo.age = 35

lalo.hasBirthday()

# call method
print(lalo.greeting())

# Init customer
john = Customer('John Doe','john@gmail.com',40)

john.setBalance(500)

print(john.greeting())
