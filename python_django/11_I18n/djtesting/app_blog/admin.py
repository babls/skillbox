from django.contrib import admin
from .models import BlogPost, FilesPost


class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'dataCreate', 'dateEdit', 'activity']
    list_filter = ['activity']
    actions = ['news_as_activity', 'news_as_not_activity']

    def news_as_activity(self, request, queryset):
        queryset.update(activity=True)

    def news_as_not_activity(self, request, queryset):
        queryset.update(activity=False)

    news_as_activity.short_description = 'Перевести новость в статус Активно'
    news_as_not_activity.short_description = 'Перевести новость в статус Не активно'


class FileAdmin(admin.ModelAdmin):
    list_display = ('id', 'file', 'post_id')


admin.site.register(BlogPost, BlogAdmin)
admin.site.register(FilesPost, FileAdmin)
