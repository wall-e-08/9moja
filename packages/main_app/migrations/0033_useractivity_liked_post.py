# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-05 04:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0032_auto_20171204_0634'),
    ]

    operations = [
        migrations.AddField(
            model_name='useractivity',
            name='liked_post',
            field=models.ManyToManyField(to='main_app.Post'),
        ),
    ]
