# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tt_user', '0005_remove_address_arecord'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderGoods',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('goods_img', models.ImageField(upload_to=b'')),
                ('goods_title', models.CharField(max_length=50)),
                ('goods_price', models.DecimalField(max_digits=5, decimal_places=2)),
                ('goods_unit', models.CharField(max_length=10)),
                ('goods_count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('order', models.CharField(max_length=20)),
                ('addr', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=10)),
                ('num_price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('user', models.ForeignKey(to='tt_user.UserInfo')),
            ],
        ),
        migrations.AddField(
            model_name='ordergoods',
            name='order',
            field=models.ForeignKey(to='tt_order.OrderInfo'),
        ),
    ]
