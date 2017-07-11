#coding=utf-8
from django.shortcuts import render
from models import *
from django.core.paginator import Paginator
from django.http import JsonResponse
# Create your views here.

def index(request):
    list = []
    typeinfo = TypeInfo.objects.all()
    for t in typeinfo:
        g = t.goodsinfo_set.order_by('-gclick')[0:4]  # click
        new = t.goodsinfo_set.order_by('-id')[0:4]  # id
        dict = {'t':t, 'click':g, 'new':new}
        list.append(dict)
        print g
    print '321321'
    context = {'title':'天天生鲜-首页', 'data':list}
    return render(request, 'index.html', context)

def list(request, type, order, page):
    # title img kg $
    t = TypeInfo.objects.filter(id=type)[0]
    # print t.ttitle
    new = t.goodsinfo_set.order_by('-id')[0:2]  # 2 new
    age = 2
    if order == '2':
        list = t.goodsinfo_set.order_by('gprice')  # 价格
        active = 'active2'
        age = 4
    elif order == '3':
        list = t.goodsinfo_set.order_by('-gclick')  # click
        active = 'active3'
    elif order == '4':
        list = t.goodsinfo_set.order_by('-gprice')  # 价格
        active = 'active2'
        age = 2
    else:
        list = t.goodsinfo_set.order_by('-id')  # 排序 默认
        active = 'active1'
    p = Paginator(list, 1)
    print p.page_range
    de = p.page(page)  # 那一页的数据
    context = {'title':'天天生鲜-商品列表', 'new':new, 'de':de,
               'id':type, active:'active', 'age':age, 'Paginator':p, 'order':order,
               'prev':de.number-1, 'next':de.number+1
               }
    return render(request, 'tt_goods/list.html', context)


def place(request):
    context = {'title':'天天生鲜-提交订单'}
    return render(request, 'tt_goods/place.html', context)


def detail(request, id):
    # 存储－－> session
    # 1.获取用户ｉｄ　　　２．获取商品ｉｄ　　　３．用户ｉｄ为键，商品ｉｄ为值存入session  失败：关闭浏览器就过期过期
    uid = request.session.get('uid')
    # 读取session 拼接值
    sidlist = request.session.get('sid'+str(uid), '')
    print sidlist
    if sidlist:
        if int(id) in sidlist:
            sidlist.remove(int(id))
        if len(sidlist) >=5:
            sidlist.pop()
        sidlist.insert(0, int(id))
    else:
        sidlist = [int(id)]
    # print sidlist
    request.session['sid'+str(uid)] = sidlist
    request.session.set_expiry(0)
    #
    goods = GoodsInfo.objects.filter(id=id)[0]
    # typeinfo = goods.gtype.ttitle
    context = {'title':'天天生鲜-商品详情', 'goods':goods}
    return render(request, 'tt_goods/detail.html', context)


def query(request):
    return render(request, 'tt_goods/query.html')























