myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(x)

# The join() method takes all items in an iterable and joins them into one string. 
# A string must be specified as the separator. 


# Syntax 
# string.join(iterable)

# Example 2 

myDict = {"name" : "John", "Country": "Norway"}
mySeparator = "TEST"

x = mySeparator.join(myDict)

print(x)

# Note : When using a dictionary as an iterable, the 
# returned values are the keys, not the values. 



