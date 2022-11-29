from app_users.views import login_view, logout_view, profile_view, history_shopping_view, register_view
from django.urls import path, include

urlpatterns = [
    path('login', login_view, name='login'),
    path('reqister/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('history_shopping/', history_shopping_view, name='history_shopping'),
    path('', include('app_store.urls'), name='main'),
]
