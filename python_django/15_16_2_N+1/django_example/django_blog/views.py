from django.shortcuts import render
from django_blog.models import Post, Author, Blog
from django.db import connection
from django.db import reset_queries


def main_view(request):
    if request.method == 'GET':
        posts = Post.objects.select_related('blog').prefetch_related('author_post').all()
        return render(request, 'django_blog/main.html', {'posts': posts})

