"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""
from collections import OrderedDict
from timeit import repeat, timeit

my_dict = {str(i): i for i in range(20)}
od_dict = OrderedDict({str(i): i for i in range(20)})
print(my_dict)
print(od_dict)

def dict_key():
    return my_dict.keys()
def od_key():
    return od_dict.keys()
def dict_val():
    return sum(my_dict.values())
def od_val():
    return sum(od_dict.values())
def dict_get():
    return my_dict.get(12)
def od_get():
    return od_dict.get(12)

print('keys - ', repeat('dict_key', setup='from __main__ import dict_key', repeat=3))
print('keys OD - ', repeat('od_key', setup='from __main__ import od_key', repeat=3))
print('summa - ', repeat('dict_val', setup='from __main__ import dict_val', repeat=3))
print('summa OD - ', repeat('od_val', setup='from __main__ import od_val', repeat=3))
print('get - ', repeat('dict_get', setup='from __main__ import dict_get', repeat=3))
print('get OD - ', repeat('od_dict', setup='from __main__ import od_dict', repeat=3))

'''OrderDict показал себя не с лучшей стороны, при следующих методах работы со словарями -
keys(), sum(.values() и .get() обычный словарь показал лучше результаты.
keys - [0.0356938, 0.041751200000000016, 0.045113199999999964]
keys OD - [0.03277950000000002, 0.05124649999999997, 0.032773600000000014]
summa - [0.03345219999999999, 0.05053679999999999, 0.038982699999999926]
summa OD - [0.043850899999999915, 0.028469700000000042, 0.04190920000000009]
get - [0.036204400000000025, 0.030534300000000014, 0.03128900000000001]
get OD - [0.03522219999999998, 0.0339971, 0.028325800000000068]'''