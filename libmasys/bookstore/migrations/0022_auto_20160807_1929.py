# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-07 19:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0021_auto_20160807_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genero',
            name='nombre',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='fechaFin',
            field=models.DateField(default=datetime.datetime(2016, 8, 14, 19, 29, 3, 223146)),
        ),
    ]
