from django.contrib import admin
from music.models import *
from user.models import Singers
# Register your models here.
class User_admin(admin.ModelAdmin):
    pass
class Music_info_admin(admin.ModelAdmin):
    pass

class Music_kind_admin(admin.ModelAdmin):
    pass

class Singer_admin(admin.ModelAdmin):
    pass

class Usercomments_admin(admin.ModelAdmin):
    pass

admin.site.register(Myusers,User_admin)
admin.site.register(Usermoviecomments,Usercomments_admin)
admin.site.register(Music_kinds,Music_info_admin)
admin.site.register(Music_info,Music_info_admin)
admin.site.register(Singers,Singer_admin)