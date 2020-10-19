"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

import cProfile
import collections

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
cProfile.run('my_dict_update()')        # 2.562 seconds

print(f"Извлечение из обычного словаря")
cProfile.run('my_dict_get()')           # 2.041 seconds

print(f"Добавление в OrderedDict")
cProfile.run('my_order_dict_update()')  # 3.246 seconds

print(f"Извлечение из OrderedDict")
cProfile.run('my_order_dict_get()')     # 2.106 seconds

# при добавлении обычный словарь быстрее
# при извлечении обычный словарь работает быстрее
