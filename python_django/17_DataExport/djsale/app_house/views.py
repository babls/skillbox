from app_house.models import House, News
from django.shortcuts import render
from django.views import generic


def about_view(request):
    return render(request, 'app_house/about.html')


def contacts_view(request):
    return render(request, 'app_house/сontacts.html')


def list_house_view(request):
    listHouse = House.objects.select_related('TypeHouse', 'CountRooms').all()
    return render(request, 'app_house/list_house.html', {
        'listHouse': listHouse,
    })


def news_view(request):
    # listNews = News.objects.select_related('House').all()
    # listNews = News.objects.select_related('House').all()
    # listNews2 = News.objects.all()[2]
    listNews3 = len(News.objects.all())
    # listNews4 = News.objects.filter(id=1)
    return render(request, 'app_house/news.html', {
        'listNews': listNews2, 'listNews2': listNews2, 'listNews3': listNews3, 'listNews4': listNews4
    })


class NewsItemDetailView(generic.DetailView):
    model = News
    template_name = 'app_house/newsitem_detail.html'
