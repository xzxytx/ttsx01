
from django.db import models
from tinymce.models import HTMLField



# Create your models here.


class TypeInfo(models.Model):
    ttitle = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)

class GoodsInfo(models.Model):
    gtitle = models.CharField(max_length=50)  # title
    gpic = models.ImageField(upload_to='goods')  # img
    gprice = models.DecimalField(max_digits=5, decimal_places=2)  # 999.99
    gclick = models.IntegerField(default=0)  # hits
    gunit = models.CharField(max_length=20)  # 500g
    isDelete = models.BooleanField(default=False) # del
    gsubtitle = models.CharField(max_length=200)  # title inner
    gkucun = models.IntegerField(default=100)  # goods much
    gcontent = HTMLField()  # inner
    gtype = models.ForeignKey('TypeInfo')  # join

