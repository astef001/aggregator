from forms import SearchForm, AddSearchPlaceForm
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from search.models import SearchPlace
from django.http import HttpResponseRedirect


class SearchView(FormView):
    template_name = "search.html"
    form_class = SearchForm

class AddSearchPlaceView(FormView):
    template_name = "add_search_place.html"
    form_class = AddSearchPlaceForm

    def post(self, request):
        params = dict(request.POST.iterlists())
        params.pop('csrfmiddlewaretoken', None)
        for param in params:
            params[param] = params[param].pop(0)
        SearchPlace.objects.create(**params)
        return HttpResponseRedirect('/')



class IndexView(TemplateView):
    template_name="index.html"
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update({'form': SearchForm()})
        return context

