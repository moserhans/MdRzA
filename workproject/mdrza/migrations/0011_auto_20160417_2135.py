# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-17 19:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mdrza', '0010_radler_gesamttage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='woche',
            name='di',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='woche',
            name='do',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='woche',
            name='fr',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='woche',
            name='mi',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='woche',
            name='mo',
            field=models.BooleanField(default=False),
        ),
    ]
