"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""
from collections import OrderedDict
from timeit import timeit

my_dict = {i: i**2 for i in range(1, 100)}
my_dict_2 = OrderedDict(my_dict)
print('Время для получения каждого элемента по ключу без OrderedDict: ')
print(timeit('''
for i in my_dict.keys():
    my_dict.get(i)
''', 'from __main__ import my_dict'))
print('Время для получения каждого элемента по ключу с OrderedDict: ')
print(timeit('''
for i in my_dict_2.keys():
    my_dict_2.get(i)
''', 'from __main__ import my_dict_2'))
print('Время для добавления элемента по ключу без OrderedDict: ')
print(timeit('''
for i in range(101, 201):
    my_dict[i] = i
''', 'from __main__ import my_dict'))
print('Время для добавления элемента по ключу с OrderedDict: ')
print(timeit('''
for i in range(101, 201):
    my_dict_2[i] = i
''', 'from __main__ import my_dict_2'))
# Время для получения каждого элемента по ключу без OrderedDict:
# 4.9428865
# Время для получения каждого элемента по ключу с OrderedDict:
# 6.5984727
# Время для добавления элемента по ключу без OrderedDict:
# 3.9401540000000015
# Время для добавления элемента по ключу с OrderedDict:
# 5.547601300000002
# OrderedDict отрабатывает медленнее обычного словаря
# Предполагаю, что в стандартном словаре Python заложена более быстрая версия
# запоминания порядка