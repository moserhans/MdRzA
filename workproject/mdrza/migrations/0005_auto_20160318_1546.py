# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-18 15:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mdrza', '0004_auto_20160315_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='radler',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='members', to='mdrza.team'),
        ),
    ]
