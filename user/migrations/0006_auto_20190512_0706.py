# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-11 23:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20190512_0700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='my_list',
            name='author',
            field=models.IntegerField(max_length=255, verbose_name='歌手'),
        ),
        migrations.AlterField(
            model_name='my_list',
            name='music_name',
            field=models.IntegerField(max_length=255, verbose_name='歌曲'),
        ),
    ]