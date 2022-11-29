from app_house.views import about_view, list_house_view, news_view, contacts_view, NewsItemDetailView
from django.urls import path

urlpatterns = [
    path('about/', about_view, name='about'),
    path('', list_house_view, name='main'),
    path('news/', news_view, name='news'),
    path('contacts/', contacts_view, name='contacts'),
    path('news/<int:pk>/', NewsItemDetailView.as_view(), name='news-item')
]
