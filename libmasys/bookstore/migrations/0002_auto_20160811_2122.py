# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-11 21:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamo',
            name='fechaFin',
            field=models.DateField(default=datetime.datetime(2016, 8, 18, 21, 22, 2, 714633)),
        ),
    ]
