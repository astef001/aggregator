from django import forms
from search.models import SearchPlace
from djng.forms import fields
from djng.styling.bootstrap3.forms import Bootstrap3Form


class SearchForm(Bootstrap3Form):
    search_places = SearchPlace.objects.values('id', 'name')
    OPTIONS = [(x.get('id'), x.get('name')) for x in search_places]
    search_string = fields.CharField(label="Search", max_length=100)
    search_on = fields.MultipleChoiceField(label="Search On",
                                          choices=OPTIONS,
                                          widget=forms.CheckboxSelectMultiple)


class AddSearchPlaceForm(Bootstrap3Form):
    class Meta:
        model = SearchPlace
        exclude = ['id']
