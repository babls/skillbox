from django.urls import path
from . import views
from .views import About,AdvertisementListView

urlpatterns = [
    #path('', views.advertisement_list, name='advertisement_list'),
    path('', views.Main.as_view()),
    path('advertisements/', views.ListAdvertisement.as_view()),
    path('advertisement_list/', AdvertisementListView.as_view(), name='advertisement'),
    path('random_advertisement/', views.RandomAdvertisement.as_view()),
    path('сontacts/', views.Contacts.as_view()),
    path('about/', views.About.as_view())
]
