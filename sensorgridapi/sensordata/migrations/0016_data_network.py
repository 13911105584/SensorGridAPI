# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-05-11 23:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sensordata', '0015_network'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='network',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sensordata.Network'),
        ),
    ]
