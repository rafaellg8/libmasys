# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-06 18:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0008_auto_20160806_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamo',
            name='fechaFin',
            field=models.DateField(default=datetime.datetime(2016, 8, 13, 18, 52, 45, 717233)),
        ),
    ]
