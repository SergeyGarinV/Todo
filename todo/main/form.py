from django.contrib.auth.forms import forms
from main.models import ListModel


class ListForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput())

    class Meta:
        model = ListModel
        fields = ('name', 'user')
