# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-05 12:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0016_auto_20171105_1026'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='uncategorized', max_length=25)),
                ('slug', models.SlugField(editable=False)),
            ],
        ),
        migrations.AddField(
            model_name='categorize',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Category'),
        ),
        migrations.AddField(
            model_name='categorize',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Post'),
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(through='main_app.Categorize', to='main_app.Category'),
        ),
    ]