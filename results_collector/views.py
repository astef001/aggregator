# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import requests
from .settings import WHERE_TO_SEARCH, DATA_MAP
from utils import update_dict, get_products
import json


def get_data(request):
    search_string = request.GET.get('search_string')
    products = {}
    for location in WHERE_TO_SEARCH:
        url = "%s%s" % (location.get('url'), search_string)
        response = requests.get(url,{'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0'})
        response = response.text
        response = get_products(response, DATA_MAP[location.get('name')], location.get('name'))
        if not products:
            products = response
        else:
            products = update_dict(products, response, location.get('name'))
    return render(request, 'results.html', {'data': products})





