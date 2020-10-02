"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

from timeit import timeit
from collections import OrderedDict

my_dict = {a: a * 2 for a in range(1, 100000)}
my_or_dict = OrderedDict({a: a * 2 for a in range(1, 100000)})


def get_dict(_dict):
    _dict.get('99000')


def get_o_dict(_o_dict):
    _o_dict.get('99000')


def popitem_dict(_dict):
    _dict.popitem()


def popitem_o_dict(_o_dict):
    _o_dict.popitem()


print('Сделаем get')
print(
    timeit(
        "get_dict(my_dict)",
        setup='from __main__ import get_dict, my_dict',
        number=10000))
print(
    timeit(
        "get_o_dict(my_or_dict)",
        setup='from __main__ import get_o_dict, my_or_dict',
        number=10000))
print('Сделаем много popitem')
print(
    timeit(
        "popitem_dict(my_dict)",
        setup='from __main__ import popitem_dict, my_dict',
        number=10000))
print(
    timeit(
        "popitem_o_dict(my_or_dict)",
        setup='from __main__ import popitem_o_dict, my_or_dict',
        number=10000))


"""
Вывод: get выполняется одинаково быстро, popitem у OrderedDict почему-то выполняется немного медленнее. 
Учитывая изменения dict в сторону "запоминания", лучше использовать его там, где это возможно.
"""
