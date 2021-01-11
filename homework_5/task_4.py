"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""


from timeit import timeit

print(timeit('''
dict1 = {x: x**2 for x in range(10)}
#print(dict1)
for i in range(10):
    dict1.get(i)
items = dict1.items()
keys = dict1.keys()
values = dict1.values()
dict3 = {'a': 1, 'b': 2, 'c': 3 }
dict1.update(dict3)
dict2 = dict1.copy()
for i in range(10):
    dict1.pop(i)
dict1.clear()
'''))

print(timeit('''
from collections import OrderedDict

odict1 = OrderedDict()
odict1 = {x: x**2 for x in range(10)}
for i in range(10):
    odict1.get(i)
items = odict1.items()
keys = odict1.keys()
values = odict1.values()
dict3 = {'a': 1, 'b': 2, 'c': 3 }
odict1.update(dict3)
dict2 = odict1.copy()
for i in range(10):
    odict1.pop(i)
odict1.clear()
'''))

# вариант с OrderedDict незначительно, но медленнее обычного словаря