# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-23 17:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tweetsentiments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='my_col',
            fields=[
                ('document_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='tweetsentiments.Document')),
            ],
            bases=('tweetsentiments.document',),
        ),
    ]