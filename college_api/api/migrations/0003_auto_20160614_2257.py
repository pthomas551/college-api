# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-14 22:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20160614_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='college',
            name='attributes',
            field=models.ManyToManyField(blank=True, to='api.Attribute'),
        ),
    ]
