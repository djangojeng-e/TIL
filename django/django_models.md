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



