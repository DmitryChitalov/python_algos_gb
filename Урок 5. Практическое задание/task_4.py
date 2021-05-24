"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""
from collections import OrderedDict
from timeit import timeit

n = 100000
my_dict = {element: element for element in range(n)}
my_order_dict = OrderedDict(my_dict)


def dict_keys():
    my_dict.keys()


def o_dict_keys():
    my_order_dict.keys()


def dict_val():
    my_dict.values()


def o_dict_val():
    my_order_dict.values()


def dict_upd():
    my_dict.update({'2': '3'})


def o_dict_upd():
    my_order_dict.update({'2': '3'})


print('Получение ключей через обычный словарь: ',
      timeit("dict_keys()", setup="from __main__ import dict_keys", number=n))
print('Получение ключей через OrderedDict: ',
      timeit("o_dict_keys()", setup="from __main__ import o_dict_keys", number=n))
print('Получение значений через обычный словарь: ',
      timeit("dict_val()", setup="from __main__ import dict_val", number=n))
print('Получение значений через OrderedDict: ',
      timeit("o_dict_val()", setup="from __main__ import o_dict_val", number=n))
print('Добавление в обычный словарь: ',
      timeit("dict_upd()", setup="from __main__ import dict_upd", number=n))
print('Добавление в OrderedDict: ',
      timeit("o_dict_upd()", setup="from __main__ import o_dict_upd", number=n))

"""
Получение ключей через обычный словарь:  0.0119448
Получение ключей через OrderedDict:  0.0121557
Получение значений через обычный словарь:  0.0123044
Получение значений через OrderedDict:  0.012166999999999997
Добавление в обычный словарь:  0.0217081
Добавление в OrderedDict:  0.0316023


OrderedDict проигрывает обычному словарю, кроме одного замера и то скорее всего случайно, но есть у него и плюсы,
скорее всего в своих проектах иногда буду его использовать.
"""
