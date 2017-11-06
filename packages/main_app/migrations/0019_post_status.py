# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-06 07:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0018_auto_20171105_1855'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('p', 'Published'), ('u', 'Unpublished'), ('a', 'Archived')], default='p', max_length=1),
            preserve_default=False,
        ),
    ]