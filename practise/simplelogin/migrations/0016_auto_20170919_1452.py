# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-19 09:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simplelogin', '0015_auto_20170919_1435'),
    ]

    operations = [
        migrations.RenameField(
            model_name='messages',
            old_name='reciever',
            new_name='message_reciever',
        ),
        migrations.RenameField(
            model_name='messages',
            old_name='user',
            new_name='message_sender',
        ),
    ]
