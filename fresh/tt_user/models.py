#coding=utf-8
from django.db import models

# Create your models here.

# import sys
# sys.path.append("..")
# from tt_goods.models import *

class UserInfo(models.Model):
    uname = models.CharField(max_length=20)
    upwd = models.CharField(max_length=40)
    uemail = models.CharField(max_length=40)

class address(models.Model):
    aname = models.CharField(max_length=10)
    aaddr = models.CharField(max_length=100)
    atel = models.CharField(max_length=11)
    acode = models.CharField(max_length=6)
    user_id = models.ForeignKey('UserInfo')

# class RecordInfo(models.Model):
#     record = models.CharField(max_length=20)
#     rgoods = models.ForeignKey('GoodsInfo')
#
# 
#
# '''
# 历史记录
# 购物车
# 时间
# 个数
# 付款状态
#  '''