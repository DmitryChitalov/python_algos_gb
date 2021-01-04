"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

from collections import OrderedDict
from timeit import timeit

my_dict = {el: el for el in range(10000)}
ord_dct = OrderedDict(my_dict)


def for_in_dct(dct):
    for key in dct.keys():
        dct[key] = key * 2
    return dct


print(timeit('for_in_dct(my_dict)', setup='from __main__ import for_in_dct, my_dict', number=10000), 'обычный словарь')
print(timeit('for_in_dct(ord_dct)', setup='from __main__ import for_in_dct, ord_dct', number=10000), 'OrderedDict')

"""
результат:

8.7115476 обычный словарь
13.023754499999999 OrderedDict

вывод: перебор элементов обычного словаря о существляется быстрее
"""


def get_in_dct(dct):
    for k in dct.keys():
        dct.get(k)
    return ''


print(timeit('get_in_dct(my_dict)', setup='from __main__ import get_in_dct, my_dict', number=10000),
      'элементы по ключу обычный словарь')
print(timeit('get_in_dct(ord_dct)', setup='from __main__ import get_in_dct, ord_dct', number=10000),
      'элементы по ключу OrderedDict')

"""
результат:

6.343992 элементы по ключу обычный словарь
10.069524099999999 элементы по ключу OrderedDict

вывод: в данном примере обычный словарь снова оказался быстрее
"""
