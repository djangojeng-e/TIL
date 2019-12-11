# Modules 



As your program gets longer, splitting the program into several files for easier maintenance might come into issue.  Python has a way to put definitions in a file and use them in a script or in an interactive instance of the interpreter. These files are called a **module.**



Modules can be imported into other modules or in to the main module. (The collection of variables that you have access to in a script executed at the top level and in calculator mode.)



**A module is a file containing Python definitions and Statements** 





```python
import fibo

a = fibo.fib(1000)
print(a)

b = fibo.fib2(100)
print(b)

# if you want to use a function 
# Assign imported module to a local name. 

local_name = fibo.fib
a = local_name(500)
print(a)
```





# More on Modules 



Each module can contain executable statements as well as function definitions. 



Statements are intended to initialise the module. Each module has its own private symbol table, used as the global symbol table by all functions defined in the module. 



The author of a module can use global variables in the module without worrying about accidental clashes with user's global variables. 



The user can touch a modules' global variables with the same notation used to refer to its functions **modname.itemname**



Import statements have variants 



**1) Import names from a module directly into the importing module's symbol table**



```python
from fibo import fib, fib2  # Specified the names of functions 
a = fib(500)
print(a)
```





**2) There is a variant to import all names that module defines**



```python
from fibo import *	# Import all names defined in module.
a = fib(500)
print(a)
```



This imports all names defined in the module except any definition with an underscore(_). 



**3) You can assign alias for the definition imported**



```python
import fibo as fib 
a = fib.fib(500)
print(a)
```



After assigned alias, you can use fib() in your module. 



**Note: For efficiency, each module is only imported once per interpreter session** **Hence, you must restart the interpreter if you change your modules.**



# Executing modules as scripts 





```python
# with the __name__ set to __main__. 
# This means that by adding this code at the end off your module. 


if __name__ == "__main__": 
    import sys
    fib(int(sys.argv[1]))
    
  
```



This is often used either to provide a convenient user interface to a module, or for the 

testing purposes (running the module as a script executes a test suite.





# The Module Search Path 



When a module is imported, the interpreter first searches for a built-in module with that name. If not found, it searches for a file named in a list of directories given by the variable. 





# Standard Modules 



Python comes with a library of standard modules, described in a separate document. Some modules are built into the interpreter. 



**e.g. the sys module is built into every Python interpreter.**



# dir() lists the names you have defined.





# Packages 



Packages are a way of structuring Python's module namespace by using 'dotted module names'. 

