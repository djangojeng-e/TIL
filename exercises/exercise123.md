What statements can you put under a try-except block? 

We have two of those: 

else - To run a piece of code when the try-block doesn't create an exception 

finally - To exceute some piece of code regardless of whether there is an exception 

```python 
try:
    print("Hello") 
except:
    print("Sorry") 
else:
    print("Oh then") 
finally:
    print("Bye") 

```

The code runs the output 

Hello

Oh then 

Bye
