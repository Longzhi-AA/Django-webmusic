from django.shortcuts import render,redirect
from music.models import Music_info,Usermoviecomments,Myusers
from user.models import Singers,My_list,User_list
from django.core.paginator import Paginator
from django.http import HttpResponse,JsonResponse
from user.forms import Usercommentsform,Mylistform
from user.views import addmusic,showlist
# Create your views here.


def index(request):  #主页
    list = My_list.objects.all()
    data = Music_info.objects.all()
    singers = Singers.objects.all()
    data = Music_info.objects.all().order_by('-id')
    ranks = data.order_by('-rating')
    new = Music_info.objects.filter(music_kind__name='最新')

    user_list = showlist(request)

    return render(request,'index.html',{'data':data,
                                        'new':new,
                                        'singers':singers,
                                        'ranks':ranks,
                                        'user_list':user_list,
                                        })

def pagein(request):  #分页函数
    ranking = Music_info.objects.all().order_by('-rating')
    paginator = Paginator(ranking,7)
    pass



def list(request): #歌单
    datas = User_list.objects.filter(user=request.user.pk)
    music_list = []
    for data in datas:
        music = data.music_name
        music_list.append(music)
    # print(music_list)

    return render(request, 'list.html',{'music_list':music_list})


def single(request,music_id): #单个音乐加载并播放
    commentmodel = Usercommentsform.Meta.model
    comments = commentmodel.objects.filter(music__id=music_id).order_by('-id')
    try:
        music = Music_info.objects.filter(pk=music_id)[0]
        addmusic(request, music_id)
    except Exception:
        return HttpResponse('404', 'bad address, not found')
    if not request.user.is_anonymous:
        user_list = showlist(request)

        data = Music_info.objects.all()
        comment_form = Usercommentsform()

        return render(request, 'single.html', {'music':music,
                                           'comment_form':comment_form,
                                           'comments':comments,
                                           'user_list':user_list,
                                           'data':data,
                                          })
    return render(request,'signin.html')


def profile(request, singer_id):  #歌手个人信息
    singer_data = Singers.objects.get(pk=singer_id)
    music_data = Music_info.objects.filter(author=singer_data.name)
    return render(request,'profile.html',{'singer_data':singer_data,
                                          'music_data':music_data})
