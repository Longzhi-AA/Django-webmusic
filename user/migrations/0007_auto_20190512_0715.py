# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-11 23:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20190512_0706'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='my_list',
            name='author',
        ),
        migrations.RemoveField(
            model_name='my_list',
            name='music_name',
        ),
        migrations.AddField(
            model_name='my_list',
            name='music_id',
            field=models.IntegerField(default=0, verbose_name='歌曲'),
        ),
        migrations.AddField(
            model_name='my_list',
            name='user_id',
            field=models.IntegerField(default=0, verbose_name='用户'),
            preserve_default=False,
        ),
    ]
