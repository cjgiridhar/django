# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_auto_20141024_0433'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('room_name', models.CharField(max_length=200)),
                ('room_type', models.CharField(default=b'Basic', max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Room_Rates',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('isSeasonal', models.BooleanField(default=False)),
                ('pricing', models.CharField(default=b'Basic', max_length=200)),
                ('current_price', models.BigIntegerField()),
                ('room', models.ForeignKey(to='myapp.Room')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
