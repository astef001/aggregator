# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-09 20:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_auto_20180106_1541'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='searchplace',
            name='category_attribute',
            field=models.CharField(default='1', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='searchplace',
            name='category_tag',
            field=models.CharField(default='1', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='searchplace',
            name='category_value',
            field=models.CharField(default='1', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='search_place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search.SearchPlace'),
        ),
    ]
