# Making Queries 



Once data models have been created, Django automatically gives a database Abstraction API that can create, retrieve, updated and delete objects. 



The topic is based on the following example. 





```python
from django.db import models



class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField()
    number_of_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.headline

```





# Creating objects 



To represent database-table in Python obejcts, Django uses an intuitive system. 



**Model class represents a database table**

**Instance of that class** represents a particular record in the database table. 



To create an object, instantiate it using keyword arguments to the model class and call **save()** to save it to the database. 



```python
from blog.models import Blog 
b = Blog(name='Beatles Blog', tagline='All the latest Beatles news.')
b.save()

```





> **The save() method has no return value**
>
> 
>
> object method can shorten this in a single step





# Saving Changes to objects 



To save changes to an object that's already in the database, use save() 





```python
b5.name = 'New name'
b5.save()
```



> Django doesn't hit the database until save() is called explicitly! 





# Saving ForeignKey and ManyToManyFields 





Tutorial does not offer the appropriate example instances of Entry and Blog.. 



Assuming there has been appropriate instances of Entry and Blog saved to the database already, we can retrieve them below. 



```python
from blog.models import Blog, Entry 
entry = Entry.objects.get(pk=1)
cheese_blog = Blog.objects.get(name="Cheddar Talk")
entrly.blog = cheese_blog 
entry.save()

# Updating a ManyToManyField works a little different 
# Use add() method on the field to add record to the relation. 

from blog.models import Author 
joe = Author.objects.create(name="Joe")
entry.authors.add(joe)


# In order to add multiple records to ManyToManyField in one go, 

john = Author.objects.create(name="John")
paul = Author.objects.create(name="Paul")
george = Author.objects.create(name="George")
ringo = Author.objects.create(name="Ringo")

entry.authors.add(john, paul, george, ringo)
```





# Retrieving objects 



To retrieve objects from the database, a **QuerySet through Manage** will get you those. 

**QuerySet represents a collection of objects from your database.**



**it could have some filters that might equate to WHERE or LIMIT in SQL.**







> Managers are accessible only via model classes, rather than from model instances, to enforce a separation between "table-level" operations and "record-level" operations. 





**Manager** is the interface through which database query operations are provided to Django models. At least one Manager exists for every model in a Django application. 





# Retrieving all objects





```python
# The simplest way to retrieve objects from a table is to get all of them . 
# To do this, Use the all() method on a Manager. 

all_entries = Entry.objects.all()


```



**The all() method returns a QuerySet of all objects in the database.**





# Retrieving specific objects with filters





You can refine the initial QuerySet, adding filter conditions.



**filter(kwargs)**

Returns a new QuerySet containing objects that match the given lookup parameters. 



**exclude(kwargs)**

Returns a new QuerySet containing objects that do not match the given lookup paramters. 





```python
# To get a QuerySet of blog entries from the year 2006, use filter()

Entry.objects.filter(pub_date__year=2006)

# This performs the same task with 
Entry.objects.all().filter(pub_date__year=2006)
```





# Chaining Filters 





The result of refining a QuerySet is itself a QuerySet, so it's possible to chain refinements together. 







```python

entry.objects.filter(
headline__startswith="what").exclude(
pub_date__gte=datetime.date.today().filter(
pub_date__gte=datetime.date(2005, 1, 30)))


# This takes all entries in the database, add a filter and exclude
# This results in a QuerySet 
# Containing all entries with a headline that starts with "What"
# That were published between January 30, 2005 and the current day. 

```



## Filtered QuerySets are unique 



```python

q1 = Entry.objects.filter(headline__startswith="What")
q2 = q1.exclude(pub_date__gte=datetime.date.today())
q3 = q1.filter(pub_date__gte=datetime.date.today())

```



Each QuerySets are not affected by the refinement process. 



## QuerySets are lazy 



Django won't actually run the query until the QuerySet is evaluated. 



```python
q = Entry.objects.filter(headline__startswith="What")
q = q.filter(pub_date__lte=datetime.date.today())
q = q.exclude(body_text__icontains="food")
print(q)

```



> In general, the results of a QuerySet are not fetched from the database until you ''ask'' for them. 





# Retrieving a single object with get()



**filter() ** will always give you a QuerySet, even if only a single object matches the query. 



> If you know that there is only one object that matches your query, you can use the get() method on a manager which returns the object directly!





```python
one_entry = Entry.objects.get(pk=1)
```





- If there are no results that match the query, get() will raise a **DoesNotExist** exception 
- If more than one item matches, the get() will raise **MultipleObjectsReturned**







# Limiting QuerySets 



QuerySet can be limited to a certain number of results. This is equivalent to SQL's LIMIT and OFFSET clauses. 



```
# This returns the first 5 objects (LIMIT 5)

Entry.objects.all()[:5]

# This returns the sixth through tenth objects (OFFSET 5 LIMIT 5) 

Entry.objects.all()[5:10]



```





**Negative indexing e.g. Entry.objects.all()[-1] is not supported.**



Slicing a QuerySet returns a new QuerySet - it does not evaludate the query. 





```python
# 'Step' parameter of Python slice syntax can be used. 
Entry.objects.all()[:10:2]


# To retrieve a single object rather than a list 

Entry.objects.order_by('headline')[0]


```





# Field Lookkups 



