# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-07 17:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0015_auto_20160807_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamo',
            name='fechaFin',
            field=models.DateField(default=datetime.datetime(2016, 8, 14, 17, 16, 55, 128535)),
        ),
    ]
