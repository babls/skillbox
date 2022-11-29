from os.path import commonpath

from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import News, Comment
from app_users.models import Profile
from django.views import View
from .forms import NewsForm, CommentsForm
from django.urls import reverse
from django import forms
from django.contrib.auth.models import User


def index(request):
    news = News.objects.filter(tag=request.GET.get('tag'))
    tags = News.objects.values('tag').distinct().filter(activity=True)
    #print(tags.value)
    #news = News.objects.order_by('dataCreate') 'tags': ['Новость', 'Хуевость']

    return render(request, 'app_news/index.html', {
        'title': 'Главная страница сайта',
        'news': news,
        'tags': tags
    })


def about(request):
    return render(request, 'app_news/about.html')


class NewsFormCreate(View):
    def get(self, request):
        news_form = NewsForm()
        if request.user.is_authenticated:
            news_form.fields['author'].widget = forms.HiddenInput()
            news_form.fields['moderate'].widget = forms.HiddenInput()
            news_form.fields['activity'].widget = forms.HiddenInput()
            news_form.fields['dateEdit'].widget = forms.HiddenInput()
        return render(request, 'app_news/createNews.html', context={'news_form': news_form})

    def post(self, request):
        news_form = NewsForm(request.POST)

        if news_form.is_valid():
            if request.user.is_authenticated:
                news_form.moderate = 'R'
                news_form.activity = 'False'
                user = Profile.objects.get(user=request.user)
                news_form.author = request.user
                New = news_form.save(commit=False)
                New.author = User.objects.get(id=request.user.id)
                New.save()
                if user.published_news_count is not None:
                    user.published_news_count += 1
                else:
                    user.published_news_count = 1
                user.save()
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

        if comments_form.is_valid():
            comment = comments_form.save(commit=False)
            comment.id_news = News.objects.get(id=news_id)

            if request.user.is_authenticated:
                comments_form.fields['nameUser'].widget = forms.HiddenInput()
                comments_form.fields['user'].widget = forms.HiddenInput()
                comment.user = request.user
            else:
                comment.nameUser += "(ANONYMOUS)"
            comment.save()
            return HttpResponseRedirect(reverse('main'))
        return render(request, 'app_news/createComments.html', context={'comments_form': comments_form, 'news_id': news_id})


class NewsModeration(View):
    def get(self, request):
        news_list_moderation = News.objects.filter(moderate='R')
        return render(request, 'app_news/newsModeration.html', {'news_list_moderation': news_list_moderation})

    def post(self, request):
        new_success = request.POST.getlist('new_success')
        for new in new_success:
            new_base = News.objects.get(id=new)
            new_base.moderate = 'V'
            new_base.activity = 'True'
            new_base.save()

        return HttpResponseRedirect(reverse('main'))



