# Python Closures



**The method of binding data to a function without actually passing them as parameters is called closure.** It is a function object that remembers values in enclosing scopes even if they are not present in memory. 



Take an example, 



```python
def func1():  # Outer function
  txt = 'func1 value'

  def func2():  # Nested function
      print(txt)
  return func2


obj = func1()
print(obj)


```



 Technically, the func1 variable txt should have gone away with outer function. 

The variable txt is the variable that the inner function depends on and is bound to the func2 even if the outer function goes away. 



Data is bound to a function without actually passing them as parameters is called closure. It is a function object that remembers values in enclosing scopes even if they are not present in memory. 



**What will happen if the func1 is deleted?** 



```python

def func1():  # Outer function
	txt = 'func1 value'

	def func2():  # Nested function
        print(txt)
    return func2


obj = func1() 	
del func1 

# Calling func1() here, will return error as func1 has been deleted. 

obj() 
# Calling obj() will still return the value 'func1 value'


```



**The outer function is deleted. However, object still stores the variable. This is called closure in python.** 



### Criteria for a closure



1. Must be a nested function (function inside another function)
2. This nested function must refer to a variable defined in the enclosing function. 
3. The enclosing function must return the nested function. 



### Why we use closures? 



1. It provides sort of data hiding as they are used as callback functions. 
2. This reduces the use of global variables. 
3. Replacing hard-coded constants 
4. Efficiency when we have a few functions in our code. 



