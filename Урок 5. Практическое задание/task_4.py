"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""
from collections import OrderedDict
from timeit import timeit

simple_dict = {i: i for i in range(10)}
ordered_dict = OrderedDict(simple_dict)


def for_keys(obj):
    return {i: i*i for i in obj.keys()}


def sorted_dict(obj):
    return {i: obj[i] for i in sorted(obj)}


def for_items(obj):
    for key, value in obj.items():
        return key, value


print(timeit('for_keys(simple_dict)', 'from __main__ import for_keys, simple_dict', number=10000))  # 0.0116952599
print(timeit('for_keys(ordered_dict)', 'from __main__ import for_keys, ordered_dict', number=10000))  # 0.0232066790
print(timeit('sorted_dict(simple_dict)', 'from __main__ import sorted_dict, simple_dict', number=10000))  # 0.02904420
print(timeit('sorted_dict(ordered_dict)', 'from __main__ import sorted_dict, ordered_dict', number=10000))  # 0.03270497
print(timeit('for_items(simple_dict)', 'from __main__ import for_items, simple_dict', number=10000))  # 0.00257601
print(timeit('for_items(ordered_dict)', 'from __main__ import for_items, ordered_dict', number=10000))  # 0.002634770

"""
По всем проведенным замерам лучший результат показывает обычный dict (на pytnon 3.8), чем OrderedDict.
т.к. в новых версиях обычный dict уже упорядочен
"""