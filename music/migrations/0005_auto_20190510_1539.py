# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-10 07:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_myusers_user_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermoviecomments',
            name='context',
            field=models.TextField(max_length=1500, verbose_name='评论内容'),
        ),
    ]
