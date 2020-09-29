"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""
import collections
from timeit import timeit


def order_dict(val):
    dict_check = collections.OrderedDict()
    for i in range(len(val)):
        dict_check[i] = val[i]
    for i in dict_check:
        dict_check.get(i)


def new_dict(val):
    dict_check = {}
    for i in range(len(val)):
        dict_check[i] = val[i]
    for i in dict_check:
        dict_check.get(i)


values = {0: 'Hello', 1: 'How', 2: 'Are', 3: 'You', 4: 'Today', 5: '?'}
print(values)
print(f'OrderedDict : {timeit("order_dict(values)", setup="from __main__ import order_dict, values", number=100000)}')
print(f'Dict : {timeit("new_dict(values)", setup="from __main__ import new_dict, values", number=100000)}')

"""
Замеры провожу с помощью timeit, так как есть возмоджность задать количество повторений
кода для более точных замеров.
Согласно полученным результатм, очевидно, что работа со  словарем происходит быстрее 
чем из со словарем коллекции OrderedDict. Предполагаю, что механизмы обеспечивающие 
упорядочение элементов в OrderedDict приводят к замедлению процессов наполнения/извлечения данных.
"""