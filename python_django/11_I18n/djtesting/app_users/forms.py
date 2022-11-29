from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class AuthForm(forms.Form):
    username = forms.CharField(label=_('username'))
    password = forms.CharField(widget=forms.PasswordInput, label=_('password'))


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, label=_('name'))
    last_name = forms.CharField(max_length=30, required=False, label=_('surname'))
    email = forms.EmailField(max_length=30, required=False, label=_('email'))
    city = forms.CharField(max_length=36, required=False, label=_('sity'))
    date_of_birth = forms.DateField(required=True,
                                    label=_(
                                        'date of birth in the format YYYY-MM-DD (Four-digit year, separator, two-digit month, separator, two-digit day (example: 2002-02-02))'))
    telephone_number = forms.CharField(max_length=13, required=False, label=_('telephone number'))
    about_myself = forms.CharField(max_length=300, required=False, label=_('about myself'))

    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name', 'email', 'city', 'telephone_number', 'about_myself', 'password1',
            'password2')


class EditForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=False, label=_('name'))
    last_name = forms.CharField(max_length=30, required=False, label=_('surname'))
    email = forms.EmailField(max_length=30, required=False, label=_('email'))
    city = forms.CharField(max_length=36, required=False, label=_('sity'))
    date_of_birth = forms.DateField(required=True, label=_('date of birth'))
    telephone_number = forms.CharField(max_length=13, required=False, label=_('telephone number'))
    about_myself = forms.CharField(max_length=300, required=False, label=_('about myself'))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'city', 'telephone_number', 'about_myself')


class RestorePasswordForm(forms.Form):
    email = forms.EmailField(label=_('Enter your email'))
