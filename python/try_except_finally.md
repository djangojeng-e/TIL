# Try, Except and Finally in Python 





**Try**  : Lets you test a block of code for error 



**Except** : Lets you handle the error 



**Finally** : lets you execute code, **regardless of the result of the try- and except** blocks. 





```python

try: 			# print(A) will be excecuted for try. 
    print(A)	
    # There will be an error as A has not been defined 
except:			# except will step out to handle the error. 
    print("There had been an error.") 
    # Instead of executing print(A) above, 
    # print("There had been an error") will be executed. 


```

Without the try block, the program will crash and raise an error: or it stops. 



# Multiple Exceptions 





Excepts can be multiple as many as you want. 



**There are error types in Python. For example,** 



Syntax Error, IndexError, ModuleNotFoundError, KeyError, ImportError, StopIteration, TypeError, ValueError, NameError, ZeroDivisionError, KeyboardInterrupt,  etc 



```python
try:
    print(x)
except NameError: 
 # if NameError occurs, the following code will be executed. 
    print("Variable x is not defined.")
except: 
 # if there is an error other than NameError, 
 # the following code will be executed. 
    print("Something else went wrong.")



```





# Else 



You could use else keyword to define a block of code to be executed if no errors were raised. 



Example 



```python
try: 
    print("Hello")
    # This code block will be executed as there's no error. 
except:
    print("Something went wrong")
else: 
    print("Nothing went wrong")
	# Since there had been no error occurred, 
    # This code block will also be executed by else: 


```



The code above will execute both statements 



**1) print("Hello") **

**2) print("Nothing went wrong").** 



# Finally 



**Finally** block, if specified will be executed regardless if the try block raises an error or not. 





```python
try:
    print(x)
except:
    print("Something went wrong")
finally: 
    print("The 'try except' is finished.")



```



According to python tutorial documentation, the **finally** **clause will execute as the last task before the try statement completes.** The finally clause runs whether or not the try statement produces an exception. 



Taking another look at the another example from python tutorial documentation, the code block under finally clause gets executed anyway. 



```python
def divide(x, y): 
    try:
        result = x / y 
    except ZeroDivisonError: 
        print("division by Zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

```

