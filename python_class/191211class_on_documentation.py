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
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable): 
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method 

class MappingSubclass(Mapping):
    
    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)
           

# Iterators 


# most container objects can be looped over using a for statement. 

for element in [1, 2, 3]:  # Loop over a list 
    print(element)
for element in (1, 2, 3):  # Loop over a tuple 
    print(element)
for key in {'one': 1, 'two': 2}: # Loop over a dictionary 
    print(key)
# for line in open("myfile.txt"):
#   print(line, end='')

s = 'abc'
it = iter(s)
print(it)
print(next(it))
print(next(it))
print(next(it))
# print(next(it))


class Reverse: 
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1 
        return self.data[self.index]

rev = Reverse('spam')
print(iter(rev))

for char in rev:
    print(char)

def reverse(data):
    for index in range(len(data)-1, -1, -1): 
        yield data[index]

for char in reverse('golf'):
    print(char)


