"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

from collections import OrderedDict
import os
import tempfile
from timeit import timeit

standard_dict = {'a': 1, 'b': 2, 'c': 3}
print('standard_dict:\t\t', standard_dict)  # -> {'a': 1, 'b': 2, 'c': 3}

collections_dict = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print('collections_dict:\t', collections_dict)  # -> OrderedDict([('a', 1), ('b', 2), ('c', 3)])


def create_big_dict(added_dict, num_key_val):
    for _ in range(num_key_val):
        key = os.path.basename(tempfile.NamedTemporaryFile().name)
        val = os.path.basename(tempfile.NamedTemporaryFile().name)
        added_dict[key] = val
    return added_dict


# # проверка на создание нового словаря
# num_of_rep = 10
# volume = 900
#
# t1 = timeit("create_big_dict(standard_dict, volume)", globals=globals(), number=num_of_rep)
# print('%.2f standard_dict' % t1)  # 4.69 standard_dict
#
# t2 = timeit("create_big_dict(collections_dict, volume)", globals=globals(), number=num_of_rep)
# print('%.2f collections_dict\n' % t2)  # 4.56 collections_dict


# # проверка времени удаления данных из словарей
# num_of_rep = 10000000
# volume = 1900
# big_standard_dict = create_big_dict(standard_dict, volume)
# big_collections_dict = create_big_dict(collections_dict, volume)
#
# print('начальная длинна big_standard_dict:', len(big_standard_dict))
# print('начальная длинна big_collections_dict:', len(big_collections_dict))
#
#
# def clear_big_dict(added_dict):
#     for _ in range(len(big_standard_dict)):
#         added_dict.popitem()
#
#
# t1 = timeit("clear_big_dict(big_standard_dict)", globals=globals(), number=num_of_rep)
# print('%.2f standard_dict' % t1)  # 2.98 standard_dict
#
# t2 = timeit("clear_big_dict(big_collections_dict)", globals=globals(), number=num_of_rep)
# print('%.2f collections_dict\n' % t2)  # 3.75 collections_dict

'''
при создании нового словаря OrderedDict показал незначительный прирост скорости около 5%
в то время как при очистки словаря его скорость ниже на 26%
'''