from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.all() #order_by('id') or order_by('-id') or order_by('id')[:5]
    return render(request, 'settings/index.html', { 'title': 'Главная страница сайта', 'tasks': tasks})


def about(request):
    return render(request, 'settings/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('main')
        else:
            error = 'Форма была неверной'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'settings/create.html', context)
