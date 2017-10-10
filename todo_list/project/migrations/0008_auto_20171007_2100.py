# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-07 21:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_auto_20171006_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_status',
            field=models.CharField(choices=[('DONE', 'Done Task'), ('NOTDONE', 'Not Done Task')], default='NOTDONE', max_length=7),
        ),
    ]
