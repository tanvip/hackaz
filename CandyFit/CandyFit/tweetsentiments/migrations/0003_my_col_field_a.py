# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-23 17:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweetsentiments', '0002_my_col'),
    ]

    operations = [
        migrations.AddField(
            model_name='my_col',
            name='field_a',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]