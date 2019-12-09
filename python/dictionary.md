# Dictionary 



A dictionary is a collection which is unordered, changeable and indexed. In Python, dictionaries are written with curly brackets and they have keys and values. 





```python
dictionary = {
    "name" : "Django", 
    "model" : "Web Framework"
    "year" : 2019
}

print(dictionary)
```



# Accessing items 



You can access the items of a dictionary by referring to its key name, inside square brackets. 



```python
# Accessing items 
x = dictionary["name"]
print(x)


# Using get() method
x = dictionary.get("name")
print(x)
```



There is also a method get() that will give the same result. 





# Change Values 



The value can be changed by referring to its key name 



```python
dictionary = {
    "name" : "Django", 
    "model" : "Web Framework"
    "year" : 2019
}

dictionary["year"] = 2020 

print(dictionary)
```





# Loop Through a Dictionary 



A dictionary can be looped by using a for loop. 



**Basically, the loop returns the keys of the dictionary** but there are methods to return the values as well. 



```python
for x in dictionary: 
	print(x)
```



**For the values of dictionary**



```python
for x in dictionary:
    print(dictionary[x])
    
# You can also use the value() functions to return values of a dictionary. 

for x in dictionary.values(): 
    print(x)
    
    
```



# Looping through both keys and values using items() functions 





Loop through both keys and values, by using the items() functions 





```python
for x, y in dictionary.items(): 
	print(x, y)
```





# Check if key Exists 





```python
dictionary ={
    "name" : "Django", 
    "model" : "Web Framework",
    "Year" : 2019
}

if "model" in dictionary:
    print("Yes, there is 'model' as a key in dictionary.")
    
```





# Dictionary Length 



```python
print(len(dictionary))
```





# Adding Items 



Adding an item to the dictionary is easy. Put the new key name in bracket and assign the new value on the right hand side. 



```python
dictionary = {
"name" : "django", 
"model" : "web framework",
"year" : 2019
}

# Add language as a new key and the value of this new key will be Python 

dictionary["language"] = "Python"

print(dictionary)
```







# Removing Items



There are some methods to remove items from a dictionary 



```python


# Pop() method removes the item with the specified key name 

dictionary = {
    "name": "Django",
    "model": "Web Framework",
    "Year" : 2019,
}

dictionary.pop("year") 
print(dictionary)

```





**del keyword removes the item with the specified key name**





```python

# Use del keyword to remove the item with key name

dictionary = {
    "name": "Django",
    "model": "Web Framework",
    "year": 2019
}

del dictionary["name"]
print(dictionary)


```





# Deleting dictionary 





**del keyword** and **clear()** keyword empties the dictionary. 



```python

dictionary = {
    "name" : "Django",
    "model" : "Web Framework", 
    "year" : 2019 
}

dictionary.clear()
print(dictionary)

# Delete dictionary using del keywords

dictionary = {
    "name" : "Django",
    "model" : "Web Framework", 
    "year" : 2019 
}

del dictionary

print(dictionary)



```



clear() keyword empties the dictionary but del keyword completely delete dictionary. 





# Make a copy of dictionary 





There are ways to copy dictionary. 



```python
# Copy dictionary using copy()

dictionary = {
    "name": "Django",
    "model": "Web Framework",
    "Year": 2019
}

dictionary_two = dictionary.copy()
print(dictionary_two)


# Copy dictionary using dict()

copied_dictionary = dict(dictionary)
print(copied_dictionary)


```







# Key Dictionary Methods





| Method   | Description                                               |
| -------- | --------------------------------------------------------- |
| clear()  | Removes all the elements from the dictionary              |
| copy()   | Returns a copy of the dictionary                          |
| get()    | Returns the value of the specified key                    |
| items()  | Returns a list containing a tuple for each key value pair |
| keys()   | Returns a list containing the dictionary's keys           |
| pop()    | Removes the element with the specified key                |
| values() | Returns a list of all the values in the dictionary        |

