from django.contrib import admin

# Register your models here.
from .models import Author, Website


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    fields =('name', 'title')


@admin.register(Website)
class FlatPageAdmin(admin.ModelAdmin):
    fields = ('url', 'title', 'content')
