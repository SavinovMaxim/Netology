from django.http import Http404
from django.shortcuts import render

from main.models import Car, Sale


def cars_list_view(request):
    return render(request, 'main/list.html', {
        'cars': Car.objects.all().order_by('price'),
        'title': 'Каталог автомобилей'
    })

def car_details_view(request, car_id):
    try:
        car = Car.objects.get(id=car_id)
        return render(request, 'main/details.html', {
            'car': car,
            'title': f'{car.model} ({car.year})'
        })
    except Car.DoesNotExist:
        raise Http404("Автомобиль не найден")

def sales_by_car(request, car_id):
    try:
        car = Car.objects.get(id=car_id)
        sales = Sale.objects.filter(car=car).order_by('-created_at')
        return render(request, 'main/sales.html', {
            'car': car,
            'sales': sales,
            'total_sales': sales.count(),
            'title': f'История продаж {car.model}'
        })
    except Car.DoesNotExist:
        raise Http404("Автомобиль не найден")