from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from app_profiles.forms import UserForm
from django.views import View
from django.shortcuts import render
from app_profiles.models import User

# Create your views here.

class UserFormView(View):

    def get(self, request):
        user_form = UserForm()
        return render(request, 'profiles/register.html', context={'user_form': user_form})
    
    def post(self, request):
        user_form = UserForm(request.POST)

        if user_form.is_valid(): # проверка на валидацию данных в форме
            # совершаем какую-либо бизнес логику
            # к примеру, сохранение в базу данных
            User.objects.create(**user_form.cleaned_data)
            return HttpResponseRedirect('')
        return render(request, 'profiles/register.html', context={'user_form': user_form})
