# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-20 06:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('POC', '0005_auto_20191119_0941'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='zip',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='POC.City'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='POC.Country'),
        ),
    ]
