# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-23 05:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0021_auto_20171119_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(upload_to='%Y-%m-%d'),
        ),
    ]
