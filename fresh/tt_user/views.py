#coding=utf-8
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from models import *
from hashlib import sha1
import datetime
# Create your views here.

def index(request):
    return render(request, 'index.html')

def register(request):
    context = {'title':'天天生鲜-注册'}
    return render(request, 'tt_user/register.html', context)

def ok(request):
    vl = request.POST
    uname = vl.get('user_name')
    upwd = vl.get('pwd')
    email = vl.get('email')
    # print (type(uname))
    # 密码加密
    s1 = sha1()
    s1.update(upwd)
    upwd = s1.hexdigest()
    # 写入数据
    u = UserInfo()
    u.uname = uname
    u.upwd = upwd
    u.uemail = email
    u.save()
    #
    # user = UserInfo.objects.create('a', 'b', 'c')
    # user.save()
    return render(request, 'index.html')

def register_valid(request):
    uname = request.GET.get('uname')
    uname = UserInfo.objects.filter(uname=uname).count()
    context = {'uname':uname}
    return JsonResponse(context)

def login(request):
    uname = request.COOKIES.get('uname', '')
    context = {'title':'天天生鲜-登录','uname':uname}
    return render(request, 'tt_user/login.html', context)

def user_judge(request):
    vl = request.GET
    uname = vl.get('uname')
    upwd = vl.get('upwd')
    list = UserInfo.objects.filter(uname=uname)
    context = {'pwd':0,'name':0}
    print '11111111111111111111111111111111'
    # print(list[0].uname)
    print '22222222222222222222222222222222'
    if list:
        context['name'] = 1
        s1 = sha1()
        s1.update(upwd)
        upwd = s1.hexdigest()
        if list[0].upwd == upwd:
            context['pwd'] = 1
    return JsonResponse(context)

def userok(request):
    vl = request.POST
    uname = vl.get('username')
    upwd = vl.get('pwd')
    uwrite = vl.get('checked')
    # str = '%s---%s' % (uname, upwd)

    list = UserInfo.objects.filter(uname=uname)
    context = {'pwd':'','name':'','uname':uname,'upwd':upwd}

    if list:
        s1 = sha1()
        s1.update(upwd)
        upwd = s1.hexdigest()
        # print upwd
        if list[0].upwd == upwd:
            response = redirect('/')
            if uwrite:
                response.set_cookie('uname', uname, expires=datetime.datetime.now() + datetime.timedelta(days = 7))
            else:
                response.set_cookie('uname', '', max_age=-1)
            # return HttpResponse('登录成功')
            return response
            # return HttpResponseRedirect('/', context)
        else:
            # 密码错误
            context['pwd'] = '密码错误'
            # return JsonResponse(context)
            return render(request, 'tt_user/login.html/', context)
            # return HttpResponseRedirect(request, '/', context)

    # 帐号不存在
    context['name'] = '帐号不存在'
    return render(request, 'tt_user/login.html/', context)

    # return render(request, 'index.html')
