# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-28 07:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0026_auto_20171128_0722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(allow_unicode=True),
        ),
    ]