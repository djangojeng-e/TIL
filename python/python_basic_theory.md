# Python is an interpreted language 



Python is an interpreted language that is not in machine level code before runtime. Unlike C, it does not need to be compiled. 





# PEP8 (Python Enhancement Proposal)



PEP stands for **Python Enhancement Proposal**. It is a set of rules that specify how to format Python code for maximum readability. 

According to PEP8, the code you write is read by others more. Developers often spend much time to read the codes written by others. PEP8 does help to write codes in more consistent forms. Anyone who follows this proposal might produce more readable codes and make it easier for others to read the code. 



# How is memory managed in Python? 





1. Memory management in python is managed by **Python Private Heap Space**. **All python objects and data structures** are located in a private heap. The programmer does not have access to this private heap. They python interpreter takes care of this instead. 
2. The allocation of heap space for Python objects is done by **Python's memory manager.** The core API gives access to tools for the programmer to code. 
3. **Python also has an inbuilt garbage collector,** which recycles all the unused memory and so that it can be made available to the heap space. 



**Heap space** is the area of memory that stores mutable objects. objects in heap space remain until you explicitly erase them or until you quit Python. **You cannot access to heap space directly**. You **access them with variables** in global space or in a call frame that contain the name of the object in heap space.



# Python modules 





**Python modules are files containing Python code**. This code can either be function classes or variables. 



## Commonly used built-in modules 



- OS
- Sys
- Math
- Random
- Datetime



# Functions in Python



A function is a block of code which is executed only when it is called. 



```python
def Function():		# Function name defined.
    print("Function is a function") 
    # code block to be exectued when function is called. 
    
```



# Dictionary in Python 



The built-in datatypes in Python is called dictionary. It defines one-to-one relationship between keys and values. Dictionary contain pair of keys and their corresponding values. 



Dictionaries are indexed by keys. 



# *args and **kwargs 



We use ***args** when we are not sure how many arguments are going to be passed to a function, or if we want to pass a stored list or tuple of arguments to a function. 

On the other hand, ****'kwargs'** is used when we do not know how many keyword arguments will be passed to a function. or it can be used to pass the values of dictionary as keyword arguments. 



The name does not have to be args or kwargs as long as they are defined with  asterisks. Examples below. 



```python
def adder(*num): 
    # adder function is defined with *num arguments. 
    # Want to pass a stored list or tuple of arguments.
    
    sum = 0 
    
    for n in num:
        sum = sum + n 
    
    print("Sum:", sum)
    
adder(3,5)
adder(4,5,6,7)
adder(1,2,3,5,6)
```

**Another Example using **kwargs**



```python
def intro(**data):
    # function intro is defined with **data arguments 
    # arguments will be in form of dictionary. 
    print("\nData type of argument:",type(data))
    
    for key, value in data.items():
        print("{} is {}".format(key,value))
        
intro(Firstname="Sita", Lastname="Buta", Age=22, phone=123456589)

intro(Firstname="John", Lastname="Wood", Email="johnwood@hotmail.com", Country="Farland", Age=30, phone=98754564)
```



#### Remember 

- *args and **kwargs are special keyword allowing functions to take variable length argument.
- *args passes variable number of non-keyword arguments lists 
- **kwargs passes variable number of keyword arguments dictionary to function on which operation of a dictionary can be performed. 
- *args and **kwargs make the function flexible. 



# When Python exists, all the memory is not de-allocated.





1. When Python exists, especially those Python modules which are having circular references to other objects or the objects that are referenced from the global namespaces are not always de-allocated or freeed. 
2. It is impossible to de-allocate those portions of memeory that are reserved by the C library. 
3. On exit, because of having its own efficient clean up mechanism, Python would try to de-allocate/destroy every other objects. 



# Dictionary in Python 



Dictionary is a built-in datatype in python. It defines one-to-one relationship between keys and values. It contains pair of keys and their corresponding values. Dictionaries are indexed by keys 



# Inheritance in Python



Inheritance allows one class to gain all the member(attributes and methods) of another class. **Inheritance provides code reusability , makes it easier to create and maintain an application**



The class that another class inherits from is called super-class and the class that is inheriting from other classes is called a derived / child class. 



**Inheritance have different types**



1. **Single Inheritance** - a delivered class acquires the members of a single Super class 
2. **Multi-level Inheritance** - a derived class d1 in inherited from base class base1, and d2 are inherited from base2. 
3. **Hierarchial Inheritance ** - From one base class you can inherit any number of child classes 
4. **Multiple Inheritance** - a derived class is inherited from more than one base class. 



# Encapsulation in Python 





**Encapsulation** means binding the code and the data together. A representative example of encapsulation in python is class that binds variables and methods(functions) that contain code blocks. 







