# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20141024_0415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_access',
            field=models.ForeignKey(to='myapp.UserAccess', null=True),
        ),
    ]
