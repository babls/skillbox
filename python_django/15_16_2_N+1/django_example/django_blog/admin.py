from django.contrib import admin
from django_blog.models import Blog, Post, Author


class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'is_publihed']


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']


admin.site.register(Post, PostAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Author, AuthorAdmin)
