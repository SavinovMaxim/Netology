from django.http import HttpResponse
from django.shortcuts import render, reverse
import os
from datetime import datetime


def home_view(request):
    # Список доступных страниц
    pages = [
        {'name': 'Home', 'url': reverse('home')},
        {'name': 'Current Time', 'url': reverse('current_time')},
        {'name': 'Work Directory', 'url': reverse('workdir')},
    ]
    return render(request, 'home.html', {'pages': pages})

def time_view(request):
    # Получаем текущее время
    now = datetime.now()
    # Форматируем время в удобный формат
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    # Возвращаем HTTP-ответ с текущим временем
    return HttpResponse(f"Current Time: {current_time}")


def workdir_view(request):
    # Получаем список файлов и папок в текущей рабочей директории
    workdir_contents = os.listdir('.')
    
    # Рендерим шаблон и передаем в него список файлов
    return render(request, 'workdir.html', {'workdir_contents': workdir_contents})
