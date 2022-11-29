from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class AuthForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, label='Имя')
    last_name = forms.CharField(max_length=30, required=False, label='Фамилия')

    class Meta:
        model = User
        fields = (
        'username', 'first_name', 'last_name', 'password1',
        'password2')