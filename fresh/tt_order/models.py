#coding=utf-8
from django.db import models
from tt_user.models import UserInfo
# Create your models here.

class OrderInfo(models.Model):
    user = models.ForeignKey('UserInfo')   #用户
    data = models.DateTimeField(auto_now_add=True)     #时间
    order = models.CharField(max_length=20)    #订单号　　　ｉｄ
    addr =  models.CharField(max_length=100)    #地址
    status = models.CharField(max_length=10)   #付款状态状态
    num_price = models.DecimalField(decimal_places=2)    #总价格


class OrderGoods(models.Model):
    goods_img = models.ImageField()       #图片
    goods_title = models.CharField(50)     #标题
    goods_price = models.DecimalField(decimal_places=2)     #价格
    goods_unit = models.CharField(max_length=10)      #单位
    goods_count = models.IntegerField()     #数量




"""
28395540886787525
12345678901234567
    user，时间，订单号，付款状态,地址， 商品总价格
           商品图片,商品名称，商品价格，商品单位，商品数量
"""
