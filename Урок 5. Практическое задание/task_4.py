"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""
from collections import OrderedDict
from timeit import timeit

n = 100000
my_dict = {el: el for el in range(n)}
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
    my_dict.update({'3': '5'})


def o_dict_upd():
    my_order_dict.update({'3': '5'})


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
Получение ключей через обычный словарь:  0.037321599999999996
Получение ключей через OrderedDict:  0.03518359999999998
Получение значений через обычный словарь:  0.034091500000000025
Получение значений через OrderedDict:  0.03417340000000002
Добавление в обычный словарь:  0.06247059999999999
Добавление в OrderedDict:  0.09901589999999999

Отличия незначительные, иногда даже OrderedDict проигрывает обычному словарю.
Применять его не имеет смысла в настоящий момент.
"""
