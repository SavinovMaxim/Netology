cook_book = {
    'Омлет': [
        {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
        {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
        {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
    'Утка по-пекински': [
        {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
        {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
        {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
        {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
    'Запеченный картофель': [
        {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
        {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
        {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ]
}

def GetList(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                ingredient_name = ingredient['ingredient_name']
                quantity = ingredient['quantity'] * person_count
                measure = ingredient['measure']

                if ingredient_name in shop_list:
                    shop_list[ingredient_name]['quantity'] += quantity

                else:
                    shop_list[ingredient_name] = {'quantity': quantity, 'measure': measure}
        else:
            print(f"Блюдо '{dish}' не найдено в книге рецептов.")

    return shop_list

def print_shopping_list(shopping_list):
  for ingredient, details in shopping_list.items():
    print(f"{ingredient}: {details}")

shopping_list = GetList(['Запеченный картофель', 'Омлет'], 2)
print_shopping_list(shopping_list)
print()
shopping_list2 = GetList(['Запеченный картофель', 'Омлет', "Несуществующее блюдо"], 2)
print_shopping_list(shopping_list2)
print()
shopping_list3 = GetList(['Омлет', 'Утка по-пекински'], 3)
print_shopping_list(shopping_list3)