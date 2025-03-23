from django.shortcuts import render
from django.http import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
def recipe_view(request, dish):
    # Получаем количество порций из параметра запроса (по умолчанию 1)
    servings = request.GET.get('servings', 1)
    try:
        servings = int(servings)  # Преобразуем в число
    except ValueError:
        servings = 1  # Если преобразование не удалось, используем 1

    # Проверяем, есть ли такое блюдо в DATA
    if dish in DATA:
        # Умножаем количество ингредиентов на количество порций
        recipe = {ingredient: amount * servings for ingredient, amount in DATA[dish].items()}
        # Формируем контекст для передачи в шаблон
        context = {
            'recipe': recipe
        }
        # Рендерим шаблон с контекстом
        return render(request, 'calculator/index.html', context)
    else:
        # Если блюдо не найдено, возвращаем 404
        return render(request, '404.html', status=404)