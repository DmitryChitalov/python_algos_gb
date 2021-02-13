"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""
"""
OrderedDict требует больше ресурсов, чем обычный словарь, но реализация позволяет 
использовать его как, например, стек, или хранение отсортированных данных
"""
from timeit import timeit
from random import randint
import collections

v_ord_dict = collections.OrderedDict([(1, 'a'), (2, 'b'), (3, 'c')])
v_def_dict = {1: 'a', 2: 'b', 3: 'c'}

key = 2
val = 'b'
for i in range(1000):
    v_ord_dict[i] = str(i)

print(v_ord_dict)
print(v_def_dict)

print(
    timeit(
        "v_def_dict[key]=val",
        setup='from __main__ import v_def_dict, key, val',
        number=1000))
print(
    timeit(
        "v_def_dict[key]",
        setup='from __main__ import v_def_dict, key',
        number=1000))
print(
    timeit(
        "v_ord_dict[key]=val",
        setup='from __main__ import v_ord_dict, key, val',
        number=1000))
print(
    timeit(
        "v_ord_dict.popitem()",
        setup='from __main__ import v_ord_dict',
        number=1000))
