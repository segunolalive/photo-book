# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-12 20:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_auto_20160812_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_group',
            field=models.CharField(max_length=120),
        ),
        migrations.DeleteModel(
            name='AlbumGroup',
        ),
    ]