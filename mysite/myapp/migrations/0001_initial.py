# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tastypie.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DesignerRole',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('role_name', models.CharField(max_length=200)),
                ('analytics', models.IntegerField(verbose_name=1)),
                ('web_themes', models.IntegerField(verbose_name=2)),
                ('ux', models.IntegerField(verbose_name=2)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('group_name', models.CharField(max_length=200)),
                ('create_date', models.DateTimeField(default=tastypie.utils.timezone.now)),
                ('is_billed', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hotel_name', models.CharField(max_length=200)),
                ('hotel_city', models.CharField(max_length=200)),
                ('hotel_region', models.CharField(max_length=200)),
                ('create_date', models.DateTimeField(default=tastypie.utils.timezone.now)),
                ('pricing_plan', models.CharField(default=b'Basic', max_length=200)),
                ('group', models.ForeignKey(to='myapp.Group')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MarketingRole',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('role_name', models.CharField(max_length=200)),
                ('room_rates', models.IntegerField(verbose_name=2)),
                ('promotions', models.IntegerField(verbose_name=2)),
                ('analytics', models.IntegerField(verbose_name=1)),
                ('web_themes', models.IntegerField(verbose_name=0)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ResellerRole',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('role_name', models.CharField(max_length=200)),
                ('group', models.IntegerField(verbose_name=0)),
                ('hotel', models.IntegerField(verbose_name=2)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_first_name', models.CharField(max_length=200)),
                ('user_last_name', models.CharField(max_length=200)),
                ('create_date', models.DateTimeField(default=tastypie.utils.timezone.now)),
                ('hotel', models.ForeignKey(to='myapp.Hotel')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserAccess',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_type', models.CharField(max_length=20)),
                ('user_access', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='user',
            name='user_access_id',
            field=models.ForeignKey(to='myapp.UserAccess'),
            preserve_default=True,
        ),
    ]
