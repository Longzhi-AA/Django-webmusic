from django.conf.urls import url
from user.views import *

urlpatterns = [
    url(r'^signin$',user_login,name='user_login'),
    url(r'^logout$',user_logout,name='user_logout'),
    url(r'^signup$',reg_user,name='user_signup'),

    url(r'^addmusic/(?P<music_id>\d+)$',addmusic,name='addmusic'),
    url(r'^addfavormusic/(?P<music_id>\d+)$',addfavormusic,name='addfavormusic'),
    url(r'^delmusic/(?P<music_id>\d+)$',deletmusic,name='delmusic'),
    url(r'^delfavormusic/(?P<music_id>\d+)$',deletfavormusic,name='delfavormusic'),
    url(r'^comments/(?P<music_id>\d+)$',user_comments,name='user_comments')
]
