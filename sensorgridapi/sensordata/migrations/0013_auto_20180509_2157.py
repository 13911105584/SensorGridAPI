# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-05-09 21:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sensordata', '0012_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='json',
            new_name='data',
        ),
    ]