# Generated by Django 3.1.2 on 2020-10-04 19:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='babytrack',
            name='time',
        ),
        migrations.AlterField(
            model_name='babytrack',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 4, 19, 44, 5, 250402)),
        ),
        migrations.AlterField(
            model_name='babytrack',
            name='leftside',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='babytrack',
            name='rightside',
            field=models.IntegerField(default=0),
        ),
    ]
