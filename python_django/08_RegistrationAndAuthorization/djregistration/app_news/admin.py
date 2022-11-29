from django.contrib import admin
from .models import News, Comment


class CommentInLine(admin.TabularInline):
    model = Comment


class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'dataCreate', 'dateEdit', 'activity']
    list_filter = ['activity']
    inlines = [CommentInLine]
    actions = ['news_as_activity', 'news_as_not_activity']

    def news_as_activity(self, request, queryset):
        queryset.update(activity=True)

    def news_as_not_activity(self, request, queryset):
        queryset.update(activity=False)

    news_as_activity.short_description = 'Перевести новость в статус Активно'
    news_as_not_activity.short_description = 'Перевести новость в статус Не активно'


class CommentsAdmin(admin.ModelAdmin):
    list_display = ['user', 'nameUser', 'text', 'id_news']
    search_fields = ['user', 'nameUser']
    actions = ['comment_as_delete']

    def comment_as_delete(self, request, queryset):
        queryset.update(text="Удалено администратором")

    comment_as_delete.short_description = 'Заблокировать комментарий'


admin.site.register(News, NewsAdmin)
admin.site.register(Comment, CommentsAdmin)
