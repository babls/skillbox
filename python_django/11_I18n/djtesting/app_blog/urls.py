from app_blog.views import NewPostBlog, list_post_view, InfoPost
from django.urls import path, include

urlpatterns = [
    path('', NewPostBlog.as_view(), name='new_post_blog'),
    path('infopost/<int:post_id>/', InfoPost.as_view(), name='infopost'),
    path('list_post/', list_post_view, name='list_post')
]
