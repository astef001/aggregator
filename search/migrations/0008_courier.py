# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-10 14:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0007_searchplace_vendor_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courier',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('url', models.CharField(max_length=100)),
                ('result_tag', models.CharField(max_length=100)),
                ('result_attribute', models.CharField(max_length=100)),
                ('result_value', models.CharField(max_length=100)),
            ],
        ),
    ]