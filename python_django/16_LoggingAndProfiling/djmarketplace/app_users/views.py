from app_users.forms import AuthForm, RegisterForm
from app_users.models import Profile, History_shopping
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import logging


logger = logging.getLogger(__name__)
# from django.views.decorators.cache import cache_page

# @cache_page(30)  Кеширование представлений (страниц)

def lk_view(request):
    # try:
    #     profile = Profile.objects.get(user=request.user)
    # except Exception:
    #     Profile.objects.create(
    #         user=request.user,
    #         balance=0,
    #         status='Н'
    #     )
    #     profile = Profile.objects.get(user=request.user)

    profile, created = Profile.objects.get_or_create(
        user=request.user,
        defaults={'user': request.user,
                  'balance': 0,
                  'balanceShopping': 0,
                  'status': 'Н'}
    )

    return render(request, 'app_users/lk.html', {
        'profile': profile,
    })


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
                        logger.info('Администратор вошел ' + username)
                        return HttpResponseRedirect(reverse('main'))
                    else:
                        # return HttpResponse('Вы успешно вошли в систему')
                        logger.info('Пользователь вошел ' + username)
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


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()

            Profile.objects.create(
                user=user,
                balance=0,
                status='Н'
            )
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            logger.info('Новый пользователь зарегистрирован ' + username)
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect(reverse('main'))
    else:
        form = RegisterForm()
    return render(request, 'app_users/register.html', {'form': form})


def history_shopping_view(request):
    history_shopping = History_shopping.objects.select_related('shop', 'product').filter(user=request.user).order_by('-id')

    return render(request, 'app_users/history_shopping.html', {
        'history_shopping': history_shopping,
    })
