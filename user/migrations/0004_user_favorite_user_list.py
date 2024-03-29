# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-10 01:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20190510_0957'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0003_my_favorite_my_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('music_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.Music_info', verbose_name='歌曲名')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户名')),
            ],
        ),
        migrations.CreateModel(
            name='User_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('music_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.Music_info', verbose_name='歌曲名')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户名')),
            ],
        ),
    ]
