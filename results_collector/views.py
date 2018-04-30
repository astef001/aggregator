# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import requests
from utils import update_dict, get_products
from search.models import SearchPlace
import json
from search.forms import SearchForm
from multiprocessing import Pool, cpu_count
import time

def get_products_from_url(url, location):
    response = requests.get(url,{'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0'})
    response = response.text
    response = get_products(response, location, location.name)
    product_dict={}
    update_dict(product_dict, response, location.name)
    return product_dict

def function_wrapper(tp):
    return get_products_from_url(*tp)


def get_data(request):
    search_string = request.POST.get('search_string')
    products={}
    threads=[]
    search_data = []
    search_on = request.POST.getlist('search_on')
    if not search_on:
        search_on = request.POST.getlist('search_on[]')
    locations = SearchPlace.objects.filter(id__in=search_on)
    start = time.time()
    for location in locations:
        url = "%s%s" % (location.url, search_string)
        search_data.append([url, location]) 
    num_cores = cpu_count()   
    pool = Pool(processes=num_cores)
    pool_outputs = pool.map(function_wrapper, search_data)
    
    for product in pool_outputs:
        if not products:
            products=product
        else:
            products.update(product)
    stop = time.time()
    print(stop-start)
    return render(request, 'results.html', {'data': products, 'form': SearchForm()})





