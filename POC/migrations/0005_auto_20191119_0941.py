# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-19 09:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('POC', '0004_auto_20191119_0609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='POC.City'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='POC.Country'),
        ),
    ]
