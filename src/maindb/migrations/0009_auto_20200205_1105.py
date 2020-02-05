# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2020-02-05 11:05
from __future__ import unicode_literals

from django.db import migrations
import helpers.director.model_func.cus_fields.jsonable


class Migration(migrations.Migration):

    dependencies = [
        ('maindb', '0008_calltask'),
    ]

    operations = [
        migrations.AddField(
            model_name='calltask',
            name='tone_list',
            field=helpers.director.model_func.cus_fields.jsonable.JsonAbleField(blank=True, default=[], verbose_name='拨打内容'),
        ),
        migrations.AlterField(
            model_name='calltask',
            name='dst_uid',
            field=helpers.director.model_func.cus_fields.jsonable.JsonAbleField(verbose_name='接收用户'),
        ),
    ]
