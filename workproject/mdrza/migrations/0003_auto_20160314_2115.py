# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-14 21:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mdrza', '0002_auto_20160314_2101'),
    ]

    operations = [
        migrations.RenameField(
            model_name='radler',
            old_name='name',
            new_name='nname',
        ),
        migrations.AddField(
            model_name='radler',
            name='vname',
            field=models.CharField(default='p', max_length=100),
            preserve_default=False,
        ),
    ]
