from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms
from django.utils.timezone import now
# Create your models here.

class Music_kinds(models.Model):
    name = models.CharField(max_length=255,verbose_name='音乐类型')
    desc = models.CharField(max_length=255,verbose_name='类型描述')

    def __str__(self):
        return self.name

class Music_info(models.Model):  #音乐信息表
    music_name = models.CharField(max_length=255,verbose_name="音乐名")
    author = models.CharField(max_length=255,verbose_name="歌手")
    music_kind = models.ManyToManyField(Music_kinds)
    online_time = models.DateField(verbose_name='上线日期')
    music_img = models.ImageField(upload_to='images', null=True, default=None)
    music_audio = models.FileField(upload_to='audio', null=True, default=None)
    music_detail = models.TextField(verbose_name='详情', max_length=3000,blank=True)
    rating = models.IntegerField(verbose_name='评分',blank=True)


    def __str__(self):
        return self.music_name

class Myusers(AbstractUser):  #用户信息表
    user_img = models.ImageField(upload_to='images', null=True, blank=True)
    music_name = models.ManyToManyField(Music_info)



class Usermoviecomments(models.Model):  #用户评论信息表
    user = models.ForeignKey(Myusers,verbose_name="用户名")
    music = models.ForeignKey(Music_info,verbose_name='歌曲名')
    context = models.TextField(verbose_name='评论内容',max_length=1500)
    comment_time = models.DateTimeField(verbose_name='评论时间',default=now)
    class Meta:
        unique_together = ('user', 'music')

    def __str__(self):
        return '用户 {} 对:{} 评论到:{}'.format(self.user.username,self.music.music_name,self.context)