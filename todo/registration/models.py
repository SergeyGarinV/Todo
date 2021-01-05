from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import forms
from django.core.exceptions import ValidationError


class CustomsUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)
        error_messages = {
            'username': {
                'unique': "Имя уже сушествует"
            },
            'password2': {
                'password_mismatch': ("Парали не совпадают", )
            }
        }


class LoginForm(forms.Form):
    login = forms.CharField(
        required=True,
        max_length=64,
        widget=forms.TextInput(attrs={'id': 'input_feild_email-id'})
    )
    password = forms.CharField(
        required=True,
        max_length=64,
        widget=forms.PasswordInput()
    )

    class Meta:
        error_messages = {
            'login': {
                'user_not_found': "Пользователя не существует"
            },
            'password': {
                'password_mismatch': "Не верный пароль",
            },
        }

    def clean_login(self):
        login = self.cleaned_data.get('login')
        if not User.objects.filter(username=login).exists():
            raise ValidationError(
                self.Meta.error_messages['login']['user_not_found'],
                code='user_not_found',
            )
        return login
