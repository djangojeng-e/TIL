# Generated by Django 2.2.8 on 2019-12-19 03:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database_models', '0006_ox'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ox',
            options={'ordering': ['horn_length'], 'verbose_name_plural': '뿔의 길이'},
        ),
    ]