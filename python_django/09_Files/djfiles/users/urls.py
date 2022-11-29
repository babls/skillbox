from django.urls import path
from users.views import index, login_view, logout_view, register_view, profile_view, EditProfileForm
from django.urls import include


urlpatterns = [
    path('', index, name='main'),
    path('logout/', logout_view, name='logout'),
    path('reqister/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('profile/', profile_view, name='profile'),
    path('edit_profile/<int:user_id>/', EditProfileForm.as_view(), name='edit_profile')
]
