# Enumerate 



enumerate(iterable, start=0)



**enumerate** return an enumerate object. iterable must be a sequence, an iterator or some other object which supports iteration. 



```python

L = ['apples', 'bananas', 'oranges']
for idx, val in enumerate(L): 
    print("index is %d and value is %s" % (idx, val))
    
```



**Enumerate a Tuple**



```python

tup = ('apples', 'bananas', 'oranges')
for idx, val in enumerate(t):
print("index is %d and value is %s" % (idx, val))

```

**Enumerate a string**



```python

str = "Python"
for idx, ch in enumerate(str): 
    print("index is %d and character is %s" % (idx, ch))
    
```



# Enumerate with a Different starting index





Indices in python starts at 0. By default **enumerate** returns the index starting from 0. 

In the case when you want the loop counter to start at a different number, 



**enumerate** allows you to do that through an optional start parameter. 



```python

L = ['apples', 'bananas', 'oranges']
for idx, s in enumerate(L, start=1): 
    print("index is %d and value is %s" % (idx, s))
    
```

**enumerate** takes care of indexes. Dictionaries and Sets are note sequences. 



**enumerate returns a Python object of type enumerate**

