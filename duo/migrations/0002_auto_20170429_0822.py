# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-29 08:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('duo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='node_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='device',
            name='time',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='device',
            name='total',
            field=models.IntegerField(),
        ),
    ]