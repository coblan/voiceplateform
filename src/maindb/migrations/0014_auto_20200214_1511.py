# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2020-02-14 15:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maindb', '0013_auto_20200214_1438'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='callevent',
            index=models.Index(fields=['channel'], name='maindb_call_channel_03fd3d_idx'),
        ),
        migrations.AddIndex(
            model_name='callrecord',
            index=models.Index(fields=['channel'], name='maindb_call_channel_5d21f0_idx'),
        ),
    ]
