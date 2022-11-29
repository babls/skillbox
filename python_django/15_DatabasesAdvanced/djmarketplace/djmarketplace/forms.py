from django import forms


class AddMoneyForm(forms.Form):
    add_money = forms.FloatField(label='На сколько пополнить баланс')
