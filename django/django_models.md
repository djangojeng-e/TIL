# Models



A model is the single, definitive source of information about your data. It contains the essential fields and behaviours of the data you're storing. 



Generally, it maps to a single database table. 



- Each model is a Python class that subclasses django.db.models.Model. 
- Each attribute of the model represents a database field. 
- With all this, Django gives you an automatically generated database-access API Making Queries 



E.g. 



```python
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
```



first_name and last_name are fields of the model. Each field is specified as a class attribute, each attribute maps to a database column. 



This equates to 



```mysql
Create Table myapp_person(
	"id" serial NOT NULL PRIMARY KEY,
	"first_name" varchar(30) NOT NULL,
	"last_name" varchar(30) NOT NULL,);
```





# Using Models 



Once the model is defined, it needs to be told to Django that those models are going to be used. **Register the created app in the settings.py** 



Go to **INSTALLED_APPS** and setting to add the name of the module that contains models.py. 



```django
INSTALLED_APPS = [
	#... 
	'myapp'
	#...
]
```





**After the new app has been registered in INSTALLED_APPS,**



<u>**Remember to run $ manage.py migrate !!**</u>



# Fields



The most important part of a model is the list of database fields it defines. Fields are specified by class attributes. **Be careful not to conflict with the models API such as clean, save or delete**



e.g 



```python
from django.db import models

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()
```







# Field Types 



**Each field in your model should be an instance of the appropriate Field Class.** 



Django uses the field class types to determine a few things 



- The column type, tells the database what kind of data to store (e.g. INTEGER, VARCHAR, TEXT)
- The default HTML to use when rendering a form field 
- The minimal validation requirements, used in Django's admin and automatically generated forms. 





# Field Options 



Each field takes a certain set of field-specific arguments. 

For example, **CharField requires max_length argument** 



There is a set of common arguments available to all field types which are optional. 



**null** 

if True, Django will store empty values as NULL in the database. Default is False 



**blank**

If True, the field is allowed to be blank. Default is False. 



**Blank is more validation-related** If a field has blank=True, form validation will allow entry of an empty value. If a field has blank=False, the field will be required. 



**Choices**

A sequence of 2-tuples to use as choices for the field. If this is given, the default form widget will be a select box instead of the standard text field and will limit choices to the choices given. 



```python
YEAR_IN_SCHOOL_CHOICES = [
    ('FR', 'Freshman'),
    ('SO', 'Sophomore'),
    ('JR', 'Junior'),
    ('SR', 'Senior'),
    ('GR', 'Graduate'),
]
```





**N.B. A new migration is created each time the order of choices changes. **



```python
from django.db import models 

class Person(models.Model):
    SHIRT_SIZES = (
    	('S', 'Small'), 
        ('M', 'Medium'), 
        ('L', 'Large'),
    	
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
    
```



You can also use enumeration classes to define choices in a concise way. 



**However, there is an error on the code below. TextChoices is not defined in models. **



```python
from django.db import models

class Runner(models.Model):
    MedalType = models.TextChoices('MedalType', 'GOLD SILVER BRONZE')
    name = models.CharField(max_length=60)
    medal = models.CharField(blank=True, choices=MedalType.choices, max_length=10)
```



**default**

The default value for the field. This can be a value or a callable object. If callable it will be called every time a new object is created. 



**help_text**

Extra "help" text to be displayed with the form widget. It's useful for documentation even if your field isn't used on a form 



**Primary_key**



**If True, this field is the primary key for the model**





If primary key is not specified for any fields in the model, Django will automatically add an IntegerField to hold the primary key. **The primary key field is read-only.** If you change the value of the primary key on existing object and then save it, a new object will be created alongside the old one. E.g. 





```python
from django.db import models 

class Fruit(models.Model): 
    name = models.CharField(max_length=100, primary_key=True)
    
```



```shell
fruit = Fruit.objects.create(name='Apple')
fruit.name = 'Pear'
fruit.save()
Fruit.obejcts.values_list('name', flat=True)
```



**Two commands to be noted here**



**objects.create(name='Apple')**

