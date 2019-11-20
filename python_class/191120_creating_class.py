# Class named as Human will be created 




class Human():      # 1. Class has been created.  
    '''Human'''     # 2. ''' ''' is description on the class. refer to Docstring


person1 = Human()   

# 3. Human Class has been called. One instance created to person1 

person2 = Human()   

# 4. Human Class has been called. One instance created to person2. 


# Class has its own functionality to save and control data. 
# e.g. list is a type of class that can store data in order. 
# e.g. list can control its data by using commands like append(), extend(), inse# rt(), pop() 


person1.language = 'English' # Person1 speaks English 
person2.language = 'German'  # Person2 speaks German 

print(person1.language) 
print(person2.language) 


print()
print()
print() 

person.name = 'George' 
person.name = 'Ozil' 


def speak(person):
    print("{} speaks {}".format(person.name, person.language)) 

speak(person1)
speak(person2)







