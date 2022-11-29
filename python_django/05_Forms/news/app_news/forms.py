from .models import News, Comment
from django import forms


class NewsForm(forms.ModelForm):
    class Meta:
        model = News    #С какой моделью работаем
        fields = '__all__'     #Какие поля присутствуют в форме


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'nameUser',
            'text'
        ]
