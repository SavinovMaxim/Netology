from django.http import HttpResponse
from django.shortcuts import render, reverse
import os
from datetime import datetime

def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': '',
        'Показать содержимое рабочей директории': ''
    }
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return HttpResponse(f"Current Time: {current_time}")


def workdir_view(request):
    workdir_contents = os.listdir('.')
    return HttpResponse(f"Work Directory Contents: {', '.join(workdir_contents)}")
