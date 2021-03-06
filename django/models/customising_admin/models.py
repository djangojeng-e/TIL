from django.db import models

# Create your models here.
from django.db import models
#
# class Author(models.Model):
#     name = models.CharField(max_length=100)
#     title = models.CharField(max_length=3)
#     birth_date = models.DateField(blank=True, null=True)
#
#     def __str__(self):
#         return f'저자 : {self.name} 제목 : {self.title}'
#
#
# class Website(models.Model):
#     author = models.ForeignKey(Author, on_delete=models.CASCADE)
#     url = models.URLField(max_length=300)
#     title = models.CharField(max_length=30)
#     content = models.TextField
#

from django.contrib import admin
from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    birthday = models.DateField()

    def born_in_fifties(self):
        return self.birthday.strftime('%Y')[:3] == '195'
    born_in_fifties.boolean = True


class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'born_in_fifties')
