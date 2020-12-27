from django.contrib.auth.forms import forms
from todo_item.models import ItemModel
from django.core.exceptions import NON_FIELD_ERRORS


class ItemForm(forms.ModelForm):
    """
    Форма добавления элементов списка дел
    """
    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Название дела",
    }))
    expr_date = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Дата завершения",
        'type': "date"
    }))

    class Meta:
        model = ItemModel
        fields = ('name', 'expr_date', 'listmodules')
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "Дело уже созданно",
            }
        }
