# Generated by Django 2.2.8 on 2019-12-20 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('m2mextrafields', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='clubs',
            field=models.ManyToManyField(through='m2mextrafields.Career', to='m2mextrafields.Club'),
        ),
    ]
