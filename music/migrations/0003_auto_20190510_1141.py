# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-10 03:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20190510_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermoviecomments',
            name='music',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.Music_info', verbose_name='歌曲名'),
        ),
    ]