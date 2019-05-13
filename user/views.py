from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import check_password, make_password
from user.forms import Reg_form, Login_form,Usercommentsform,Mylistform,Myfavorlistform
from music.models import Myusers
from user.models import Singers,My_list,Music_info,My_favorite
from copy import deepcopy

# Create your views here.


def reg_user(request):  #注册函数

    if request.method == 'GET':
        form = Reg_form()
        return render(request, "signup.html", {'form': form})
    if request.method == 'POST':
        form = Reg_form(request.POST)
        if not form.is_valid():
            return HttpResponse('填写格式有误')
        form.instance.password = make_password(form.instance.password)
        refer_url = request.META['HTTP_REFERER']
        new_user = form.save()
        login(request, new_user)
        return redirect(refer_url.split('/user')[0] + '/index')


def user_login(request):  #登录函数
    # refer_url = request.META['HTTP_REFERER']
    if request.method == 'GET':
        form = Login_form()
        return render(request, 'signin.html', {'form': form})
    if request.method == 'POST':
        refer_url = request.META['HTTP_REFERER']

        userlogin = Login_form(request.POST)
        if not userlogin.is_valid():
            return HttpResponse('登录失败')
        data = userlogin.cleaned_data
        try:
            user = Myusers.objects.filter(username=data['username'])[0]
        except Exception:
            return HttpResponse('用户不存在')
        encode_pwd = user.password

        is_true = False
        if check_password(data['password'], encode_pwd):
            is_true = True
        if is_true:
            login(request, user)
            return redirect(refer_url.split('/user')[0] + '/index')
        else:
            return HttpResponse('密码错误')


def user_logout(request):  #退出函数
    refer_url = request.META['HTTP_REFERER']
    logout(request)
    return redirect(refer_url)

def user_comments(request,music_id):  #用户评论
    refer_url = request.META['HTTP_REFERER']
    data = deepcopy(request.POST)
    try:
        data['user'] = request.user.pk
    except Exception:
        data['user'] = 0
    data['music'] = music_id
    res_data = Usercommentsform(data)
    if not res_data.is_valid():
        return redirect(refer_url)
    try:
        res_data.save()
    except Exception:
        return HttpResponse('用户不能重复评论')
    return redirect(refer_url)

def addmusic(request,music_id):   #增加音乐到歌单
    refer_url = request.META['HTTP_REFERER']

    # if request.method == 'GET':
    #     form = Mylistform()
    #     return redirect(refer_url)
    list_dic={'user_id':request.user.pk,'music_id':int(music_id)}
    form = Mylistform(list_dic)
    if not form.is_valid():
        return HttpResponse('填写格式有误')
    try:
        form.save()
        return redirect(refer_url)

    except Exception:
        return HttpResponse('添加错误')

def addfavormusic(request,music_id):   #增加音乐到歌单
    refer_url = request.META['HTTP_REFERER']

    # if request.method == 'GET':
    #     form = Mylistform()
    #     return redirect(refer_url)
    list_dic={'user_id':request.user.pk,'music_id':int(music_id)}
    form = Myfavorlistform(list_dic)
    if not form.is_valid():
        return HttpResponse('填写格式有误')
    try:
        form.save()

        return redirect(refer_url)

    except Exception:
        return HttpResponse('添加错误')

def deletmusic(request,music_id):
    refer_url = request.META['HTTP_REFERER']
    user_id = request.user.pk
    data = My_list.objects.filter(user_id=user_id,music_id=music_id)

    data[0].delete()
    return redirect(refer_url)
def deletfavormusic(request,music_id):
    refer_url = request.META['HTTP_REFERER']
    user_id = request.user.pk
    data = My_favorite.objects.filter(user_id=user_id,music_id=music_id)

    data[0].delete()
    return redirect(refer_url)


def showlist(request):
    user_id = request.user.pk
    user_list = []
    try:
        for user_music in My_list.objects.filter(user_id=user_id).order_by('-id'):
            music_info = Music_info.objects.get(pk=user_music.music_id)
            user_list.append(music_info)
    except Exception:
        return user_list
    return user_list

