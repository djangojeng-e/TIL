# Generated by Django 2.2.8 on 2019-12-13 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database_models', '0002_auto_20191213_0625'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fruit',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
