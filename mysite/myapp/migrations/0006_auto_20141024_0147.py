# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20141024_0129'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='user_access_id',
            new_name='access',
        ),
    ]
