# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tt_user', '0002_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='arecord',
            field=models.CharField(default=b'', max_length=40),
        ),
    ]
