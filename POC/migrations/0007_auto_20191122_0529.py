# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-22 05:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('POC', '0006_auto_20191120_0612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='POC.City'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='POC.Country'),
        ),
    ]
