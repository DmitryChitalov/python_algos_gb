"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

from timeit import timeit
from collections import OrderedDict


def add_el(test_dict):
    test_dict['z'] = 'z'


def del_el(test_dict):
    test_dict.popitem()


def dict_gen(test_dict):
    test_dict = {str(x): x for x in range(1000)}


def get_el(test_dict):
    test_dict.get(str(len(test_dict)-1))


my_dict = {}
my_order_dict = OrderedDict()

my_dict_c = {str(x): x for x in range(1000)}
my_order_dict_c = OrderedDict(my_dict_c)


print(timeit("add_el(my_dict_c)", setup="from __main__ import add_el, my_dict_c", number=100_000))  # -> 0.024
print(timeit("add_el(my_order_dict_c)", setup="from __main__ import add_el, my_order_dict_c", number=100_000))  # -> 0.027

print(timeit("add_el(my_dict_c)", setup="from __main__ import add_el, my_dict_c", number=100_000))  # -> 0.024
print(timeit("add_el(my_order_dict_c)", setup="from __main__ import add_el, my_order_dict_c", number=100_000))  # -> 0.027

print(timeit("dict_gen(my_dict)", setup="from __main__ import dict_gen, my_dict", number=100_000))  # -> 52.6
print(timeit("dict_gen(my_order_dict)", setup="from __main__ import dict_gen, my_order_dict", number=100_000))  # -> 47.3

print(timeit("get_el(my_dict_c)", setup="from __main__ import get_el, my_dict_c", number=100_000))  # -> 0.077
print(timeit("get_el(my_order_dict_c)", setup="from __main__ import get_el, my_order_dict_c", number=100_000))  # -> 0.102

""" Все дейсвия с OrderedDict медленнее обычного словаря, исключение может составить его заполнение с помощью генератора,
    что +- работает одинаково """

