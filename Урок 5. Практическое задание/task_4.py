"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

from timeit import timeit

from collections import OrderedDict

my_dict = {str(i): i for i in range(100)}
my_ord_dict = OrderedDict({str(i): i for i in range(100)})

def in_dict(el):
    new_dict = dict()
    for i in range(el):
        new_dict[str(i)] = i
    return new_dict

def in_ord_dict(el):
    new_dict = OrderedDict()
    for i in range(el):
        new_dict[str(i)] = i
    return new_dict

def get_values_dict(current_dict):
    return current_dict.values()

def get_values_ord_dict(current_ord_dict):
    return current_ord_dict.values()

def sorting_dict(current_dict):
    return sorted(current_dict.items(), key=lambda item: item[1])

def sorting_ord_dict(current_ord_dict):
    return sorted(current_ord_dict.items(), key=lambda item: item[1])

def popitem_dict(current_dict):
    for i in range(len(current_dict)):
        return current_dict.popitem()

def popitem_ord_dict(current_ord_dict):
    for i in range(len(current_ord_dict)):
        return current_ord_dict.popitem()




print('Функция in_dict(100)')
new_dict = in_dict(100)
print(
    timeit(
        "in_dict(100)",
        setup='from __main__ import in_dict, new_dict',
        number=10000))

print('Функция in_ord_dict(100)')
new_ord_dict = in_ord_dict(100)
print(
    timeit(
        "in_ord_dict(100)",
        setup='from __main__ import in_ord_dict, new_ord_dict',
        number=10000))

print('Функция get_values_dict')
values_list = get_values_dict(my_dict)
print(
    timeit(
        "get_values_dict(my_dict)",
        setup='from __main__ import get_values_dict, values_list',
        number=10000))

print('Функция get_values_ord_dict')
values_ord_list = get_values_ord_dict(my_ord_dict)
print(
    timeit(
        "get_values_ord_dict(my_ord_dict)",
        setup='from __main__ import get_values_ord_dict, values_list',
        number=10000))

print('Функция sorting_dict')
sorted_list = sorting_dict(my_dict)
print(
    timeit(
        "sorting_dict(my_dict)",
        setup='from __main__ import sorting_dict, sorted_list',
        number=10000))

print('Функция sorting_ord_dict')
sorted_ord_list = sorting_ord_dict(my_ord_dict)
print(
    timeit(
        "sorting_ord_dict(my_ord_dict)",
        setup='from __main__ import sorting_ord_dict, sorted_ord_list',
        number=10000))

print('Функция popitem_dict')
pop_dict = popitem_dict(my_dict)
print(
    timeit(
        "popitem_dict(my_dict)",
        setup='from __main__ import popitem_dict, pop_dict',
        number=10000))

print('Функция popitem_ord_dict')
pop_ord_dict = popitem_ord_dict(my_ord_dict)
print(
    timeit(
        "popitem_ord_dict(my_ord_dict)",
        setup='from __main__ import popitem_ord_dict, pop_ord_dict',
        number=10000))



'''

'''