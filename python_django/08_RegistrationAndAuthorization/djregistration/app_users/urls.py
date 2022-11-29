from django.urls import path
from app_users.views import login_view, logout_view, register_view, profile_view, verification_users_view
from django.urls import include


urlpatterns = [
    path('', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('reqister/', register_view, name='register'),
    path('profile/', profile_view, name='profile'),
    path('verification/', verification_users_view, name='verification')
]

