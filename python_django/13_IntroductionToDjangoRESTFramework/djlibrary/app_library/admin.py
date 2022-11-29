from django.contrib import admin

from .models import Author, Book


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'surname', 'date_of_birth']
    list_filter = ['name']


class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'isbn', 'year_of_issue', 'page_count']
    list_filter = ['name']


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
