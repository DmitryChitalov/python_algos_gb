"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""


import collections
import timeit

my_dict = {'a': 1, 'b': 2, 'c': 3}
ord_dict = collections.OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# Время выполнения операций у OrderedDict и стандартного словаря почти одинаковое, поэтому стандартный словарь
# будет просто удобнее применять.

print('my_dict.fromkeys: ', timeit.timeit("my_dict.fromkeys([el for el in range(100)], 1)", "from __main__ import my_dict", number=10000))
print('ord_dict.fromkeys: ', timeit.timeit("ord_dict.fromkeys([el for el in range(100)], 1)", "from __main__ import ord_dict", number=10000), '\n')

print('my_dict.get: ', timeit.timeit("my_dict.get('c')", "from __main__ import my_dict", number=100000))
print('ord_dict.get: ', timeit.timeit("ord_dict.get('c')", "from __main__ import ord_dict", number=100000), '\n')

print('my_dict.keys: ', timeit.timeit("my_dict.keys()", "from __main__ import my_dict", number=100000))
print('ord_dict.keys: ', timeit.timeit("ord_dict.keys()", "from __main__ import ord_dict", number=100000), '\n')

print('my_dict.values: ', timeit.timeit("my_dict.values()", "from __main__ import my_dict", number=100000))
print('ord_dict.values: ', timeit.timeit("ord_dict.values()", "from __main__ import ord_dict", number=100000), '\n')

print('my_dict.items: ', timeit.timeit("my_dict.items()", "from __main__ import my_dict", number=100000))
print('ord_dict.items: ', timeit.timeit("ord_dict.items()", "from __main__ import ord_dict", number=100000), '\n')

print('my_dict.pop: ', timeit.timeit("my_dict.pop('a')", "from __main__ import my_dict", number=1))
print('ord_dict.pop: ', timeit.timeit("ord_dict.pop('a')", "from __main__ import ord_dict", number=1), '\n')
