class Human(): 
    pass

def create_human(name, weight):     # Gets Name and Weight and stores.  
    person = Human()
    person.name = name 
    person.weight = weight 
    return person 

Human.create = create_human             # Human class's create Function 'create_human' 
person = Human.create("John", 60.5) # John and 60.5 values assigned to person instance. 


# Eating 

def eat(person): 
    person.weight += 0.1    # If you eat, you gain 0.1kg 
    print("{} ate, so gained {} kg.".format(person.name, person.weight))

# Walking 

def walk(person):
    person.weight -= 0.1    # If you walk, you lose 0.1kg 
    print("{} walked, so lost {} kg.".format(person.name, person.weight))


# Injecting it to Human Class 

Human.eat = eat 
Human.walk = walk 


# Applying to actual person 


person.walk()
person.eat()
person.walk()

# Expressing the things in the real life in codes is called modelling. 


