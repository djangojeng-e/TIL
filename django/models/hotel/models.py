from django.db import models

# Create your models here.


class Feature(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=30)
    features = models.ManyToManyField(Feature)

    def __str__(self):
        return self.name

