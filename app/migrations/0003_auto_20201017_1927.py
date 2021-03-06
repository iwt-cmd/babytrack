# Generated by Django 3.1.2 on 2020-10-17 19:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20201004_1944'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='babytrack',
            name='sup_amount',
        ),
        migrations.RemoveField(
            model_name='babytrack',
            name='sup_b',
        ),
        migrations.RemoveField(
            model_name='babytrack',
            name='sup_f',
        ),
        migrations.AddField(
            model_name='babytrack',
            name='sup_b_amt',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='babytrack',
            name='sup_f_amt',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=3),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='babytrack',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 17, 19, 27, 0, 739481)),
        ),
    ]
