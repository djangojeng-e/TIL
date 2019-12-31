# Django Admin Site 



Django has its automatic admin interface. It reads metadata from the models to provide a quick, model-centric interface. 



The admin's recommended use is limited to an organisations' internal management tool. The admin has hooks for customisation. 





# Overview 



The admin is enabled in default setting by project template used by startproject. 



After using startproject command to create a project. This admin site will be accessible by visiting URL/admin. 



**createsuperuser** command will create a user to login with. 



Serving files are used as static files for admin (images, Javascript, and CSS)



# ModelAdmin objects



The ModelAdmin class is the representation of a model in the admin interface. Usually these are store in a file named admin.py in your application. 





```python
from django.contrib import admin
from myproject.myapp.models import Author 

class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Author,AuthorAdmin)
```



## The register decorator 





There is also a decorator for registering your ModelAdmin classes. 





```python
from django.contrib import admin 
from .models import Author 

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass 

```





# ModelAdmin options 



The ModelAdmin is very flexible. It has a several options for dealing with customising the interface. 





```python
from django.contrib import admin 

class AuthorAdmin(admin.ModelAdmin):
    date_hierarchy = 'pub_date'
    
```



# Examples 



```python
from django.contrib import admin 
from django.db import models 

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    birthday = models.DateField()
    
    def born_in_fifties(self):
        return self.birthday.strftime('%Y')[:3] == '195'
    born_in_fifties.boolean = True 
    
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'born_in_fifities')
```

