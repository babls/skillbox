from django.contrib import admin
from django.urls import path
from django_blog.views import main_view

urlpatterns = [
    path('', main_view, name='main'),
]