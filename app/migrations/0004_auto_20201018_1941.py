# Generated by Django 3.1.2 on 2020-10-18 19:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20201017_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='babytrack',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 18, 19, 41, 56, 882316)),
        ),
    ]