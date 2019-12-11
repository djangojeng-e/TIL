def scope_test():
    
    def do_local():
        spam = "local spam"
    
    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    print("After local assignment: ", spam)         # "test spam"  
    do_nonlocal()
    print("After nonlocal assignment: ", spam)      # "nonlocal spam"
    do_global()
    print("After global assignment:", spam)         # "nonlocal spam"

scope_test()
print("In global scope: ", spam)                    # global spam 





class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)
print(x.r,x.i)


class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'

y = MyClass()
print(y.f())



# class Dog: 

#     kind = 'canine' # class variable shared by all instances 

#     def __init__(self, name):
#         self.name = name    # instance variable unique to each instance 

# d = Dog('Fido')
# e = Dog('Buddy')

# print(d.kind)   # Shared by all dogs 

# print(e.kind)   # Shared by all dogs 

# print(d.name)   # unique to d 

# print(e.name)   # unique to e 


# class Dog:

#     tricks = []     # mistaken use of a class variable 

#     def __init__(self, name):
#         self.name = name 

#     def add_trick(self, trick): 
#         self.tricks.append(trick)

# d = Dog('Fido')
# e = Dog('Buddy')
# d.add_trick('roll over')
# e.add_trick('played dead')

# print(d.tricks)



class Dog: 

    def __init__(self, name):
        self.name = name 
        self.tricks = []    # Creates a new empty list for each dog 

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')

print(d.tricks)

print(e.tricks)



class Warehouse: 
    purpose = 'storage'
    region = 'west'

w1 = Warehouse()
print(w1.purpose, w1.region)

w2 = Warehouse()
w2.region = 'east'

print(w2.purpose, w2.region)


# Function defined outside the class 

def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1 

    def g(self):
        return 'hello world'

    h = g 


class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x): 
        self.add(x)
        self.add(x)



class Mapping: 
    def __init__(self, iterable):    


