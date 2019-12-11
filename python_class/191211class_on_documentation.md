# Classes 



Class should be one of the most difficult but important concept to understand. Classes provide a means of bundling data and functionality together. Creating a new class creates a **new type of object** allowing **new instances** of that type to be made. 



Each class instance can have attributes attached to it for maintaining its state. Class instance can also have methods (defined by its class) for modifying its state. 



 

# A word about Names and Objects



Objects have **individuality, and multiple names (in multiple scopes)** can be bound to the same object. 



When dealing **with immutable basic types (numbers, strings and tuples)**, this was not appreciated much. 





# Python Scopes and Namespaces



Before understanding about what's going on, understandings on how scopes and namespaces work are required. 



**A namespace is a mapping from names to objects.** 





![img](https://postfiles.pstatic.net/MjAxOTA5MjNfMjYg/MDAxNTY5MjI5MDQ2NTAy.fV9r_tdCWEjlsAhWiDYyCs3J1lvfW8RLDp6ygky3iZ4g.tz5w5XfPcvP0gl8yATsKPrhFScUubx_h-q-rwBaFL-sg.PNG.codeitofficial/namespace.png?type=w966)





Namespaces are created at different moments and have different lifetimes. The **namespace containing the built-in names is created when the Python interpreter starts** up. 



**The global namespace** for a module is created when the module definition is read in.  Module namespaces last until the interpreter quits. 



**The Local namespace** for a function is created when the function is called, and deleted when the function returns or raises an exception that is not handled with the function. 



A **scope** is a textual region of a Python program where a namespace is directly accessible.  



**At any time during execution, there are at least three nested scopes whose namespaces are directly accessible**



- The innermost scope, searched first contains the local names 
- The scopes of any enclosing functions, searched starting with the nearest enclosing scope, contains non-local but also non-global names 
- The next-to-last scope contains the current module's global names 
- The outermost scope (searched last) is the namespace containing built-in names. 



if a name is declared global, then all references and assignments go directly to the middle scope containing the module's global names. 



**Namespace and scopes are pretty difficult to understand. **

**Let's learn by example**



```python
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
```



The nonlocal assignment changed scope_test's binding of spam, and the global assignment changed the module-level binding. 





# Class definition 



```python
class ClassName: 
    <statement 1> 
    
    <statement N>
    
```



When a class definition is entered, a new namespace is created, and used as the local scope. Therefore, all assignments to local variables go into this new namespace. 



When a class definition is left normally, a class object is created. 



# Class objects 



**Class objects support two kinds of operations : attribute references and instanitation**



*Attribute references * use the standard syntax used for all attribute references in Python: **obj.name** . Valid attribute names are all the names that were in the class's namespace when the class object was created. So, if the class definition looked like this below. 



```python
class MyClass: 
    """A simple example class"""
    i = 12345 
    
    def f(self):
        return 'hello world'

# Valid attribute references 
# MyClass.i and MyClass.f are valid attribute references 
# Returning an integer 
# And a function object 

```





# Class instantiation



**Class instantiation uses function notation. Just pretend that the class object is a parameterless function that returns a new instance of the class. **



```python
x = MyClass()
```





This creates a new instance of the class and assigns this object to the local variable x. 



**The instantiation operation ("Calling" a class object) creates an empty object**

Many classes like to create objects with instances customised to a special initial state. 

Therefore, a class may define a special method named 



```python
def __init__(self): 
    self.data = []
    
# Class defines an __init__() method, 
# class instantiation automatically invokes 
# __init__() for the newly-created class instacne. 


# __init__() method may have arguments for greater flexibility. 
```







```python
class Complex: 
    def __init__(self, realpart, imagpart): 
        self.r = realpart
        self.i = imagpart 
        
x = Complex(3.0, -4.5) 
print(x.r,x.i)
```





# Instance Objects



There are two kinds of valid attribute names, **data attributes and methods** 



**Data Attributes correspond to "Instance variables"** 

**Attribute Reference corresponds to method** - function that belongs to an object. 



**Difference between method object and function object**





# Method objects 







```python
class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'

y = MyClass()
print(y.f())
```





When a method is called, y.f() was called without an argument above. What happened to the argument? 



**The special thing about methods is that the instance object is passed as the first argument of the function.**



## **The call y.f() is equivalent to MyClass.f(y) **



When a non-data attribute of an instance is referenced, the instance's class is searched. If the name denotes a valid class attribute that is a function object, a method object is created by packing (pointers to) the instance object and the function object just found together in an abstract object. This is the method object. 





# Class and Instance Variables 



Instance variables are for data unique to each instance and class variables are for attributes and methods shared by all instances of the class. 





```python
class Dog: 

    kind = 'canine' # class variable shared by all instances 

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance 

d = Dog('Fido')
e = Dog('Buddy')

print(d.kind)   # Shared by all dogs 

print(e.kind)   # Shared by all dogs 

print(d.name)   # unique to d 

print(e.name)   # unique to e 
```





**Shared Data can have possibly surprising effects when involving mutable objects such as lists and dictionaries.**



Shared Data could arise unintended results or so. 



```python
class Dog:

    tricks = []     # mistaken use of a class variable 

    def __init__(self, name):
        self.name = name 

    def add_trick(self, trick): 
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('played dead')

print(d.tricks)
```





**Correct design of the class above should use an instance variable instead.**





```python
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
```





# Random Remarks 



If the same attribute name occurs in both an instance and in a class, then attribute lookup prioritises the instance 





```python
class Warehouse: 
    purpose = 'storage'
    region = 'west'

w1 = Warehouse()
print(w1.purpose, w1.region)

w2 = Warehouse()
w2.region = 'east'

print(w2.purpose, w2.region)
```





Data attributes may be reference by methods as well as by ordinary users of an object. 



Classes are not usable to implement pure abstract data types. **Nothing in Python makes it possible to enforce data hiding**



The users of an object (clients) should use data attributes with care - clients may mess up invariants maintained by the methods by stamping on their data attributes. **NB : clients may add data attributes of their own to an instance object without affecting the validity of the methods as long as name conflicts are avoided.** (A naming convention can save a lot of headacheds here. )



**First argument of a method is called self** this is nothing more than a convention. it has absolutely no special meaning to Python. 



```python
# Function defined outside the class
def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g
```



This practice usually only serves to confuse the reader of a program. 



Methods may call other methods by using method attributes of the self argument. 



```python
class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x): 
        self.add(x)
        self.add(x)

```





Methods may reference global names in the same way as ordinary functions. The global scope associated with a method is the module containing its definition. **(A class is never used as a global scope)**





# Inheritance



A language feature would not be worthy of the name 'class' without supporting inheritance. 



derived class can inherit methods from base class. 



# Multiple Inheritance 



Python supports a form of multiple inheritance as well. 



```python
class DerivedClassName(Base1, Base2, Base3):
    <statement -1 > 
    .
    .
    .
    <statement - N> 
    
```





search for attributes inherited from a parent class as depth-first, left-to-right, not searching twice in the same class where there is an overlap in the hierarchy. If an **attribute is not found in DerivedClassName, it is searched for in Base1, then Base2 and so on.** 





# Private Variables 



**Private instance variables that cannot be accessed except from inside an object don't exist in Python.**



However, there is a convention: a name prefixed with an underscore. It should be treated as non-public part of the API. It should be considered an implementation detail and subject to change without notice. 



 There is a valid use-case for class-private members (namely to avoid name clashes of names with names defined by subclasses) which is limited support for such a mechanism, called **name mangling**



Name mangling is helpful for letting subclasses override methods without breaking intraclass method calls. 



```python

```

