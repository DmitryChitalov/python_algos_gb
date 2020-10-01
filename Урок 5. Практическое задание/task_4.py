"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""
# Вывод: defaultdict быстрее обычного словаря

import random
import collections
import timeit



def dict_add():
    my_dict = {}
    for i in range(10):
        my_dict[f'{i}'] = [random.randint(1, 100) for i in range(10)]
    my_dict.popitem()
    my_dict.values()
    my_dict.keys()

    return my_dict


def default_dict_add():
    my_def_dict = collections.defaultdict(int)
    for i in range(10):
        my_def_dict[f'{i}'] = [random.randint(1, 100) for i in range(10)]
    my_def_dict.popitem()
    my_def_dict.values()
    my_def_dict.keys()
    return my_def_dict


print(dict_add())
print(default_dict_add())

print(timeit.timeit('dict_add', setup='from __main__ import dict_add', number=10000))
print(timeit.timeit('default_dict_add', setup='from __main__ import default_dict_add', number=10000))