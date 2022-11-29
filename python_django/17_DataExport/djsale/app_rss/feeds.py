from app_house.models import News
from django.contrib.syndication.views import Feed
from django.db.models import QuerySet
from django.urls import reverse


class LatestNewsFeed(Feed):
    title = "Новости"
    link = "/news/"
    description = "Самые свежие новости."

    def items(self) -> QuerySet:
        return News.objects.order_by('-published_at')[:5]

    def item_title(self, item: News) -> str:
        return item.Name

    def item_description(self, item: News) -> str:
        return item.description

    def item_link(self, item: News) -> str:
        return reverse('news-item', args=[item.pk])
