# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-05 04:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0033_useractivity_liked_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserExtended',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likes', models.IntegerField(default=0)),
                ('shares', models.IntegerField(default=0)),
                ('uploads', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='UserPostRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.UserExtended')),
            ],
        ),
        migrations.RemoveField(
            model_name='useractivity',
            name='liked_post',
        ),
        migrations.RemoveField(
            model_name='useractivity',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserActivity',
        ),
        migrations.AddField(
            model_name='userextended',
            name='liked_post',
            field=models.ManyToManyField(through='main_app.UserPostRelation', to='main_app.Post'),
        ),
        migrations.AddField(
            model_name='userextended',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]
