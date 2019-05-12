"""webmusic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.views.static import serve
from webmusic.settings import BASE_DIR,MEDIA_ROOT
import os
from music.views import *
urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^static/(?P<path>.*)$', serve, {'document_root': os.path.join(BASE_DIR,'static_root')}),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),

    url(r'^user/',include('user.urls')),


    url(r'^index/', index, name='index'),
    url(r'^single/(?P<music_id>\d+)$',single,name='single_music'),

    url(r'^listen/', listen, name='listen'),
    url(r'^list/', list, name='list'),
    url(r'^video/', video, name='video'),
    url(r'^player/', player, name='player'),

]