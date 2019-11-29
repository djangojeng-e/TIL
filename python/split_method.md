

# Split() method 





The split() method splits a string into a list. 



 It has a separator and maxsplit values. Default value for separator is whitespace. 

Default Value for maxsplit is -1. 



Let's take some examples. 



```python

txt = "Django is a great web framework."
x = txt.split()

print(x)

# This returns a list x containing 
# ['Django', 'is', 'a', 'great', 'web', 'framework.']

# txt has been recreated as a list. 
# The white spaces in string txt have been the separator. 

```



​		Example2 

```python

txt = "Hello, Django, You are good"
x = txt.split(",")

print(x)

# String txt has been separated by ','
# ['Hello', ' Django', ' You are good']




```



string() method is useful when solving algorithm problems especially when you breakdown string values into the lists. 





​    