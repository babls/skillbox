from os.path import commonpath

from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import News, Comment
from django.views import View
from .forms import NewsForm, CommentsForm
from django.urls import reverse
from django import forms

def index(request):
    news = News.objects.order_by('dataCreate')
    return render(request, 'app_news/index.html', {'title': 'Главная страница сайта', 'news': news})


def about(request):
    return render(request, 'app_news/about.html')


class NewsFormCreate(View):
    def get(self, request):
        news_form = NewsForm()
        return render(request, 'app_news/createNews.html', context={'news_form': news_form})

    def post(self, request):
        news_form = NewsForm(request.POST)

        if news_form.is_valid():
            News.objects.create(**news_form.cleaned_data)
            return HttpResponseRedirect(reverse('main'))
        return render(request, 'app_news/createNews.html', context={'news_form': news_form})


class NewsFormEdit(View):
    def get(self, request, news_id):
        news = News.objects.get(id=news_id)
        news_form = NewsForm(instance=news)
        return render(request, 'app_news/editNews.html', context={'news_form': news_form, 'news_id': news_id})

    def post(self, request, news_id):
        news = News.objects.get(id=news_id)
        news_form = NewsForm(request.POST, instance=news)

        if news_form.is_valid():
            news.save()
        return render(request, 'app_news/editNews.html', context={'news_form': news_form, 'news_id': news_id})


class InfoNewsAndComment(View):
    def get(self, request, news_id):
        news = News.objects.get(id=news_id)
        comments = Comment.objects.filter(id_news=news_id)
        return render(request, 'app_news/infonews.html', {'title': 'Новость и комментарии', 'news': news, 'comments': comments})


class CommentsFormCreate(View):
    def get(self, request, news_id):
        comments_form = CommentsForm(request.GET)
        if request.user.is_authenticated:
            comments_form.fields['nameUser'].widget = forms.HiddenInput()
            comments_form.fields['user'].widget = forms.HiddenInput()

            # Попытки убрать обязательные поля (работает, но валидацию не проходит если поле в БД обязательное xDDDD)
            #comments_form.fields['nameUser'].widget.attrs['required'] = False
            #comments_form.fields['nameUser'].required = False
            #comments_form.fields['user'].widget.attrs['required'] = False
            #comments_form.fields['user'].required = False
        else:
            comments_form.fields['user'].widget = forms.HiddenInput()
        return render(request, 'app_news/createComments.html',
                      context={'comments_form': comments_form, 'news_id': news_id})

    def post(self, request, news_id):
        comments_form = CommentsForm(request.POST)
        print("hello")

        if comments_form.is_valid():
            print("bingo valid")
            comment = comments_form.save(commit=False)
            comment.id_news = News.objects.get(id=news_id)

            if request.user.is_authenticated:
                print("bingo auth")
                comments_form.fields['nameUser'].widget = forms.HiddenInput()
                comments_form.fields['user'].widget = forms.HiddenInput()
                comment.user = request.user
            else:
                comment.nameUser += "(ANONYMOUS)"
            comment.save()
            return HttpResponseRedirect(reverse('main'))
        return render(request, 'app_news/createComments.html', context={'comments_form': comments_form, 'news_id': news_id})



