"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

from collections import OrderedDict
from random import randint
from timeit import timeit


def append_dict():
    for i in range(200):
        var_dict[i] = i


def append_order_dict():
    for i in range(200):
        var_order_dict[i] = i


def get_dict():
    j = var_dict.get(5)


def get_order_dict():
    j = var_order_dict.get(5)


def keys_dict():
    j = var_dict.keys()


def keys_order_dict():
    j = var_order_dict.keys()


var_dict = dict()
var_order_dict = OrderedDict()

print('append_dict:\t', timeit("append_dict()",
                               setup="from __main__ import append_dict",
                               number=100000))
print('append_order_dict:\t',
      timeit("append_order_dict()",
             setup="from __main__ import append_order_dict",
             number=100000))

print('----------------------------------')

print('get_dict:\t', timeit("get_dict()",
                            setup="from __main__ import get_dict",
                            number=100000))
print('get_order_dict:\t', timeit("get_order_dict()",
                                  setup="from __main__ import get_order_dict",
                                  number=100000))

print('----------------------------------')

print('keys_dict:\t', timeit("keys_dict()",
                             setup="from __main__ import keys_dict",
                             number=100000))
print('keys_order_dict:\t', timeit("keys_order_dict()",
                                   setup="from __main__ import keys_order_dict",
                                   number=100000))

#
# append_dict:	 2.9707382
# append_order_dict:	 2.4739006000000003
# ----------------------------------
# get_dict:	 0.03362310000000068
# get_order_dict:	 0.02656529999999968
# ----------------------------------
# keys_dict:	 0.018112299999999415
# keys_order_dict:	 0.0246795999999998
#
# Операции с Dict и OrderedDict выполняются примерно одинаково,
# особого смысла использовать OrderedDict нет