**objects.values_list('name, flat=True) **



**Unique**



if True, this field must be unique throughout the table. 





# Automatic Primary Key Fields 



By default, Django gives each model the following Field: 



```python
id = models.AutoField(primary_key=True)
```





# Verbose field names 



Each field type, except for ForeignKey, ManyTomanyField and OnetoOneField takes an optional first positional argument - a verbose name. **If the verbose name isn't given, Django will automatically create it using the field's attribute name, converting underscores to spaces.** 



```python
first_name = models.Charfield("person's first name", max_length=30)
```



ForeignKey, ManyToManyField and OneToOneField require the first argument to be a model calss, so use the Verbose_name keyword argument. 



```python
poll = models.ForeignKey(Poll, on_delete=models.CASCADE, verbose_name="the related poll",)
sites = models.ManyToManyField(Site, verbose_name="list of sites")
place = models.OneToOneField(Place, on_delete=models.CASCADE, verbose_name="related place",)
```



**The convention is not to capitalise the first letter of the verbose_name. Django will automatically capitalise the first letter where it needs to**





# Relationships



The power of relational databases lies in relating tables to each other. 

Django offers way to define the three most common types of database relationships 

**many-to-one, many-to-many and one-to-one**



## Many-to-one realtionships 



**django.db.models.Foreignkey** including it as a class attribute of your model. 



**ForeignKey** requires a positional argument : the class to which the model is related. 



E.g. a car manufacturer makes multiple cars. However, one car has only one Manufacturer. 



In a class definition, 





```python
from django.db import models 

class Manufacturer(models.Model): 
    #.. 
    pass 

class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete= models.CASCADE)
    
```



It's suggested that the name of a ForeignKey field be the name of the model, the lowercase.. You can call the field whatever you want. like below. 



```python
class Car(models.Model):
    company_that_makes_it = models.ForeignKey(Manufacturer, on_delete=models.CASCADE,)
    
```







## Many-to-many relationships 



E.g. If a Pizza has multiple Topping objects - that is a Topping can be on multiple pizzas and each pizza has multiple toppings - that could be represented as below. 





Use **models.ManyToManyField(Topping)**





```Python
from django.db import models 

class Topping(models.Model): 
    #.. 
    pass 

class Pizza(models.Model): 
    #.. 
    toppings = models.ManyToManyField(Topping)
    
    # toppings represent plural form to indicate the set of related model objects.
```



**ManyToManyField** fields accepts a number of extra arguments which are explained in the model field reference. 





## Extra fields on many-to-many relationships 





When dealing with many-to-many relationships such as mixing and matching pizzas and toppings, a standard **ManyToManyField ** is all you need. 



Example, the case of an application tracking the musical groups which musicians belong to. A person and the groups of which they are a member can be represented by ManyToManyField. 



To describe this relationship, take the example below. 





```python
from django.db import models 

class Person(models.Model): 
    name = models.CharField(max_length=128)
    
    def __str__(self): 
        return self.name 
    
    
class Group(models.Model): 
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, thorugh="Membership")
    
    def __str__(self): 
        return self.name 
    

class Membership(models.Model): 
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)
    
    
```



**When you set up the intermediary model, you explicitly specify foreign keys to the models that are involved in the many-to-many relationship. This explicit declaration defines how the two models are related**



# 

# One-to-One relationships 





To define a one-to-one relationship, use **OneToOneField**

It requires a positional argument : the class to which the model is related. 







**E.g.** 

If you were building a database of "places", you would build pretty standard stuff such as address, phone number, etc. Then, if you wanted to build a database of restaurants on top of the places, instead of repeating yourself and replicating those fields in the Restaurant model, 



**you could make Restaurant have OneToOneField to Place. ** 



Restaurant is a place. In fact, to handle this you'd typically use inheritance, which involves an implicit one-to-one relation. 





# Models across files 



It's pretty ok to relate a model to one from another app. To do this, import the related model at the top of the file where your model is defined. 



```python
from django.db import models 
from geography.models import Zipcode 

class Restaurant(models.Model):
    #...
    zip_code = models.ForeignKey(
    ZipCode, 
    on_delete=models.SET_NULL, 
    blank=True, 
    null=True,)
```





# Field Name restrictions 



**Django places some restrictions on model field names:**





1. A field name cannot be a Python reserved word. It will lead to a Python Syntax error 



```python
class Example(models.Model): 
    pass = models.IntegerField()

# 'pass' is a reserved word! 

```

2. A field name cannot contain more than one underscore in a row, due to the way Django's query lookup syntax works 





```python
class Example(models.Model): 
    foo__bar = models.IntegerField()
    
   # 'foo__bar' has two underscores. 


```





3. A field name cannot end with an underscore 



However, SQL reserved words such as join, where or select are allowed as model field names as Django escapes all database table names and column names in every underlying SQL query. 





# Meta Options 





```python
from django.db import models 

class Ox(models.Model): 
    horn_length = models.IntegerField()
    
    class Meta:
        ordering = ["horn_length"]
        verbose_name_plural = "oxen"
        
```



Model Metadata is not a field. 





# objects.get(name__contain="contain")

# objects.filter(name_contain="contain")



> objects.get extracts the data the unique. If no unique data is extracted, using get method will raise the error. 
>
> 
>
> On the other hand, objects.filter() will list out the data meeting up the conditions in filter().





# Model Attributes 



**objects**  - The most important attribute of  model is the Manager. It is the interface through database query operations are provided to Django models and is used to retrieve the instances from the Database. 





# Model Methods 





Custom methods on a model can be added custom "row-level" functionality to the objects. **Manager** methods are intended to do "table-wide" things, model methods should act on a particular model instance. 



Demonstrating the custom methods:





```python
from django.db import models 

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()

    def baby_boomer_status(self):
        "Returns the persons's baby-boomer status."
		import datetime 
        if self.birth_date < datetime.date(1945, 8, 1):
            return "Pre-boomer"
        elif self.birth_date < datetime.date(1965, 1, 1): 
            return "Baby boomer"
        else:
            return "Post-boomer"
        
       @property 
    
    	def full_name(self):
            "Returns the person's full name."
            return '%s %s' % (self.first_name, self.last_name)
        
        
```





**Magic Method** 



```
__str__() 

# A python "magic method" returns a string representation of any object. 
# This is used in Python and Django whenever a model instance needs to be coerced and displayed as a plain string. 

# This happens when you display an obejct in an interactive console or in the admin. 

```





# Model Inheritance



Model inheritance in Django works almost identically to the way normal class inheritance works in Python. The only decision you have to make is whether you want the parent models to be models in their own right or if the parents are just holders of common information that will only be visible through the child models. 



**3 styles of inheritance that are possible in Django**



1. Just use the parent class to hold information that you don't want to have to type out for each child model. This class is not going to ever be used in isolation. **-> Abstract base classes**



2. If you are subclassing an existing model (maybe something from another application entirely) and want each model to have its own database table -> **Multi-table inheritance**



3. If you only want to modify the Python-level behavior of a model, without changin the models fields in any way, use **Proxy models**





# Abstract Base Classes 



Abstract base classes are useful when you want to put some common information into a number of other models. **abstract=True** in the Meta class. This model will not be used to create any database table. When it is used as a base class for other models, its fields will be added to those of the child class. 





```python
from django.db import models 

class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    
    class Meta:
        abstract = True 
        
class Student(CommonInfo):
    home_group = models.CharField(max_length=5)
    

```



**CommonInfo** model cannot be used as normal Django model, since it is an abstract base class. It does not generate a database table or have a manager, and cannot be instantiated or saved directly. 



This provides a way to factor out common information at the Python level, while still only creating one database table per child model at the database level. 



## Meta Inheritance 



When an abstract base class is created, there is Meta inner class you declared in the base class available as an attribute. **If a child class does not declare its own Meta Class**, it will inherit the parent's Meta. 





```python
from django.db import models 

class COmmonInfo(models.Model):
    # ... 
    class Meta:
        abstract = True 
        ordering = ['name']
        
class Student(CommonInfo):
    # ... 
    class Meta(CommonInfo.Meta): 
        db_table = 'student_info'
        
```

