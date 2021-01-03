"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

from collections import OrderedDict
from timeit import timeit

def fill_simple_dict():
    simple_dict = dict()
    for i in range(10000):
        simple_dict[i] = i

def fill_ordered_dict():
    ordered_dict = OrderedDict()
    for i in range(10000):
        ordered_dict[i]= i

s = dict()
o = OrderedDict()
for i in range(10000):
    s[i] = i
    o[i] = i

def find_in_simple_dict(simple_dict : dict):
    for i in range(10000):
        if i in simple_dict:
            pass

def find_in_ordered_dict(ordered_dict : OrderedDict):
    for i in range(10000):
        if i in ordered_dict:
            pass


print("fill_simple_dict: ", timeit("fill_simple_dict()","from __main__ import fill_simple_dict",number=1000))
print("fill_ordered_dict: ",timeit("fill_ordered_dict()","from __main__ import fill_ordered_dict",number=1000))

print("find_in_simple_dict: ", timeit("find_in_simple_dict(s)","from __main__ import find_in_simple_dict, s",number=10000))
print("find_in_ordered_dict: ",timeit("find_in_ordered_dict(o)","from __main__ import find_in_ordered_dict, o",number=10000))

"""Вывод: целесообразнее использовать обычный dict, т.к при операциях заполнения словаря, он работает на 30% быстрее OrderedDict
Что касается операции поиска ключа, то оба контейнера работают примерно одинаково(но обычный словарь тут тоже опережает)
Вывод программы:
fill_simple_dict:  1.3148751760000001
fill_ordered_dict:  2.039563823
find_in_simple_dict:  8.821126876000001
find_in_ordered_dict:  8.844777422
"""
