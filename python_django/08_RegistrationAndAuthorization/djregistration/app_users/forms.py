from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, label='Имя')
    last_name = forms.CharField(max_length=30, required=False, label='Фамилия')
    email = forms.EmailField(max_length=30, required=False, label='Email')
    city = forms.CharField(max_length=36, required=False, label='Город')
    date_of_birth = forms.DateField(required=True, label='Дата рождения в формате YYYY-MM-DD (Four-digit year, separator, two-digit month, separator, two-digit day (example: 2002-02-02))')
    telephone_number = forms.CharField(max_length=13, required=False, label='Телефонный номер')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'city', 'telephone_number', 'password1', 'password2')
