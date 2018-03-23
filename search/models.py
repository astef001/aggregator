# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class SearchPlace(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False, verbose_name="Id")
    name = models.CharField(max_length=100,
                            blank=False,
                            null=False,
                            unique=True)
    url = models.CharField(max_length=100,
                           blank=False,
                           null=False,
                           unique=True)
    product_tag = models.CharField(max_length=100,
                                   blank=False,
                                   null=False)
    product_attribute = models.CharField(max_length=100,
                                         blank=False,
                                         null=False)
    product_value = models.CharField(max_length=100,
                                     blank=False,
                                     null=False)
    image_tag = models.CharField(max_length=100,
                                 blank=False,
                                 null=False)
    image_attribute = models.CharField(max_length=100,
                                       blank=False,
                                       null=False)
    image_value = models.CharField(max_length=100,
                                   blank=False,
                                   null=False)
    link_tag = models.CharField(max_length=100,
                                blank=False,
                                null=False)
    link_attribute = models.CharField(max_length=100,
                                      blank=False,
                                      null=False)
    link_value = models.CharField(max_length=100,
                                  blank=False,
                                  null=False)
    price_tag = models.CharField(max_length=100,
                                 blank=False,
                                 null=False)
    price_attribute = models.CharField(max_length=100,
                                       blank=False,
                                       null=False)
    price_value = models.CharField(max_length=100,
                                   blank=False,
                                   null=False)
    price_decimal = models.IntegerField(blank=False,null=False)
    name_tag = models.CharField(max_length=100,
                                blank=False,
                                null=False)
    name_attribute = models.CharField(max_length=100,
                                      blank=False,
                                      null=False)
    name_value = models.CharField(max_length=100,
                                  blank=False,
                                  null=False)
    category_tag = models.CharField(max_length=100,
                                blank=False,
                                null=False)
    category_attribute = models.CharField(max_length=100,
                                      blank=False,
                                      null=False)
    category_value = models.CharField(max_length=100,
                                  blank=False,
                                  null=False)



class Category(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False)
    search_place = models.ForeignKey(SearchPlace)
    name = models.CharField(max_length=100,
                            blank=False,
                            null=False)
    link = models.CharField(max_length=100,
                            blank=True,
                            null=False)
