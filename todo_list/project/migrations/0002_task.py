# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 20:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_title', models.CharField(max_length=200)),
                ('task_priority', models.CharField(choices=[('H', 'High'), ('M', 'Medium'), ('L', 'Low')], max_length=1)),
                ('task_deadline', models.DateTimeField()),
                ('task_status', models.CharField(choices=[('DONE', 'Done Task'), ('NOTDONE', 'Not Done Task')], max_length=5)),
                ('task_project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Project')),
            ],
            options={
                'db_table': 'task',
            },
        ),
    ]
