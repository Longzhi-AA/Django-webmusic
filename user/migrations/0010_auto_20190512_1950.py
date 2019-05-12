# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-12 11:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_auto_20190512_0922'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='my_favorite',
            name='author',
        ),
        migrations.RemoveField(
            model_name='my_favorite',
            name='music_name',
        ),
        migrations.AddField(
            model_name='my_favorite',
            name='music_id',
            field=models.CharField(default='null', max_length=255, verbose_name='歌曲'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='my_favorite',
            name='user_id',
            field=models.CharField(default='1', max_length=255, verbose_name='用户'),
            preserve_default=False,
        ),
    ]
