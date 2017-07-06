# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tt_user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('aname', models.CharField(max_length=10)),
                ('aaddr', models.CharField(max_length=100)),
                ('atel', models.CharField(max_length=11)),
                ('acode', models.CharField(max_length=6)),
                ('user_id', models.ForeignKey(to='tt_user.UserInfo')),
            ],
        ),
    ]
