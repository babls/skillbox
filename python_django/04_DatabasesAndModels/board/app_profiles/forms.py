from django import forms
import datetime
from django.core.exceptions import ValidationError

class UserForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    first_name = forms.CharField()
    second_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    birthday = forms.DateField()
    
    def clean_birthday(self):
        data = self.cleaned_data['birthday']
        today = datetime.date.today()
        year_delta = (today - data).days / 365
        if year_delta < 18:
            raise ValidationError('Регистрироваться могут только лица старше 18 лет')
        return data

class AdvertisementForm(forms.Form):
    title = forms.CharField(min_length=3)
    description = forms.CharField(min_length=10)
    price = forms.FloatField(min_value=10,max_value=100000)