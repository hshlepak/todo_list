# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-05 19:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_auto_20171005_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_day',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_time',
            field=models.TimeField(),
        ),
    ]
