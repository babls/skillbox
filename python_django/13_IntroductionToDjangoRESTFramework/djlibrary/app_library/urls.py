from django.contrib import admin
from django.urls import path, include
from app_library.views import BookList,AuthorList

urlpatterns = [
    path('books_list/', BookList.as_view(), name='books_list'),
    path('authors_list/', AuthorList.as_view(), name='authors_list'),
]