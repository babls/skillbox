from app_store.views import main_view, shops_view, index_view
from django.urls import path

urlpatterns = [
    path('', main_view, name='main'),
    path('shops/', shops_view, name='shops'),
    path('index', index_view, name='index')
]
