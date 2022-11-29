from app_store.models import History_shopping, Profile
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import AuthForm
from .forms import RegisterForm


def login_view(request):
    if request.method == 'POST':  # для POST пытаемся аутентифицировать пользователя
        auth_form = AuthForm(request.POST)
        if auth_form.is_valid():
            username = auth_form.cleaned_data['username']
            password = auth_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    if user.is_superuser:
                        # return HttpResponse('Добро пожаловать, администратор!')
                        return HttpResponseRedirect(reverse('main'))
                    else:
                        # return HttpResponse('Вы успешно вошли в систему')
                        return HttpResponseRedirect(reverse('main'))
                else:
                    auth_form.add_error('__all__', 'Ошибка! Учетная запись пользователя не активна!')
            else:
                auth_form.add_error('__all__', 'Ошибка! Проверьте правильность написания логина и пароля!')

    else:  # для всех остальных запросов просто отображаем саму страничку логина
        auth_form = AuthForm()
    context = {
        'form': auth_form
    }
    return render(request, 'app_users/login.html', context=context)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('main'))


def profile_view(request):
    user_balans_update = 0
    if request.user is 'AnonymousUser':
        print(request.user)
        user = Profile.objects.get(user=request.user)
        user_balans = History_shopping.objects.filter(user=request.user)
        for u_balans in user_balans:
            user_balans_update += u_balans.total
        user.balance = user_balans_update
        user.save()

    if request.method == 'GET':
        return render(request, 'app_users/profile.html')


def history_shopping_view(request):
    history = History_shopping.objects.filter(user=request.user)

    if request.method == 'GET':
        return render(request, 'app_users/history_shopping.html', {
            'history': history,
        })


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            date_of_birth = form.cleaned_data.get('date_of_birth')
            city = form.cleaned_data.get('city')
            about_myself = form.cleaned_data.get('about_myself')
            telephone_number = form.cleaned_data.get('telephone_number')

            Profile.objects.create(
                user=user,
                city=city,
                telephone_number=telephone_number,
                about_myself=about_myself,
                balance=0
            )
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect(reverse('main'))
    else:
        form = RegisterForm()
    return render(request, 'app_users/register.html', {'form': form})
