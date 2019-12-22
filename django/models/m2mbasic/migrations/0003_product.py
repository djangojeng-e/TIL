# Generated by Django 2.2.8 on 2019-12-20 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('m2mbasic', '0002_auto_20191220_1716'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('similar_products', models.ManyToManyField(related_name='_product_similar_products_+', to='m2mbasic.Product')),
            ],
        ),
    ]