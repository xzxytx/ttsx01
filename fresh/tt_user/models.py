from django.db import models

# Create your models here.

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

