# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-18 22:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radio', '0005_talkgroup_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='talkgroup',
            name='common_name',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]