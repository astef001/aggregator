# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-20 18:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0003_auto_20180209_2020'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='link',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]