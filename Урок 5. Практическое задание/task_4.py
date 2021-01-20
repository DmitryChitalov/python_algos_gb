"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

from collections import OrderedDict
from timeit import timeit


def odict_init(odct=OrderedDict()):
    for i in range(10000):
        odct[f'{i}'] = i


def odict_read(odct=OrderedDict()):
    for key, value in odct.items():
        k = key
        v = value


def odict_get(odct=OrderedDict()):
    for i in range(10000):
        odct.get(i)




def dict_init(dct=dict()):
    for i in range(10000):
        dct[f'{i}'] = i


def dict_read(dct=dict()):
    for key, value in dct.items():
        k = key
        v = value


def dict_get(dct=dict()):
    for i in range(10000):
        dct.get(i)



gl_odct = OrderedDict()
for i in range(10000):
    gl_odct[f'{i}'] = i

gl_dct = dict()
for i in range(10000):
    gl_dct[f'{i}'] = i


print(f'odict_init:'
      f' {timeit("odict_init(gl_odct)", setup="from __main__ import odict_init, gl_odct", number=100)}')
print(f'dict_init:'
      f' {timeit("dict_init(gl_dct)", setup="from __main__ import dict_init, gl_dct", number=100)}')


print(f'odict_read:'
      f' {timeit("odict_read(gl_odct)", setup="from __main__ import odict_read, gl_odct", number=100)}')
print(f'dict_read:'
      f' {timeit("dict_read(gl_dct)", setup="from __main__ import dict_read, gl_dct", number=100)}')


print(f'odict_get:'
      f' {timeit("odict_get(gl_odct)", setup="from __main__ import odict_get, gl_odct", number=100)}')
print(f'dict_get:'
      f' {timeit("dict_get(gl_dct)", setup="from __main__ import dict_get, gl_dct", number=100)}')


"""
odict_init: 0.1515013
dict_init: 0.13219299999999998
odict_read: 0.051519800000000004
dict_read: 0.029057500000000014
odict_get: 0.0622182
dict_get: 0.05178729999999998

Операции для Dict порядка на 10-15% быстрее"""