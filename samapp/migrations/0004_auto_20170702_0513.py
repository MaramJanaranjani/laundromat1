# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-02 05:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('samapp', '0003_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='laundries',
            old_name='city_area_mapid',
            new_name='city_areamapid',
        ),
        migrations.AddField(
            model_name='profile',
            name='mobile',
            field=models.CharField(default=None, max_length=10, null=True),
        ),
    ]