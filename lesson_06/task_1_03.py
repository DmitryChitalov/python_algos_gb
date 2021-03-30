"""
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск n компаний с наибольшей годовой прибылью.
"""

from profile_code import profile_code
from random import randint


companies_dict = {str(key): randint(1000, 1000000) for key in range(10000)}


@profile_code(50)
def sort_by_profit(data: dict, num: int):
    result_list = list(data)
    result_list.sort(key=lambda x: data[x], reverse=True)
    return [(key, data[key]) for key in result_list[:num]]


@profile_code(50)
def sort_by_profit_refactor(data: dict, num: int):
    result_list = list(data)
    result_list.sort(key=lambda x: data[x], reverse=True)
    return ((key, data[key]) for key in result_list[:num])


sort_by_profit(companies_dict, 1000)
# Время: 11.019330800000002, Память: 0.19921875

sort_by_profit_refactor(companies_dict, 1000)
# Время: 10.960874000000002, Память: 0.02734375

# Для анализа взята функция из 3 задания к первому уроку. Для показательности результатов ищем не 3 фирмы,
# а 1000 фирм из 10000. Очень простой рефакторинг - вместо списка возвращаем генератор, ведь скорее всего, всё,
# что мы будем делать с результатом, это итерироваться по нему. Выигрыш по памяти очевиден. Кроме того,
# и скорость выполнения стала немного ниже.
