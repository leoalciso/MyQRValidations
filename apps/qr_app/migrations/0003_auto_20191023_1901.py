# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-10-23 19:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qr_app', '0002_qr'),
    ]

    operations = [
        migrations.CreateModel(
            name='Master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RenameModel(
            old_name='Company',
            new_name='All_QR',
        ),
        migrations.RemoveField(
            model_name='qr',
            name='company',
        ),
    ]
