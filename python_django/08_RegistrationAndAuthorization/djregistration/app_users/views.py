from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from app_users.forms import AuthForm, RegisterForm
from django.urls import reverse
from app_users.models import Profile
from app_news.models import News, Comment
from django.contrib.auth.models import User


def login_view(request):
    if request.method == 'POST':    # для POST пытаемся аутентифицировать пользователя
        auth_form = AuthForm(request.POST)
        if auth_form.is_valid():
            username = auth_form.cleaned_data['username']
            password = auth_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    if user.is_superuser:
                        #return HttpResponse('Добро пожаловать, администратор!')
                        return HttpResponseRedirect(reverse('main'))
                    else:
                        #return HttpResponse('Вы успешно вошли в систему')
                        return HttpResponseRedirect(reverse('main'))
                else:
                    auth_form.add_error('__all__', 'Ошибка! Учетная запись пользователя не активна!')
            else:
                auth_form.add_error('__all__', 'Ошибка! Проверьте правильность написания логина и пароля!')

    else:   # для всех остальных запросов просто отображаем саму страничку логина
        auth_form = AuthForm()
    context = {
        'form': auth_form
    }
    return render(request, 'app_users/login.html', context=context)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('main'))


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            date_of_birth = form.cleaned_data.get('date_of_birth')
            city = form.cleaned_data.get('city')
            telephone_number = form.cleaned_data.get('telephone_number')

            Profile.objects.create(
                user=user,
                city=city,
                date_of_birth=date_of_birth,
                telephone_number=telephone_number,
                verification='S',
                published_news_count=0,
                Group_user='N'
            )
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect(reverse('main'))
    else:
        form = RegisterForm()
    return render(request, 'app_users/register.html', {'form': form})


def profile_view(request):
    if request.method == 'GET':
        return render(request, 'app_users/profile.html')

    if request.method == 'POST':
        profile_user = Profile.objects.get(id=request.POST.get('ver_request'))
        profile_user.verification = 'R'
        profile_user.save()
        return HttpResponseRedirect(reverse('profile'))


def verification_users_view(request):
        if request.method == 'GET':
            users_ver_list = Profile.objects.filter(verification='R')
            return render(request, 'app_users/verification_users.html', {'users_ver_list': users_ver_list})

        if request.method == 'POST':
            arr_users = request.POST.getlist('ver_users')
            for user_ver in arr_users:
                profile_user = Profile.objects.get(id=user_ver)
                profile_user.verification = 'V'
                profile_user.Group_user = 'V'
                profile_user.save()

            return HttpResponseRedirect(reverse('main'))

