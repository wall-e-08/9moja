# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-28 10:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0038_post_nsfw'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='nsfw',
            field=models.BooleanField(default=False, verbose_name='Not Safe for Work'),
        ),
    ]
