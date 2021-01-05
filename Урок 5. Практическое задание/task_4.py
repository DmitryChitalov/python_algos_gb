"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""
import timeit
from collections import OrderedDict
from random import randint

new_dct = {}
dct_col = OrderedDict()

print(timeit.timeit('new_dct',
                    setup='from __main__ import new_dct',
                    number=1000000))   # 0.023627677001059055

print(timeit.timeit('dct_col',
                    setup='from __main__ import dct_col',
                    number=1000000))   # 0.02154662600150914

print(type(new_dct))
print(type(dct_col))

new_dct = {i: i for i in range(1000)}
dct_col = OrderedDict({i: i for i in range(1000)})

print(type(new_dct), new_dct)
print(type(dct_col), dct_col)

print(timeit.timeit('new_dct={i: i for i in range(1000)}',
                    setup='from __main__ import new_dct',
                    number=10000))   # 0.6512544939978397

print(timeit.timeit('dct_col',
                    setup='from __main__ import dct_col',
                    number=10000))   # 0.0001322129974141717

print(timeit.timeit('new_dct[randint(0, 999)]',
                    setup='from __main__ import new_dct, randint',
                    number=1000000))   # 0.8624748420006654

print(timeit.timeit('dct_col[randint(0, 999)]',
                    setup='from __main__ import dct_col, randint',
                    number=1000000))   # 0.8537719029991422

"""
По итогам замеров видно, что collections.OrderedDict работает быстрее dict
"""
