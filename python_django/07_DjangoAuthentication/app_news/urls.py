from django.urls import path
from app_news import views
from app_news.views import NewsFormCreate, NewsFormEdit, InfoNewsAndComment, CommentsFormCreate

urlpatterns = [
    path('', views.index, name='main'),
    path('about/', views.about, name='about'),
    path('create_news/', NewsFormCreate.as_view(), name='createNews'),
    path('<int:news_id>/create_comment/', CommentsFormCreate.as_view(), name='createComment'),
    path('<int:news_id>/edit/', NewsFormEdit.as_view(), name='create'),
    path('<int:news_id>/infonews/', InfoNewsAndComment.as_view(), name='infonews'),
]
