#coding=utf-8
from django.shortcuts import render
from django.http import JsonResponse
from tt_cart.models import CartInfo
from models import *
from django.db import transaction
from django.core.paginator import Paginator
# Create your views here.
@transaction.atomic()
def place_order(request):
    cart_id_list = request.GET.get('cart_list')
    cart_id_list = cart_id_list.split(',')
    sid = transaction.savepoint()
    try:
        # 存
        num_price = 0
        order = OrderInfo()
        uid = request.session.get('uid')
        order.user_id = uid
        order.order = ''
        order.addr = ''
        order.status = '未支付'
        order.num_price = 0
        order.save()
        order = OrderInfo.objects.filter(user=uid,num_price=0)[0]  # 需要修改
        # 存订单数据
        for cart_id in cart_id_list:
            # 取
            cart = CartInfo.objects.filter(id=int(cart_id))[0]
            price = cart.goods.gprice
            count = cart.num
            # 存
            order_goods = OrderGoods()
            order_goods.order = order
            order_goods.goods_img = cart.goods.gpic
            order_goods.goods_title = cart.goods.gtitle
            order_goods.goods_price = price
            order_goods.goods_unit = cart.goods.gunit
            order_goods.goods_count = count
            order_goods.save()
            # 删
            cart.delete()

            if num_price == 0:
                # UserInfo　　存
                order.addr = str(cart.user.address_set.all()[0].aaddr.encode('utf-8')) + '  (' +\
                       str(cart.user.address_set.all()[0].aname.encode('utf-8')) + '  收)  ' +\
                       str(cart.user.address_set.all()[0].atel.encode('utf-8'))

            num_price += price*100 * count
        order.num_price = (num_price+1000)/100
        order.save()
        transaction.savepoint_commit(sid)
    except Exception:
        transaction.savepoint_rollback(sid)
        return JsonResponse({'ok':0})


    return JsonResponse({'ok':1})

def order_list(request):
    uid = request.session.get('uid')
    order_list = OrderInfo.objects.filter(user=uid)
    order_id_list = []
    for order in order_list:
        order_id_list.append(int(order.id))

    return JsonResponse({'order_id_list':str(order_id_list)})