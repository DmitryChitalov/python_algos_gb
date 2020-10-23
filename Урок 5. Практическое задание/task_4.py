"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""
from collections import OrderedDict
import timeit

my_dict = {'first': 1, 'second': 2, 'third': 3, 'forth': 4}

def dict_get():
    return my_dict.get('third')

def or_dict_get():
    return OrderedDict(my_dict).get('third')

def dict_items():
    return my_dict.items()

def or_dict_items():
    return OrderedDict(my_dict).items()

def dict_pop():
    return (my_dict.pop('first'))

def or_dict_pop():
    return OrderedDict(my_dict).pop('second')

print(timeit.timeit("dict_get()", setup="from __main__ import dict_get"))  #0.17801
print(timeit.timeit("or_dict_get()", setup="from __main__ import or_dict_get"))  #1.0293092
print(timeit.timeit("dict_items()", setup="from __main__ import dict_items"))  #0.161162399999982
print(timeit.timeit("or_dict_items()", setup="from __main__ import or_dict_items"))  #0.9273182
print(timeit.timeit("dict_pop()", setup="from __main__ import dict_pop"))  #0.161162399999982
print(timeit.timeit("or_dict_pop()", setup="from __main__ import or_dict_pop"))  #1.119293399999
'''
В данном случае трудно сказать однозначно, но у меня вышло, что ордердикт работает медленнее дикта... 
возможно что-то не так в замерах, или другие операции сравнить. Ордердикт медленнее.
'''

