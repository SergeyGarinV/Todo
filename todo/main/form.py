from django.contrib.auth.forms import forms
from django.core.exceptions import NON_FIELD_ERRORS

from main.models import ListModel


class ListForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput())

    class Meta:
        model = ListModel
        fields = ('name', 'user')
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "Список уже создан",
            }
        }

