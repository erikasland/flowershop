# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-04 02:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flower', '0002_flower_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flower',
            name='email',
        ),
        migrations.AddField(
            model_name='flower',
            name='link',
            field=models.CharField(default='somestring', max_length=200),
            preserve_default=False,
        ),
    ]
