from django import forms
from app_blog.models import BlogPost
from django.utils.translation import gettext_lazy as _


class UploadFileForm(forms.ModelForm):
    # title = forms.CharField(max_length=50, label='Заголовок')
    # description = forms.CharField(max_length=100, label='Текст')
    image = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), label=_('File upload'))

    class Meta:
        model = BlogPost
        fields = '__all__'


class UploadFilePostListForm(forms.Form):
    file = forms.FileField(label=_('Upload a csv file with a list of posts'))
