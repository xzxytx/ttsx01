# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tt_user', '0004_auto_20170709_1811'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='arecord',
        ),
    ]