Field lookups are like SQL WHERE clause. It is specified in keyword arguments to the queryset methods like filter(), exclude() and get().



Basic lookup keyword arguments take the form 



**field__lookuptype=value**





**exact vs ieact** **contains vs icontains**



```python
Entry.objects.filter(pub_date__lte='2016-01-01')

# In case of ForeignKey,
# Specify the field name suffixed with _id 

Entry.objects.filter(blog_id=4)

Entry.objects.get(headline__exact='Cat bites dog')

Blog.objects.get(id__exact=14)	# Explicit Form 
Blog.objects.get(id=14)			# __exact is implied 


# iexact 
# A case-insentive match 

Blog.objects.get(name__iexact="beatles blog")

# contains 
# Case-sensitive containment test 

Entry.objects.get(headline__contains='Lennon')


# icontains 
# Case Insensitive containment test 

Entry.objects.get(headline__icontains='Lennon')

# startswith, istartwith
Entry.objects.get(headline__startswith="K")
Entry.objects.get(headline__istartswith="k")

# endswith, iendswith 
Entry.objects.get(headline__endswith="K")
Entry.objects.get(headline__iendswith="k")





```





# Looksups that span relationships 



Django offers a powerful and intuitive way to follow relationships in lookups,. To span a relationship, use the field name of related fields across models. 



```python
# Retrieves all Entry objects with Blog whose name is 'Beatles Blog'
Entry.objects.filter(blog__name='Beatles Blog')

# Retrieves all Blog obejcts which have at least one Entry whose headline contains 'Lennon' 

Blog.objects.filter(entry__headline__contains='Lennon')

# If you are filtering across multiple relationships and one of the intermediate models 
# doesn't have a value that meets the filter condition, 
# Django will treat it as if there is an empty but valid object there. 

Blog.objects.filter(entry__authors__name='Lennon')


# If there was no author associated with an entry, it would be treated as 
# if there was also no name attached, rather than raising an enrror 
# because of the missing author. 

Blog.objeccts.filter(entery__authors__name__isnull=True)

# This will return Blog objects that have an empty name on the author and those 
# which have an empty author on the entry. 

Blog.objects.filter(entry__authors__isnull=False, entry__authors__name__isnull=True)




```



## Spanning Multi-Valued Relationships 





```python
# To select all blogs that contain entries with both "Lennon" in the headline 
# That were published in 2008 (the same entry satisfying both conditions)

Blog.objects.filter(entry__headline__contains='Lennon',
                   entry__pub_date__year=2008)


# To select all blogs that contain an entry with "Lennon" in the headline as well as 
# an entry that was published in 2008,

Blog.objects.filter(entry__headline__contains='Lennon').filter(entry__pub_date__year=2008)
```



# The pk lookup shortcut 



For Convenience, Django provides a pk lookup shortcut, which stands for ''primary key'' 



```python


# In the example of Blog models, 
# the primary key is the id field 
# Three statements below are equivalent 


Blog.objects.get(id__exact=14)		# Explicit form 
Blog.objects.get(id=14)				# __exact is implied 
Blog.objects.get(pk=14)				# pk implies id__exact 


```



**The use of pk isn't limited to __exact queries** - any query term can be combined with pk to perform a query on the primary key of a model 



```python
# Get blogs entries with id 1, 4 and 7 
Blog.objects.filter(pk__in=[1,4,7])

# Get all blog entries with id > 14 
Blog.objects.filter(pk__gt=14)


```





**pk lookups also work across joins.**



```python
Entry.objects.filter(blog__id__exact=3)		# Explicit form 
Entry.objects.filter(blog__id=3)			# __exact is implied 
Entry.objects.filter(blog__pk=3)			# __pk implies __id__exact 
```







# Comparing objects 



To compare two model instances, use the standard Python comparison operator, the double equal sign == 





```python
some_entry == other_entry 
some_entry.id == other_entry.id 
```





# Deleting objects 



delete() method immediately deletes the object and returns the number of objects deleted and a dictionary with the number of deletions per object type 





```
e.delete() 

# This will return 

# (1, {'weblog.Entry': 1})
```





**Every QuerySet has a delete() method, which deletes all members of that QuerySet**



```python

Entry.objects.filter(pub_date__year=2005).delete()

```



**When django deletes an object, it emulates the behaviour of the SQL constraint ON DELETE CASCADE** - Any objects which had foreign keys pointing at the object to be deleted will be deleted along with it. 



```python
b = Blog.objects.get(pk=1)
# This will delete the Blog and all of its Entry objects. 

b.delete()
```





**NB :** delete() is the only QuerySet method that is not exposed on a manager itself preventing from accident requests like Entry.objects.delete(), and deleting all the entries.  





# Copying model instances 



There is no built-in method for copying model instances, it is possible to easily create new instance with all fields' values copied. 



```python

blog = Blog(name='My blog', tagline='Blogging is easy')
blog.save() # blog.pk == 1 

blog.pk = None 
blog.save()	# blog.pk == 2 


```





# Updating multiple objects at once 





Sometimes you want to set a field to a particular value for all the objects in a QuerySet. update() method can achieve this. 



```python

# Update all the headlines with pub_date in 2007. 

Entry.objects.filter(pub_date__year=2007).update(headline='Everything is the same')

```





# Related objects 

