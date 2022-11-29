from app_users.views import login_view, lk_view, logout_view, register_view, history_shopping_view
from django.urls import path
from djmarketplace.views import index_view

urlpatterns = [
    path('', index_view, name='main'),
    path('login', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('lk/', lk_view, name='lk'),
    path('lk/history_shopping/', history_shopping_view, name='history_shopping'),
    path('register/', register_view, name='register')
]
