# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2020-02-10 19:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maindb', '0009_auto_20200205_1105'),
    ]

    operations = [
        migrations.AddField(
            model_name='calltask',
            name='status',
            field=models.IntegerField(choices=[(0, '初始'), (1, '已经拨打')], default=0, verbose_name='状态'),
        ),
    ]