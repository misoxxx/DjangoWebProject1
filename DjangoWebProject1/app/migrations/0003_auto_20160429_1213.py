# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-29 10:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20160429_1135'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shopitem',
            old_name='picture',
            new_name='imgurl',
        ),
        migrations.RemoveField(
            model_name='shopitem',
            name='manufacturer',
        ),
    ]