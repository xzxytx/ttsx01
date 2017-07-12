#coding=utf-8
from django.db import models

# Create your models here.


# from ..tt_goods.models import *

class UserInfo(models.Model):
    uname = models.CharField(max_length=20)
    upwd = models.CharField(max_length=40)
    uemail = models.CharField(max_length=40)

class address(models.Model):
    aname = models.CharField(max_length=10)
    aaddr = models.CharField(max_length=100)
    atel = models.CharField(max_length=11)
    acode = models.CharField(max_length=6)
    # arecord = models.CharField(max_length=40)  # 历史记录
    user_id = models.ForeignKey('UserInfo')




'''
历史记录
购物车
时间
个数
付款状态
 '''