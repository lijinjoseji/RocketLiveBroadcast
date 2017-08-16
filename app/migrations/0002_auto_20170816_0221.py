# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-16 02:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liveroom',
            name='room_img',
            field=models.ImageField(null=True, upload_to='img/covers'),
        ),
        migrations.AlterField(
            model_name='vertifyforgetpasswd',
            name='vertifytime',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 16, 2, 21, 19, 407596)),
        ),
        migrations.AlterField(
            model_name='vertifyregister',
            name='vertifytime',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 16, 2, 21, 19, 406044)),
        ),
    ]