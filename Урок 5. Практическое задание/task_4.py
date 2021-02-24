"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

from collections import OrderedDict
from timeit import timeit

my_dict = {el: el for el in range(20000)}
my_order_dict = OrderedDict(my_dict)


# Полуение ключей
def dict_getkeys():
    my_dict.keys()


def order_dict_getkeys():
    my_order_dict.keys()


# Получение значений
def dict_values():
    my_dict.values()


def order_dict_values():
    my_order_dict.values()


# Обновление элементов

def dict_update():
    my_dict.update({'100': '23'})


def order_dict_update():
    my_order_dict.update({'100': '23'})


numbers = 5000000

print('Извлечение ключей через словарь: ',
      timeit("dict_getkeys()", globals=globals(), number=numbers))
print('Извлечение ключей через OrderedDict: ',
      timeit("order_dict_getkeys()", globals=globals(), number=numbers))
print('Извлечение значений через словарь: ',
      timeit("dict_values()", globals=globals(), number=numbers))
print('Извлечение значений через OrderedDict: ',
      timeit("order_dict_values()", globals=globals(), number=numbers))
print('Обновление значений в словаре: ',
      timeit("dict_update()",globals=globals(), number=numbers))
print('Обновление значений в OrderedDict: ',
      timeit("order_dict_update()",globals=globals(), number=numbers))

"""
Извлечение ключей через словарь:  0.8314403619999999
Извлечение ключей через OrderedDict:  0.7555105950000001
Извлечение значений через словарь:  0.7400107009999999
Извлечение значений через OrderedDict:  0.738951717
Обновление значений в словаре:  1.3898034699999995
Обновление значений в OrderedDict:  2.3170796649999996

Получение значений и ключей быстрее с помощью OrderedDict,
а вот update определенно дольше происходит.

"""
