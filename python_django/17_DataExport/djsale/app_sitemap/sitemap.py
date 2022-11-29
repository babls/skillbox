from django.contrib.sitemaps import Sitemap
from app_house.models import News
from django.urls import reverse


class HouseSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return News.objects.filter(is_published=True).all()

    def lastmod(self, obj: News):
        return obj.published_at


class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'never'

    def items(self):
        return ['main', 'about', 'news', 'contacts']

    def location(self, item):
        return reverse(item)

