from django.db import models
from django.shortcuts import render
from advertisements_app.models import Advertisement,Autor
from django.views import generic

class AdvertisementListView(generic.ListView):
    model = Advertisement,Autor
    template_name = 'advertisements_list.html'
    context_object_name = 'advertisement_list'
    queryset = Advertisement.objects.all()

class AdvertisementDetailView(generic.DetailView):
    model = Advertisement
