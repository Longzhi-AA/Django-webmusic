# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-10 01:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usermoviecomments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('context', models.TextField(max_length=2500, verbose_name='评论内容')),
                ('comment_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='评论时间')),
                ('music', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.Music_info', verbose_name='评论电影')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户名')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='usermoviecomments',
            unique_together=set([('user', 'music')]),
        ),
    ]