# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2020-01-06 10:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maindb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountinfo',
            name='uid',
            field=models.CharField(max_length=30, unique=True, verbose_name='用户统一ID'),
        ),
    ]
