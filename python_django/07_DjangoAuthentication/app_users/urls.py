from django.urls import path
from app_users.views import login_view, logout_view
from django.urls import include

urlpatterns = [
    path('', login_view, name='login'),
    path('logout', logout_view, name='logout'),
]

