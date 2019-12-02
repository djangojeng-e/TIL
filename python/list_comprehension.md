# List Comprehension 



In python, there is a famous and powerful tool that you can use as a single line to do the task that would have been done in multi lines. This way, you can save your code, shorten them and make your code more stylish in more pythonic way. 



This all can be achieved by using List Comprehension. 



## First, we will need to understand how to create lists in Python 



There are 3 ways to create lists in Python 



1. Using for Loops 
2. Using a map() objects 
3. **Using List Comprehensions** 

 

#### Using for Loops to create lists



This is the most common way to create lists. For example, a list that contains the first ten perfect squares, you can complete these steps in three lines of code below. 



```python

squares = []
for i in range(10): 
    squares.append(i * i)

print(squares)



```



#### Using map() Objects 



Taking from examples above, 



```python

def get_square(list_1):
    return list_1 ** 2

powered_numbers = map(get_square, list_1)
powered_numbers = list(powered_numbers)
print(powered_numbers)

```

map() takes an iterable objects and a function. map() executes function taken to objects contained in iterable objects. 



#### Using List Comprehension 



```python
squares = [i * i for i in range(10)]
print(squares)
```



It operates pretty much the same with map() above. However, there is a certain distinction between implementation and map(). 



**List comprehension in Python returns a list, Map() does not return a list.** 



```python

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def get_square(list_1): 
    return list_1 ** 2 

squared_numbers = [get_square(i) for i in list_1]

print(squared_numbers)


```



## Benefits of Using List comprehensions 



List comprehensions are one of the most Pythonic form. Before use it regularly, the benefits of using list comprehensions should be covered. 



- It is a single tool that you can use in many different situations. List comprehension is used particularly when creating a list. 
- It aligns with Pythonic. List comprehension represents **simple, powerful tool** that you can use in wide variety of situations.
- There is less need to remember the proper order of arguments like in map() 
- **It is more declarative than loops.**  They're easier to read and understand. 





## Using Conditional Logic 





List comprehension allows to add conditional statement just before closing bracket. 



Conditionals are important when filtering out unwanted values, which would normally require a call to filter(): 



```python


sentence = 'the rocket came back from mars'
vowels = [i for i in sentence if i in 'aeiou']

print(vowels)



```

It allows to add additional logic to select from multiple possible output options. 



```python


original_prices = [1, -9, 10, 3, 5]
prices = [i if i > 0 else 0 for i in original_prices]
print(prices)


```



#### Using Set and Dictionary Comprehensions 



You can also create set and dictionary comprehensions. A set comprehension is almost exactly the same as a list comprehension in python. 



**Set comprehensions make sure that output contains no duplicates. You can create a set comprehension by using curly braces instead of brackets:** 



```python

quote = "life, uh finds a way"
unique_vowels = {i for i in quote if i in 'aeiou'}
print(unique_vowels)

```



#### Dictionary comprehensions are similar, with additional requirement of defining a key: 



```python

squares = {i: i * i for i in range(10)}
print(squares)


```



# When not to use a List Comprehension in Python 





List comprehensions are useful and can write elegant code. However, they're not the right choice for all circumstances. It could lead to less performance or it could also make the code harder to understand. 



Particularly, Nested Comprehensions are harder to understand. List comprehension would not be a good option to choose first on the nested functions or conditions. 



# Choose Generators for Larger Datasets 



- A list comprehension in python works by loading the entire output list into memory. 



When it comes to a larger Datasets, Python will try to create a list into memory. The computer may not have the resources it needs to generate a large data and store it into memory. 



#### A generator does not create a single, large data structure in memory, but instead returns an iterable. 





# Conclusion 



List comprehension in python is used to accomplish complex tasks without making your code overly complicated. 













