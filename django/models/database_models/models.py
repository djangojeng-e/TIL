# # # from django.db import models
# # # #
# # # # # Create your models here.
# # # # #
# # # # # class Musician(models.Model):
# # # # #     first_name = models.CharField(max_length=50)
# # # # #     last_name = models.CharField(max_length=50)
# # # # #     instrument = models.CharField(max_length=100)
# # # # #
# # # # # class Album(models.Model):
# # # # #     artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
# # # # #     name = models.CharField(max_length=100)
# # # # #     release_date = models.DateField()
# # # # #     num_stars = models.IntegerField()
# # # #
# # # # # class Person(models.Model):
# # # # #     SHIRT_SIZES = (
# # # # #         ('S', 'Small'),
# # # # #         ('M', 'Medium'),
# # # # #         ('L', 'Large'),
# # # # #     )
# # # # #     name = models.CharField(max_length=60)
# # # # #     shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
# # # #
# # # # # Making choices in a conscise way.
# # # #
# # # #
# # # # # class Runner(models.Model):
# # # # #     MedalType = models.TextChoices('MedalType', 'GOLD SILVER BRONZE')
# # # # #     name = models.CharField(max_length=60)
# # # # #     medal = models.CharField(blank=True, choices=MedalType.choices, max_length=10)
# # # #
# # # # # TextChoices are not included in the model.
# # # #
# # # # #
# # # # # class Fruit(models.Model):
# # # # #     name = models.CharField(max_length=100, primary_key=True)
# # # #
# # # # class Person(models.Model):
# # # #     name = models.CharField(max_length=128)
# # # #
# # # #     def __str__(self):
# # # #         return self.name
# # # #
# # # #
# # # # class Group(models.Model):
# # # #     name = models.CharField(max_length=128)
# # # #     members = models.ManyToManyField(Person, through='Membership')
# # # #
# # # #     def __str__(self):
# # # #         return self.name
# # # #
# # # #
# # # # class Membership(models.Model):
# # # #     person = models.ForeignKey(Person, on_delete=models.CASCADE)
# # # #     group = models.ForeignKey(Group, on_delete=models.CASCADE)
# # # #     date_joined = models.DateField()
# # # #     invite_reason = models.CharField(max_length=64)
# # # #
# # #
# # # class Manufacturer(models.Model):
# # #     # ..
# # #     pass
# # #
# # # class Car(models.Model):
# # #     manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
# # from django.db import models
# #
# #
# # class Person(models.Model):
# #     SHIRT_SIZES = (
# #         ('S', 'Small'),
# #         ('M', 'Medium'),
# #         ('L', 'Large'),
# #     )
# #     name = models.CharField(max_length=60)
# #     shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
# #
# #
#
# from django.db import models
#
#
# class Person(models.Model):
#     name = models.CharField(max_length=128)
#
#     def __str__(self):
#         return self.name
#
#
# class Group(models.Model):
#     name = models.CharField(max_length=128)
#     members = models.ManyToManyField(Person, through='Membership')
#
#     def __str__(self):
#         return self.name
#
#
# class Membership(models.Model):
#     person = models.ForeignKey(Person, on_delete=models.CASCADE)
#     group = models.ForeignKey(Group, on_delete=models.CASCADE)
#     date_joined = models.DateField()
#     invite_reason = models.CharField(max_length=64)
