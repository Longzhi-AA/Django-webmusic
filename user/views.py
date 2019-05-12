from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import check_password, make_password
from user.forms import Reg_form, Login_form,Usercommentsform,Mylistform
from music.models import Myusers
from copy import deepcopy

# Create your views here.


def reg_user(request):

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


def user_login(request):
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


def user_logout(request):
    refer_url = request.META['HTTP_REFERER']
    logout(request)
    return redirect(refer_url)

def play(request):
    pass


def user_addmusic(request):
    pass

def user_comments(request,music_id):
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
    if not request.user.is_anonymous:
        return HttpResponse('用户未登录，无法评论')
    try:
        res_data.save()
    except Exception:
        return  HttpResponse('用户不能重复评论')
    return redirect(refer_url)

def addmusic(request,music_id,user_id):
    refer_url = request.META['HTTP_REFERER']
    form = Mylistform()
    if form.is_valid():
        # data = form.cleaned_data

        form.music_id = music_id
        form.user_id = user_id
        try:
            form.save()

        except Exception:
            return redirect(refer_url)