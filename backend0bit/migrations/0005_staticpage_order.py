# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-14 18:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend0bit', '0004_auto_20161003_0850'),
    ]

    operations = [
        migrations.AddField(
            model_name='staticpage',
            name='order',
            field=models.IntegerField(default=0, unique=True),
            preserve_default=False,
        ),
    ]
