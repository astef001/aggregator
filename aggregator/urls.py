"""aggregator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import RedirectView

import search.views

urlpatterns = [
    url(r'^results_collector/', include('results_collector.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^search/', search.views.SearchView.as_view(), name="search_view"),
    url(r'^add_search_place/', search.views.add_search_place),
    #url(r'^.*$', RedirectView.as_view(url='search/', permanent=False), name='index')
]
