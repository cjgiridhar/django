# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_accesstoken'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AccessToken',
        ),
    ]
