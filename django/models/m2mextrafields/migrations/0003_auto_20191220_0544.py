# Generated by Django 2.2.8 on 2019-12-20 05:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('m2mextrafields', '0002_player_clubs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='clubs',
        ),
        migrations.DeleteModel(
            name='Career',
        ),
        migrations.DeleteModel(
            name='Club',
        ),
        migrations.DeleteModel(
            name='Player',
        ),
    ]