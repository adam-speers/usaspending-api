# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-22 15:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0005_auto_20161219_1358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submissionattributes',
            name='user_id',
        ),
    ]
