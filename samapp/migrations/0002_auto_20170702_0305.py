# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-02 03:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('samapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laundries',
            name='city_area_mapid',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='laundries',
            name='sector_id',
            field=models.CharField(max_length=10),
        ),
    ]
