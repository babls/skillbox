from app_sitemap.sitemap import HouseSitemap, StaticViewSitemap
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include

sitemaps = {
    'news': HouseSitemap,
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_house.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('rss/', include('app_rss.urls')),
]
