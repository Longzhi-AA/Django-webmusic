from django.conf.urls import url
from user.views import *

urlpatterns = [
    url(r'^signin$',user_login,name='user_login'),
    url(r'^logout$',user_logout,name='user_logout'),
    url(r'^signup$',reg_user,name='user_signup'),
    url(r'^comments/(?P<music_id>\d+)$',user_comments,name='user_comments')
]
