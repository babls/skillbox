from django.contrib import admin
from django.urls import path, include
from app_library.views import BookList,AuthorList, BookDetail, AuthorDetail

urlpatterns = [
    path('books_list/', BookList.as_view(), name='books_list'),
    path('authors_list/', AuthorList.as_view(), name='authors_list'),
    path('books_list/<int:pk>/', BookDetail.as_view(), name='books_detail'),
    path('authors_list/<int:pk>/', AuthorDetail.as_view(), name='authors_detail'),
]