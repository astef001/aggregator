from django import forms
from search.models import SearchPlace
from djng.forms import fields
from djng.styling.bootstrap3.forms import Bootstrap3Form, Bootstrap3ModelForm


class SearchForm(Bootstrap3Form):
    """This object is representing a form used for searchng through searchplaces"""
    search_places = SearchPlace.objects.values('id', 'name')
    search_string = fields.CharField(label="Search", max_length=100)
    search_on = fields.MultipleChoiceField(choices=[])

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields['search_on'] = fields.MultipleChoiceField(
            label="Search On",
            widget=forms.CheckboxSelectMultiple,
            choices=[(place.id, place.name) for place in SearchPlace.objects.all()])


class AddSearchPlaceForm(Bootstrap3ModelForm):
    """This form object is meant to build a form for adding search places"""
    def __init__(self, *args, **kwargs):
        super(AddSearchPlaceForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
        })

    class Meta:
        model = SearchPlace
        exclude = ['id']


class SearchAWBForm(Bootstrap3Form):
    """This form object is meant to build a form for adding search packages by awb"""
    awb = fields.CharField(label="AWB", max_length=100)

    