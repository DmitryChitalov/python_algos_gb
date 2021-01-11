"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

from collections import OrderedDict
from timeit import timeit

dict_d = {'персона': 'человек', 'марафон': 'гонка бегунов длиной около 26 миль', 
'противостоять': 'оставаться сильным, несмотря на давление', 'бежать': 'двигаться со скоростью'}

ord_dict = OrderedDict(dict_d)

def dict_tries():
    dict_keys = dict_d.keys()
    dict_values = dict_d.values()
    dict_d['персона'] = 'man'
    dict_d.clear()
    new_dict_d = {a: a ** 2 for a in range(7)}
    return new_dict_d

def ord_tries():
    ord_dict_keys = ord_dict.keys()
    ord_dict_values = ord_dict.values()
    ord_dict['персона'] = 'man'
    ord_dict.clear()
    new_ord_dict = {a: a ** 2 for a in range(7)}
    return new_ord_dict

print(dict_tries())
print(ord_tries())

print(timeit("dict_tries()", setup="from __main__ import dict_tries, dict_d", number=1000))   # 0.0031014089999999994
print(timeit("ord_tries()", setup="from __main__ import ord_tries, ord_dict", number=1000)) # 0.002689798


""" После проведения замеров, простого словаря и упорядоченного, можно увидеть что упорядоченный
словарь имеет производительность выше, чем простой словарь. """