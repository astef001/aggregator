# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import requests
from utils import update_dict, get_products
from search.models import SearchPlace


def get_data(request):
    search_string = request.POST.get('search_string')
    products = {}
    locations = SearchPlace.objects.filter(id__in=request.POST.get('search_on'))
    for location in locations:
        url = "%s%s" % (location.url, search_string)
        response = requests.get(url,{'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0'})
        response = response.text
        response = get_products(response, location, location.name)
        if not products:
            products = response
        else:
            products = update_dict(products, response, location.name)
    return render(request, 'results.html', {'data': products})





