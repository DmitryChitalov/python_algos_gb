"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

import collections
from timeit import timeit


my_dict = {}
my_ord_dict = collections.OrderedDict()
def fill_dict():
    for i in range(0, 1000):
        my_dict[f'key_{i}'] = i**2
def fill_o_dict():
    for i in range(0, 1000):
        my_ord_dict[f'key_{i}'] = i**2

def print_d():
    for i in range(0, 1000):
        my_dict[f'key_{i}']

def print_o_d():
    for i in range(0, 1000):
        my_ord_dict[f'key_{i}']

def change_dict():
    for i in range(0, 1000):
        my_dict[f'key_{i}'] = my_dict[f'key_{i}'] * 10
def change_o_dict():
    for i in range(0, 1000):
        my_ord_dict[f'key_{i}'] = my_ord_dict[f'key_{i}'] * 10

print('Время заполнения Dict 12000 раз')
print(timeit('fill_dict()', setup="from __main__ import fill_dict", number=12000))
print('Время заполнения OrderedDict 12000 раз')
print(timeit('fill_o_dict()', setup="from __main__ import fill_o_dict", number=12000))

print('Время обращения к Dict 12000 раз')
print(timeit('print_d()', setup="from __main__ import print_d", number=12000))
print('Время обращения к OrderedDict 12000 раз')
print(timeit('print_o_d()', setup="from __main__ import print_o_d", number=12000))

print('Время изменения в Dict 12000 раз')
print(timeit('change_dict()', setup="from __main__ import change_dict", number=12000))
print('Время изменения в OrderedDict 12000 раз')
print(timeit('change_o_dict()', setup="from __main__ import change_o_dict", number=12000))

"""
Какой-либо значимой разницы в работе не наблюдается. Значения плавают вокруг одних и тех же значений
"""