# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class SearchPlace(models.Model):
    """This Model is meant to store all search places needed data for searching through them"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,
                            blank=False,
                            null=False,
                            unique=True)
    url = models.CharField(max_length=100,
                           blank=False,
                           null=False,
                           unique=True)
    vendor_logo = models.CharField(max_length=100,
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
    """This model is meant to store data for categories extracted from search places"""
    id = models.AutoField(primary_key=True)
    search_place = models.ForeignKey(SearchPlace)
    name = models.CharField(max_length=100,
                            blank=False,
                            null=False)
    link = models.CharField(max_length=100,
                            blank=True,
                            null=False)


class Courier(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.CharField(max_length=100,
                           blank=False,
                           null=False)
    result_tag = models.CharField(max_length=100,
                                  blank=False,
                                  null=False)
    result_attribute = models.CharField(max_length=100,
                                        blank=True,
                                        null=True)
    result_value = models.CharField(max_length=100,
                                    blank=True,
                                    null=True)
    is_json = models.BooleanField(default=False)


class CourierParams(models.Model):
    id = models.AutoField(primary_key=True)
    courier_id = models.ForeignKey(Courier)
    param_label = models.CharField(max_length=100,
                                   blank=False,
                                   null=False)
    param_value = models.CharField(max_length=100,
                                   blank=True,
                                   null=True)

    class Meta:
        unique_together = ("courier_id", "param_label")
