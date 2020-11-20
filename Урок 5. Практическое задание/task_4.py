"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""
from timeit import timeit
from collections import OrderedDict

dic = {i: i for i in range(10000)}
ordered_dic = OrderedDict(dic)


def get_items_dic(dictionary):
    return dictionary.items()


def get_items_ord_dic(dictionary):
    return dictionary.items()


def get_elements_dic(dictionary):
    return dictionary.get(1)


def get_elements_ord_dic(dictionary):
    return dictionary.get(1)


def update_dict(dict, other):
    dict.update(other)


def update_o_dict(dict, other):
    dict.update(other)


other = {i: i for i in range(100)}

print(timeit('get_items_dic(dic)', setup="from __main__ import get_items_dic, dic", number=10000))
print(timeit('get_items_ord_dic(ordered_dic)', setup="from __main__ import get_items_ord_dic, ordered_dic", number=10000))
print(timeit('get_elements_dic(dic)', setup="from __main__ import get_elements_dic, dic", number=10000))
print(timeit('get_elements_ord_dic(ordered_dic)', setup="from __main__ import get_elements_ord_dic, ordered_dic", number=10000))
print(timeit('update_dict(dic, other)', setup="from __main__ import update_dict, dic, other", number=10000))
print(timeit('update_o_dict(ordered_dic, other)', setup="from __main__ import update_o_dict, ordered_dic, other", number=10000))

#OrderedDict С функцией update работает гораздо медленнее, в остальном +- одинаково