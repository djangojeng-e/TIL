

# Python @Property Getter/Setter 





Python @Property, getter, setter methods in class have been the most difficult concept to understand in class. 



Before start learning about @property,  certain concepts have to be understood beforehand. 



# Python attribute



Python attributes are instance variables. Attributes are the names used after objects as a reference to a function or a variable. 





```python

class Stick: 
    def __init__(self, length): 
        self.length = length 
        
stick1 = Stick(10)
stick1.length 

# This returns the value of 10. 
# This length is the attribute. 


```





Please remember. Attributes are simply instance variables.





Before looking into @property, **We should understand that there are no private variables in Python technically.**  



Explicitly though, **using a leading underscore with variables can make the variables private.** However, this does not prevent a programmer from accessing it beyond the class and manipulating. 



```python


class Stick: 
    def __init__(self, length): 
        self._length = length  
        # Put a leading underscore to make the variable 	           private
        
stick1 = Stick(10)
stick1.length 

# This returns the value of 10. 
# This length is the attribute. 


```



With this example, let us assume if the user puts a negative value into length variable. This does not make sense as length of object is not measured in negative values. 



# Let's use getters and setters in Python





```python

class Stick: 
    def __init__(self, length): 
        self._length = length  
        # Put a leading underscore to make the variable 	           private
    
    # Implementing new getter method 
    def get_length(self):
        return self.length 
    
    # Implementing new setter method 
    def set_length(self, length_value): 
        if length_value < 0:
            raise ValueError("Length cannot be negative")
        self.length = length_value
        
stick1 = Stick(10)
stick1.length 

# This returns the value of 10. 
# This length is the attribute. 



```

