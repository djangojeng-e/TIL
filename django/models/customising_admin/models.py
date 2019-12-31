from django.db import models

# Create your models here.
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=3)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'저자 : {self.name} 제목 : {self.title}'


class Website(models.Model):
    url = models.URLField
    title = models.CharField(max_length=30)
    content = models.TextField

    def __str__(self):
        return self.url