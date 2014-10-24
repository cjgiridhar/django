# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_accesstoken'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accesstoken',
            name='access_token',
        ),
        migrations.AddField(
            model_name='accesstoken',
            name='user_id',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
    ]
