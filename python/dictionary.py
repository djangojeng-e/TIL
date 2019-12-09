dictionary = {
    "name" : "Django", 
    "model" : "Web Framework",
    "year" : 2019
}

print(dictionary)


# Accessing items 
x = dictionary["name"]
print(x)


# Using get() method
x = dictionary.get("name")
print(x)


# Change Values 

dictionary = {
    "name" : "Django", 
    "model" : "Web Framework",
    "year" : 2019
}

dictionary["year"] = 2020 

print(dictionary)


# Printing the keys 

for x in dictionary: 
	print(x)


# Printing values

for x in dictionary:
    print(dictionary[x])
    
# You can also use the value() functions to return values of a dictionary. 

for x in dictionary.values(): 
    print(x)
    

# Loop through both keys and values, by using the items() function 


for x, y in dictionary.items(): 
	print(x, y)


# Checking the keys 

dictionary ={
    "name" : "Django", 
    "model" : "Web Framework",
    "Year" : 2019
}

if "model" in dictionary:
    print("Yes, there is 'model' as a key in dictionary.")
    

# Checking the length of dictionary.
print(len(dictionary))

