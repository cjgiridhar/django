# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20141024_0405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_access',
            field=models.ForeignKey(default=b'1', to='myapp.UserAccess'),
        ),
    ]
