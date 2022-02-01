from django.shortcuts import render
from django.http import HttpResponse, request

def advertisement_list(request, *args, **kwargs):
    return render(request, 'advertisement/advertisement_list.html', {})

def course1(request, *args, **kwargs):
    return render(request, 'advertisement/course1_web_dev.html', {})

def course2(request, *args, **kwargs):
    return render(request, 'advertisement/course2_python_django.html', {})

def course3(request, *args, **kwargs):
    return render(request, 'advertisement/course3_data_scientist.html', {})

def course4(request, *args, **kwargs):
    return render(request, 'advertisement/course4_java.html', {})

def course5(request, *args, **kwargs):
   return render(request, 'advertisement/course5_android.html', {})
