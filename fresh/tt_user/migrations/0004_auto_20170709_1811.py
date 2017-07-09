# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tt_user', '0003_address_arecord'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='arecord',
            field=models.CharField(max_length=40),
        ),
    ]
