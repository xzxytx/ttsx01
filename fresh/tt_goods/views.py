#coding=utf-8
from django.shortcuts import render
from models import *
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

def list(request):
    context = {'title':'天天生鲜-商品列表'}
    return render(request, 'tt_goods/list.html', context)