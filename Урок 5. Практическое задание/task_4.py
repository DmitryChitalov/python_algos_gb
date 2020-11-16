"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

from collections import OrderedDict
from timeit import timeit


my_dict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
my_ord_dict = OrderedDict(my_dict)


# dict functions:

def dict_func_1(dct):
    for key, value in dct.items():
        return f'The key "{key}" corresponds to the value {value}'

def dict_func_2(dct):
    dct.update({'f':6, 'g':7})
    return dct


print('Time measures of dict functions:')
print(round(timeit('dict_func_1(my_dict)', 'from __main__ import dict_func_1, my_dict'), 2))
print(round(timeit('dict_func_2(my_dict)', 'from __main__ import dict_func_2, my_dict'), 2))

# OrderedDict functions:

def ord_dict_func_1(ord_dict):
    for key, value in ord_dict.items():
        return f'The key "{key}" corresponds to the value {value}'

def ord_dict_func_2(ord_dict):
    ord_dict.update({'f':6, 'g':7})
    return ord_dict


print('Time measures of ordered dict functions:')
print(round(timeit('ord_dict_func_1(my_ord_dict)', 'from __main__ import ord_dict_func_1, my_ord_dict'), 2))
print(round(timeit('ord_dict_func_2(my_ord_dict)', 'from __main__ import ord_dict_func_2, my_ord_dict'), 2))


# to sum up:
'''
В моем случае измерения показали, что операции с OrderedDict выполняются дольше, чем операции с обычным dict'ом из коробки: 
разница не сказать, чтобы особенно существенна - d:0.64/0.54 vs ord_d:0.82/0.74 - но, полагаю, при выполнении сложных операций будет 
заметна очевиднее. 
'''

