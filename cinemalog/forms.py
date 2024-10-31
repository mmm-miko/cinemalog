from django import forms
from .models import WatchList

class WatchListForm(forms.ModelForm):
    class Meta:
        model = WatchList
        fields = ['image', 'title','comment']
