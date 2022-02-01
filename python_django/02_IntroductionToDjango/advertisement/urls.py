from django.urls import path
from django.urls import path
from .import views

urlpatterns = [
    path("",views.advertisement_list, name='advertisement_list'),
    path("course1/",views.course1, name='course1'),
    path("course2/",views.course2, name='course2'),
    path("course3/",views.course3, name='course3'),
    path("course4/",views.course4, name='course4'),
    path("course5/",views.course5, name='course5')
]
