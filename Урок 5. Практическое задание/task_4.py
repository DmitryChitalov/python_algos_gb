"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

import cProfile
import collections
import random
my_dict = {}
my_order_dict = collections.OrderedDict()


def my_dict_update():
    for i in range(10000000):
        my_dict.setdefault(i)


def my_dict_get():
    for i in range(10000000):
        my_dict.get(i)


def my_order_dict_update():
    for i in range(10000000):
        my_order_dict.setdefault(i)


def my_order_dict_get():
    for i in range(10000000):
        my_order_dict.get(i)


print(f"Добавление в обычный словарь")
cProfile.run('my_dict_update()')        # 2.595 seconds

print(f"Извлечение из обычного словаря")
cProfile.run('my_dict_get()')           # 2.491 seconds

print(f"Добавление в OrderedDict")
cProfile.run('my_order_dict_update()')  # 3.010 seconds

print(f"Извлечение из OrderedDict")
cProfile.run('my_order_dict_get()')     # 2.486 seconds

"""
Оба варианта словаря одинаково быстро работают при извлечении элементов. А при добавлении обычный словарь работает
несколько быстрее
"""

