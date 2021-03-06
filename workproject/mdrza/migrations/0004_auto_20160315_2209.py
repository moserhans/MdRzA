# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-15 22:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mdrza', '0003_auto_20160314_2115'),
    ]

    operations = [
        migrations.AddField(
            model_name='radler',
            name='gesamtkm',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='radler',
            name='km',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='gesamtkm',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='woche',
            name='di',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='woche',
            name='di_extra',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='woche',
            name='do',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='woche',
            name='do_extra',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='woche',
            name='fr',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='woche',
            name='fr_extra',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='woche',
            name='km',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='woche',
            name='kwnr',
            field=models.IntegerField(default=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='woche',
            name='mi',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='woche',
            name='mi_extra',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='woche',
            name='mo',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='woche',
            name='mo_extra',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='radler',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mdrza.team'),
        ),
    ]
