#coding=utf-8
from django.shortcuts import render
from django.http import JsonResponse
from models import *
# Create your views here.


class a:
    pass
def add_cart(request):
    goods_id = request.GET.get('goods')
    goods_count = request.GET.get('goods_count')
    uid = request.session.get('uid')
    # 查询有没有此商品
    goods_list = CartInfo.objects.filter(user=uid, goods=goods_id)
    if len(goods_list)>0:
        goods_list[0].num += 1
        print goods_list[0].num
        print '1111111'
        goods_list[0].save()
    else:
        cart = CartInfo()
        cart.goods_id = goods_id
        cart.user_id = uid
        cart.num = goods_count
        cart.save()
    goods_kind_num_list = CartInfo.objects.filter(user=uid)  # 商品种类个数
    goods_num = 0
    for goods in goods_kind_num_list:
        goods_num += goods.num
    print goods_num
    return JsonResponse({'goods_num':goods_num})

def goods_count(request):
    uid = request.session.get('uid')
    goods_kind_num_list = CartInfo.objects.filter(user=uid)  # 商品种类个数
    goods_num = 0
    for goods in goods_kind_num_list:
        goods_num += goods.num
    return JsonResponse({'goods_num': goods_num})

def cart(request):
    context = {'title': '天天生鲜-购物车','inner_title':'购物车'}
    uid = request.session.get('uid')
    goods_list = CartInfo.objects.filter(user=uid)
    context['goods_list'] = goods_list
    return render(request, 'tt_cart/cart.html', context)


def revise_cart(request):
    revise = request.GET.get('revise')
    goods_id = request.GET.get('goods_id')
    # 提取购物车信息　进行　增删改查
    uid = request.session.get('uid')
    goods_car_id = CartInfo.objects.filter(id=goods_id)[0]
    if revise == '1':
        goods_car_id.num += 1
    elif revise == '2':
        goods_car_id.num -= 1
    elif revise == '4':
        pass # xiu gai
    goods_car_id.save()

    if revise == '3' or goods_car_id.num <= 0:
        goods_car_id.delete()
        goods_car_id = a()
        goods_car_id.num = 0
    return JsonResponse({'goods_num':goods_car_id.num})