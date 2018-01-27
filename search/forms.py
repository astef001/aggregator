from django import forms
from search.models import SearchPlace


class SearchForm(forms.Form):
    search_places = SearchPlace.objects.values('id', 'name')
    OPTIONS = [(x.get('id'), x.get('name')) for x in search_places]
    search_string = forms.CharField(label="Search", max_length=100)
    search_on = forms.MultipleChoiceField(label="Search On",
                                          choices=OPTIONS,
                                          widget=forms.CheckboxSelectMultiple)


class AddSearchPlaceForm(forms.ModelForm):
    class Meta:
        model = SearchPlace
        exclude = ['id']
