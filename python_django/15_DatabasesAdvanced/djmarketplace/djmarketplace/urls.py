"""djmarketplace URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from djmarketplace.views import index_view, money_view, addBasket_view, buyBasket_view, deleteBasket_view, report_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_users.urls'), name='main'),
    path('shops/', index_view, name='shops'),
    path('money/', money_view, name='money'),
    path('report/', report_view, name='report'),
    path('addBasket/<int:id_product>/', addBasket_view.as_view(), name='addBasket'),
    path('buyBasket/<int:id_history_shopping>/', buyBasket_view.as_view(), name='buyBasket'),
    path('deleteBasket/<int:id_history_shopping>/', deleteBasket_view.as_view(), name='deleteBasket'),
]
