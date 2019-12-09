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



dictionary = {
"name" : "django", 
"model" : "web framework",
"year" : 2019
}

# Add language as a new key and the value of this new key will be Python 

dictionary["language"] = "Python"

print(dictionary)



# Pop() method removes the item with the specified key name 

dictionary = {
    "name": "Django",
    "model": "Web Framework",
    "Year" : 2019,
}

dictionary.pop("Year") 
print(dictionary)



# Use del keyword to remove the item with key name

dictionary = {
    "name": "Django",
    "model": "Web Framework",
    "year": 2019
}

del dictionary["name"]
print(dictionary)



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

# print(dictionary)
# del keyword removes dictionary completely. 

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