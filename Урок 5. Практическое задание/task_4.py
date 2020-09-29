"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

from timeit import timeit
from collections import OrderedDict

dic = {k: k for k in range(15)}
ordered_dic = OrderedDict(dic)


def get_items_dic(dictionary):
    return dictionary.items()


def get_items_ord_dic(dictionary):
    return dictionary.items()


def get_elements_dic(dictionary):
    return dictionary.get(1)


def get_elements_ord_dic(dictionary):
    return dictionary.get(1)


print(f'Извлечение элементов из словаря занимает: '
      f'{timeit("lambda: get_items_dic(dic)", setup="from __main__ import get_items_dic", number=1000)}')
print(f'Извлечение элементов из OrderedDict занимает: '
      f'{timeit("lambda: get_items_ord_dic(ordered_dic)", setup="from __main__ import get_items_ord_dic", number=1000)}')
print(f'Извлечение ключей и значений из словаря занимает: '
      f'{timeit("lambda: get_elements_dic(dic)", setup="from __main__ import get_elements_dic", number=1000)}')
print(f'Извлечение ключей и значений из OrderedDict занимает: '
      f'{timeit("lambda: get_elements_ord_dic(ordered_dic)", setup="from __main__ import get_elements_ord_dic", number=1000)}')

# Извлечение элементов из словаря занимает: 0.00023159999999999847
# Извлечение элементов из OrderedDict занимает: 0.00013619999999999605
# Извлечение ключей и значений из словаря занимает: 0.00016530000000000017
# Извлечение ключей и значений из OrderedDict занимает: 0.0001364000000000018
# Таким образом, операции с OrderedDict, действительно, занимают меньше времени, чем со словарем
