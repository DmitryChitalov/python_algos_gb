"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

from collections import OrderedDict
from timeit import timeit

simple_dict = {1: '1',
               2: '2',
               3: '3',
               4: '4',
               5: '5'}
ordered_dict = OrderedDict(simple_dict)


def for_keys(obj):
    for i in obj.keys():
        obj[i] *= i**10**10
        return


def for_items(obj):
    for i, j in obj.items():
        return


def sorted_dict(obj):
    return {i: obj[i] for i in sorted(obj)}


print(timeit('for_keys(simple_dict)', 'from __main__ import for_keys, simple_dict', number=10000))          # 0.0153661
print(timeit('for_keys(ordered_dict)', 'from __main__ import for_keys, ordered_dict', number=10000))        # 0.0117650
print(timeit('for_items(simple_dict)', 'from __main__ import for_items, simple_dict', number=10000))        # 0.0021601
print(timeit('for_items(ordered_dict)', 'from __main__ import for_items, ordered_dict', number=10000))      # 0.0023770
print(timeit('sorted_dict(simple_dict)', 'from __main__ import sorted_dict, simple_dict', number=10000))    # 0.0104420
print(timeit('sorted_dict(ordered_dict)', 'from __main__ import sorted_dict, ordered_dict', number=10000))  # 0.0110497

'''
Разница незначительна (3-5%)
Но даже при такой разнце OrderedDict выигрывает. 

В новых версиях Python обычный словарь уже упорядочен.
Смысл использовать OrederedDict есть разве что из-за незначительно превосходящей скорости. 
'''