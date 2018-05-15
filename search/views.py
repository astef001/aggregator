from forms import SearchForm, AddSearchPlaceForm, SearchAWBForm
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from search.models import SearchPlace, Category
from django.http import HttpResponseRedirect
from django.shortcuts import render
from search.utils import get_package_status

class SearchView(FormView):
    """This view is meant to build the search form"""
    template_name = "search.html"
    form_class = SearchForm


class AddSearchPlaceView(TemplateView):
    """This view is meant to build the add_search_place form"""
    template_name = "add_search_place.html"

    def get_context_data(self, **kwargs):
        """This method is meant to get context data for rendering the add search place form"""
        context = super(TemplateView, self).get_context_data(**kwargs)
        context.update({'form': SearchForm,
                        'add_form': AddSearchPlaceForm})
        return context

    def post(self, request):
        """This method is meant to handle the post request for current form
            :param request - request object sent by the client
            :returns redirect to Index view if successful
        """
        params = dict(request.POST.iterlists())
        params.pop('csrfmiddlewaretoken', None)
        for param in params:
            params[param] = params[param].pop(0)
        SearchPlace.objects.create(**params)
        return HttpResponseRedirect('/')


class IndexView(TemplateView):
    """This view is the index view containing the list of site categories"""
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        """This method is meant to get context data for rendering the index view"""
        context = super(IndexView, self).get_context_data(**kwargs)
        categories = Category.objects.all()
        context.update({"categories": categories, "form":SearchForm})
        return context

class SearchAWB(FormView):
    template_name = "search_awb.html"
    form_class = SearchAWBForm

    def post(self, request):
        params = dict(request.POST.iterlists())
        params = params.pop("awb")[0]
        return render(request, 'search_awb.html', {"form":SearchAWBForm(), "result": get_package_status(params)})

