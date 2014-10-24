# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20141024_0147'),
    ]

    operations = [
        migrations.CreateModel(
            name='DefaultRole',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('attribute_default', models.IntegerField(verbose_name=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='user',
            name='access',
        ),
        migrations.DeleteModel(
            name='UserAccess',
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.CharField(default=b'DefaultRole', max_length=20),
            preserve_default=True,
        ),
    ]
