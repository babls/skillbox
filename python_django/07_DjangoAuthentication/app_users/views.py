from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from app_users.forms import AuthForm
from django.urls import reverse

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

