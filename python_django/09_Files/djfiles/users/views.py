from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import AuthForm, RegisterForm, EditForm
from django.views import View
from app_blog.models import BlogPost
import datetime


def index(request):
    blog_post = BlogPost.objects.order_by('dataCreate')
    return render(request, 'users/index.html', {
        'title': 'Главная страница',
        'blog': blog_post
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
    return render(request, 'users/login.html', context=context)


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
            about_myself = form.cleaned_data.get('about_myself')
            telephone_number = form.cleaned_data.get('telephone_number')

            Profile.objects.create(
                user=user,
                city=city,
                date_of_birth=date_of_birth,
                telephone_number=telephone_number,
                about_myself=about_myself
            )
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect(reverse('main'))
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})


def profile_view(request):
    if request.method == 'GET':
        return render(request, 'users/profile.html')

    if request.method == 'POST':
        user = request.POST.get('user_id')
        return HttpResponseRedirect('/edit_profile/' + str(user))


class EditProfileForm(View):

    def get(self, request, user_id):
        user = User.objects.get(id=user_id)
        profile_user = Profile.objects.get(user=user_id)
        edit_user_form = EditForm(initial={
            'city': profile_user.city,
            'telephone_number': profile_user.telephone_number,
            'about_myself': profile_user.about_myself,
            'date_of_birth': profile_user.date_of_birth
        }, instance=user)
        # print(edit_user_form)
        # edit_user_form. = profile_user.city
        return render(request, 'users/edit_profile.html', {'form': edit_user_form})

    def post(self, request, user_id):
        user = User.objects.get(id=user_id)
        profile_user = Profile.objects.get(user=user_id)
        form = EditForm(request.POST, instance=user)

        if form.is_valid():
            profile_user.city = request.POST.get('city')
            profile_user.telephone_number = request.POST.get('telephone_number')
            profile_user.about_myself = request.POST.get('about_myself')
            old_date = request.POST.get('date_of_birth')
            profile_user.date_of_birth = datetime.datetime.strptime(old_date, '%d.%m.%Y').strftime('%Y-%m-%d')
            user.save()
            profile_user.save()

        return HttpResponseRedirect(reverse('profile'))

# def edit_profile_view(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         print(request.POST)
#         user = User.objects.get(id=request.POST.get('user_id'))
#         return HttpResponseRedirect(reverse('profile'))
#     else:
#         print(request)
#         user = User.objects.get(id=request.GET.get('user_id'))
#         edit_user = EditForm(instance=user)
#         return render(request, 'users/edit_profile.html', {'form': edit_user})
