# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-13 11:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metrics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metrics',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
