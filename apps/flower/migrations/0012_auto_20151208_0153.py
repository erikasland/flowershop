# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-08 01:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flower', '0011_cart_flowerid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='flower',
        ),
        migrations.AddField(
            model_name='cart',
            name='flower',
            field=models.ManyToManyField(to='flower.Flower'),
        ),
    ]
