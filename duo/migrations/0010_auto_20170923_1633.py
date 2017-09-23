# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-23 08:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('duo', '0009_auto_20170731_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='nodepowerarchive',
            name='latest_time',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='nodepowerarchive',
            name='latest_total',
            field=models.FloatField(default=0),
        ),
    ]
