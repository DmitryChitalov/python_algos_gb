"""
Задание 3.

Для этой задачи:
1) придумайте 1-3 решения (желательно хотя бы два)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.


Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
"""

import random


# O(n)
# Нахождение топ заработков и соответсвующих компаний этим заработкам
def find_most_profitable1(dct: dict):
    top_values = list(dct.values())
    top_values.sort(reverse=True)
    output_dict = {}
    for key, itm in dct.items():
        if itm in top_values[:3]:
            output_dict.update({key: itm})
    return output_dict


# O(n)
# Поидее функция должна быть быстрее первой, ведь сначала создается отсортированный словарь, а затем уже перебирается
# содержимое
def find_most_profitable2(dct: dict):
    return {key: itm for key, itm in sorted(dct.items(), key=lambda item: item[1])[-3:]}


# O(n^2)
# Уже не знал как изощриться и получилось оно
def find_most_profitable3(dct: dict):
    output_dict = {}
    for item in dct.items():
        if len(output_dict.keys()) < 3:
            output_dict.update({item[0]: item[1]})
        else:
            output_dict_new = output_dict.copy()
            for key, itm in output_dict.items():
                if item[1] > itm and item[0] not in output_dict_new.keys():
                    output_dict_new.pop(key)
                    output_dict_new.update({item[0]: item[1]})
            output_dict = output_dict_new.copy()
    return output_dict


companies_profit = {
    'Geekbrains': random.randint(10000, 1000000000),
    'VK': random.randint(10000, 1000000000),
    'Google': random.randint(10000, 1000000000),
    'Youtube': random.randint(10000, 1000000000),
    'Mail.ru': random.randint(10000, 1000000000),
    'Tesla': random.randint(10000, 1000000000),
}

print(companies_profit)
print(find_most_profitable1(companies_profit))
print(find_most_profitable2(companies_profit))
print(find_most_profitable3(companies_profit))

# Вывод: второе задание по моему мнению самое эффективное, т.к. хоть сложность и линейная как и с первым вариантом, но
# по факту выполняться должно быстрее
