# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-10-23 22:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qr_app', '0004_auto_20191023_2044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qr',
            name='photo',
        ),
        migrations.AddField(
            model_name='qr',
            name='imgfile',
            field=models.ImageField(blank=True, null=True, upload_to='pictures/%Y/%m/%d/'),
        ),
    ]