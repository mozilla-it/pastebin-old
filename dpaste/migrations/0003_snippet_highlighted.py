# -*- coding: utf-8 -*-
# Generated by Django 1.11a1 on 2017-01-21 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpaste', '0002_auto_20170119_1038'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='highlighted',
            field=models.TextField(default='', verbose_name='Highlighted Content'),
            preserve_default=False,
        ),
    ]
