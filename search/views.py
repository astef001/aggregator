from forms import SearchForm, AddSearchPlaceForm
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render


class SearchView(FormView):
    template_name = "search.html"
    form_class = SearchForm

class AddSearchPlaceView(FormView):
    template_name = "add_search_place.html"
    form_class = AddSearchPlaceForm

class IndexView(TemplateView):
    template_name="index.html"
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update({'form': SearchForm()})
        return context

