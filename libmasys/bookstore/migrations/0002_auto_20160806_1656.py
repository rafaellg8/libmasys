# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-06 16:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Recursos',
            new_name='Recurso',
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='fechaFin',
            field=models.DateField(default=datetime.datetime(2016, 8, 13, 16, 56, 29, 131954)),
        ),
    ]
