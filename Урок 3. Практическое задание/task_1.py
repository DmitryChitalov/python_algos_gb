"""
Задание 1.

Реализуйте свои пользовательские функции, в которых реализуйте:

a) заполнение списка и словаря программно,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!
"""

from time import time


def print_time_decorator(func):
    def wrapper_function(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        print(f"Function: {str(func)} Time: {time() - start}")
        return result
    return wrapper_function


@print_time_decorator
def add_to_list(count: int):
    list_object = list()
    for index in range(count):
        list_object.append(index)
    return list_object


@print_time_decorator
def add_to_dict(count: int):
    dictionary = dict()
    for index in range(count):
        dictionary[index] = index
    return dictionary


@print_time_decorator
def dict_get_by_key(dictionary: dict, key: int):
    return dictionary[key]


@print_time_decorator
def list_get_by_index(list_obj, search_index: int):
    for index in range(len(list_obj)):
        if index == search_index:
            return list_obj[index]


@print_time_decorator
def find_dict_value(dict_obj, search_value: int):
    for value in dict_obj.values():
        if value == search_value:
            return value
    return None


@print_time_decorator
def find_list_value(list_obj, search_value: int):
    for value in list_obj:
        if value == search_value:
            return value
    return None


list_1 = add_to_list(10000000)
dict_1 = add_to_dict(10000000)
dict_get_by_key(dict_1, 900000)
list_get_by_index(list_1, 900000)

find_dict_value(dict_1, 990000)  # Function: <function find_dict_value at 0x000001E022B4F670> Time: 0.04687237739562988
find_list_value(list_1, 990000)  # Function: <function find_list_value at 0x000001E022B4F790> Time: 0.031253814697265625
find_dict_value(dict_1, 990000)  # Function: <function find_dict_value at 0x000001E022B4F670> Time: 0.09373879432678223
find_list_value(list_1, 990000)  # Function: <function find_list_value at 0x000001E022B4F790> Time: 0.06251382827758789
find_dict_value(dict_1, 990000)  # Function: <function find_dict_value at 0x000001E022B4F670> Time: 0.06247901916503906
find_list_value(list_1, 990000)  # Function: <function find_list_value at 0x000001E022B4F790> Time: 0.031246423721313477
find_dict_value(dict_1, 990000)  # Function: <function find_dict_value at 0x000001E022B4F670> Time: 0.06249809265136719
find_list_value(list_1, 990000)  # Function: <function find_list_value at 0x000001E022B4F790> Time: 0.06249403953552246
find_dict_value(dict_1, 990000)  # Function: <function find_dict_value at 0x000001E022B4F670> Time: 0.07811689376831055
find_list_value(list_1, 990000)  # Function: <function find_list_value at 0x000001E022B4F790> Time: 0.07812309265136719

# Добавление элементов в словарь занимает больше времени в виду построения хештаблицы и вычисления хэшей для ключей,
# Получение элемента из словаря по ключу намного быстрее, чем для списка благодаря хештаблице.
# Поиск по значениям ключей в словаре происходит дольше в виду особенностей структуры данных, дело может быть либо
# в values(), а также в способе итерации значений словаря.
