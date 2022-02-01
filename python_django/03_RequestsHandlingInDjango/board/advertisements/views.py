from django.db import models
from django.shortcuts import render
from django.views import View

from django.http import HttpResponse
from django.views import generic
from django.views.generic import TemplateView
from collections import defaultdict
from rest_framework.authentication import SessionAuthentication
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from advertisements.models import Advertisement
import random

class CsrfExemptSessionAuthentication(SessionAuthentication):        

    def enforce_csrf(self, request):        

        return None

# Class Based Views
@method_decorator(csrf_exempt, name='dispatch')
class ListAdvertisement(View):
    count = 0
    Alist = Advertisement.objects.all()   
    def get(self, request):    
        #ip = request.META.get('REMOTE_ADDR')
        #count_request = 1
        #count_request[ip] +=1
        #count = count_request[ip]
        ListAdvertisement.count +=1
        
        return render(request, 'advertisements/advertisement_list.html', {'advertisements': ListAdvertisement.Alist,'count': ListAdvertisement.count})
    
    def post(self, request):
            return HttpResponse('/Cоздание новой записи успешно выполнено/')

    def method_decorator(post):   #Декоратор функции post
        authentication_classes = (CsrfExemptSessionAuthentication,)
    
class Main(View):
    title = 'Главная страница'

    def get(self, request):
        categories = [
        'личные вещи',
        'транспорт',
        'хобби ',
        'отдых',
        'гараж'
    ]

        regions = [
        'Москва',
        'Московская область',
        'республика Алтай',
        'Вологодская область',
        'Пермь'
        ]
        
        return render(request, 'advertisements/main.html', {'categories': categories,
                                                                      'regions': regions,'title': Main.title})

# TemplateView

class RandomAdvertisement(TemplateView):
    template_name = 'advertisements/random_advertisement.html'
    Alist = Advertisement.objects.all()

    def get_context_data(self, **kwargs):
        random_item = random.choice(RandomAdvertisement.Alist)
        contex = super().get_context_data(**kwargs)
        contex['title'] = random_item.title
        contex['price'] = random_item.price
        contex['created_at'] = random_item.created_at
        contex['views_count'] = random_item.views_count
        return contex

class About(TemplateView):
    template_name = 'advertisements/about.html'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['title'] = 'О компании'
        contex['name'] = 'О компании'
        contex['about_company'] = 'Продам гараж'
        contex['description_company'] = 'Продам гараж, недорого :3'
        return contex

class Contacts(TemplateView):
    template_name = 'advertisements/contacts.html'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['title'] = 'Контакты'
        contex['name'] = 'Контакты'
        contex['telephone_number'] = '8-999-126-76-34'
        contex['email'] = 'daniil_sa@pspu.ru'
        return contex

class AdvertisementListView(generic.ListView):
    model = Advertisement
    template_name = 'advertisement_listview.html'
    context_object_name = 'advertisement_listview'
    queryset = Advertisement.objects.all()[:5]