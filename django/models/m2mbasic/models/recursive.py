# ManyToMany 인데 자신을 참조할수 있는것
# 추천상품
# 같이 추천되는 상품


from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    similar_products = models.ManyToManyField('self')

    def __str__(self):
        return self.name

