from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class AuthForm(forms.Form):
    username = forms.CharField(label=_('Username'))
    password = forms.CharField(widget=forms.PasswordInput, label=_('Password'))


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, label='Имя')
    last_name = forms.CharField(max_length=30, required=False, label='Фамилия')
    email = forms.EmailField(max_length=30, required=False, label='Email')
    city = forms.CharField(max_length=36, required=False, label='Город')
    telephone_number = forms.CharField(max_length=13, required=False, label='Телефонный номер')
    about_myself = forms.CharField(max_length=300, required=False, label='О себе')

    class Meta:
        model = User
        fields = (
        'username', 'first_name', 'last_name', 'email', 'city', 'telephone_number', 'about_myself', 'password1',
        'password2')

