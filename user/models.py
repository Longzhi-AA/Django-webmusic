from django.db import models
from django import forms
from music.models import Music_info,Myusers
# Create your models here.
from django.contrib.auth import get_user_model
# Create your models here.
# Myuser = get_user_model()

class Singers(models.Model):  #所有歌手
    name = models.CharField(max_length=255,verbose_name='姓名')
    nation = models.CharField(max_length=255,verbose_name='国籍')
    detail = models.TextField(verbose_name='详情', max_length=3000, blank=True)
    img = models.ImageField(upload_to='avatar', null=True, default=None)

    def __str__(self):
        return self.name
class My_list(models.Model): #个人歌单
    music_id = models.CharField(max_length=255,verbose_name="歌曲")
    user_id = models.CharField(max_length=255,verbose_name="用户")


class My_favorite(models.Model):
    music_id = models.CharField(max_length=255, verbose_name="歌曲")
    user_id = models.CharField(max_length=255, verbose_name="用户")


class User_list(models.Model):  #测试用的个人歌单
    user = models.ForeignKey(Myusers,verbose_name="用户名")
    music_name = models.ForeignKey(Music_info,verbose_name='歌曲名')

class User_favorite(models.Model):#测试用的个人歌单
    user = models.ForeignKey(Myusers, verbose_name="用户名")
    music_name = models.ForeignKey(Music_info, verbose_name='歌曲名')
