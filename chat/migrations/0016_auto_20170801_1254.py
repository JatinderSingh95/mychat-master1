# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-01 07:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0015_auto_20170801_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='name',
            field=models.CharField(default=b'', max_length=200),
        ),
    ]