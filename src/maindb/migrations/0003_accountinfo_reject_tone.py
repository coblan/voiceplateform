# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2020-01-07 23:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maindb', '0002_auto_20200106_1028'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountinfo',
            name='reject_tone',
            field=models.CharField(blank=True, max_length=300, verbose_name='拒接电话语言'),
        ),
    ]
