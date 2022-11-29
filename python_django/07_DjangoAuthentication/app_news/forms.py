from app_news.models import News, Comment
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
            'user',
            'text'
        ]

        # Попытки убрать обязательные поля (работает, но валидацию не проходит если поле в БД обязательное xDDDD)
        #user = forms.CharField(required=False)
        #nameUser = forms.CharField(required=False)
        #widgets = {'nameUser': forms.HiddenInput()}
