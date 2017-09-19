# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-18 13:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simplelogin', '0012_auto_20170918_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='first_name',
            field=models.CharField(default=None, max_length=64),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(default=None, max_length=64),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(default=None, max_length=254),
        ),
    ]
