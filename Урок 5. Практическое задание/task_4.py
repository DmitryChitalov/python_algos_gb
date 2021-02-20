"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

from collections import OrderedDict
from timeit import timeit


def create_dict(num):
    list_dict = dict()
    for i in range(num):
        list_dict[i] = i
    return list_dict


def create_order_dict(num):
    list_dict = OrderedDict()
    for i in range(num):
        list_dict[i] = i
    return list_dict


def pop_dict(list_dict):
    for i in range(len(list_dict)):
        el = list_dict.popitem()


def pop_order_dict(list_dict):
    for i in range(len(list_dict)):
        el = list_dict.popitem()


def get_dict(list_dict):
    for i in range(len(list_dict)):
        el = list_dict.get(i)


def get_order_dict(list_dict):
    for i in range(len(list_dict)):
        el = list_dict.get(i)


def print_timeint(func, n):
    print(f'{func} {timeit(f"{func}({n})", globals=globals(), number=10000)}')

n = 999
simple_dict = create_dict(n)
order_dict = create_order_dict(n)

print_timeint('create_dict', n)
print_timeint('create_order_dict', n)
print_timeint('pop_dict', simple_dict)
print_timeint('pop_order_dict', order_dict)
print_timeint('get_dict', simple_dict)
print_timeint('get_order_dict', order_dict)
print("OrderedDict медленнее словаря")
