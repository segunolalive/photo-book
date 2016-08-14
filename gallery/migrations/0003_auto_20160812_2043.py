# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-12 19:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20160812_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_group',
            field=models.ForeignKey(default='unnamed', on_delete=django.db.models.deletion.CASCADE, to='gallery.AlbumGroup'),
        ),
        migrations.AlterField(
            model_name='albumgroup',
            name='name',
            field=models.CharField(max_length=120),
        ),
    ]