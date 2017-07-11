#coding=utf-8
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from models import *
from hashlib import sha1
import datetime
from tt_goods.models import GoodsInfo


# from ttsx01.fresh.tt_goods.models import GoodsInfo

# Create your views here.
class a():
    pass


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
    # print 'cookies里面对数据'
    # print uname
    # print '1111'
    context = {'title':'天天生鲜-登录','uname':uname}
    return render(request, 'tt_user/login.html', context)

# def user_judge(request):
#     vl = request.GET
#     uname = vl.get('uname')
#     upwd = vl.get('upwd')
#     list = UserInfo.objects.filter(uname=uname)
#     context = {'pwd':0,'name':0}
#     print '11111111111111111111111111111111'
#     # print(list[0].uname)
#     print '22222222222222222222222222222222'
#     if list:
#         context['name'] = 1
#         s1 = sha1()
#         s1.update(upwd)
#         upwd = s1.hexdigest()
#         if list[0].upwd == upwd:
#             context['pwd'] = 1
#     return JsonResponse(context)

def userok(request):
    # vl = request.POST
    vl = request.GET
    uname = vl.get('username')
    upwd = vl.get('pwd')
    uwrite = vl.get('checked')
    list = UserInfo.objects.filter(uname=uname)
    context = {'pwd':'','name':'','uname':uname,'upwd':upwd, 'ok':0}
    if list:
        s1 = sha1()
        s1.update(upwd)
        upwd = s1.hexdigest()
        if list[0].upwd == upwd:
            request.session['uid'] = list[0].id
            request.session.set_expiry(0)
            context['ok'] = 1
            response = JsonResponse(context)
            if uwrite:
                response.set_cookie('uname', uname, expires=datetime.datetime.now() + datetime.timedelta(days = 7))
            else:
                response.set_cookie('uname', '', max_age=-1)
            return response
        else:
            context['pwd'] = '密码错误'
            # return render(request, 'tt_user/login.html/', context)
            return JsonResponse(context)

    # 帐号不存在
    context['name'] = '帐号不存在'
    # return render(request, 'tt_user/login.html/', context)
    return JsonResponse(context)


# user info
def user(request):
    # user id
    uid = request.session.get('uid')
    if uid == -1:
        return HttpResponseRedirect('/')
    user = UserInfo.objects.filter(id=uid)[0]

    # user address info
    # addr = UserInfo.objects.filter(address__id=1)
    try:
        addr = address.objects.filter(user_id_id=uid)[0]
    except Exception:
        addr = a
        addr.aname = '空'
        addr.aaddr = '空'
        addr.atel = '空'
        addr.acode = '空'
    context = {'name':user.uname, 'uname':addr.aname, 'addr':addr.aaddr, 'tel':addr.atel, 'code':addr.acode, 'uid':uid}
    return JsonResponse(context)


def info(request):
    uid = request.session.get('uid')
    if uid > 0:
        context = {'title':'天天生鲜-用户中心'}
        # 历史记录  读取session得到ｉｄ
        sid_list = request.session.get('sid'+str(uid), '')
        goods = []
        if sid_list:
            for sid in sid_list:
                g = GoodsInfo.objects.filter(id=sid)
                goods += g
            context['goods'] = goods
        # print goods[0].id
        #
        return render(request, 'tt_user/info.html', context)
    else:
        return HttpResponseRedirect('/login/')


def order(request):
    uid = request.session.get('uid')
    if uid > 0:
        context = {'title': '天天生鲜-用户中心'}
        return render(request, 'tt_user/order.html', context)
    else:
        return HttpResponseRedirect('/login/')


def site(request):
    uid = request.session.get('uid')
    if uid > 0:
        context = {'title': '天天生鲜-用户中心'}
        return render(request, 'tt_user/site.html', context)
    else:
        return HttpResponseRedirect('/login/')


def site_addr(request):
    user = request.POST
    uname = user.get('uname')
    uinner = user.get('uinner')
    ucode = user.get('ucode')
    utel = user.get('utel')
    # print uname,uinner,ucode,utel  # 测试用
    uid = request.session.get('uid') # 用户id
    try:
        # addr = UserInfo.objects.filter(address__id=1)
        addr = address.objects.filter(user_id=uid)[0]
    except Exception:
        addr = address()
    addr.aname = uname
    addr.aaddr = uinner
    addr.atel = utel
    addr.acode = ucode
    addr.user_id_id = uid
    addr.save()
    # addr = address.objects.filter(id=uid)[0]
    return HttpResponseRedirect('/site/')





def exit(request):
    request.session['uid'] = -1
    return HttpResponseRedirect('/')

def record(request):
    sid = request.GET.get('sid')
    uid = request.session.get('uid')
    info = address.objects.filter(user_id=uid)[0]
    info.arecord = sid
    info.save()
    print info.arecord
    print sid
    return JsonResponse({'a': 'hello', 'h2': 'world'})