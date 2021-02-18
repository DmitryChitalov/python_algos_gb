"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

import collections
import random
import timeit as t


def d_normal(c):
    a = dict()
    for i in range(c):
        a[i] = chr(random.randint(1, 200))
    return a


def d_ord(c):
    a = collections.OrderedDict()
    for i in range(c):
        a[i] = chr(random.randint(1, 200))
    return a


def d_normal_acc(z, n):
    return d_normal(z)[n]


def d_ord_acc(x, m):
    return d_ord(x)[m]


print('Insertion of elements')
print(100)
print(t.timeit("d_normal(100)", globals=globals(), number=1000))
print(t.timeit("d_ord(100)", globals=globals(), number=1000))
print(1000)
print(t.timeit("d_normal(1000)", globals=globals(), number=1000))
print(t.timeit("d_ord(1000)", globals=globals(), number=1000))
print(10000)
print(t.timeit("d_normal(10000)", globals=globals(), number=1000))
print(t.timeit("d_ord(10000)", globals=globals(), number=1000))

print('Access to elements')
print(100)
print(t.timeit("d_normal_acc(100,50)", globals=globals(), number=1000))
print(t.timeit("d_ord_acc(100,50)", globals=globals(), number=1000))
print(1000)
print(t.timeit("d_normal_acc(1000,483)", globals=globals(), number=1000))
print(t.timeit("d_ord_acc(1000,483)", globals=globals(), number=1000))
print(10000)
print(t.timeit("d_normal_acc(10000,700)", globals=globals(), number=1000))
print(t.timeit("d_ord_acc(10000,700)", globals=globals(), number=1000))

"""
Insertion of elements
100
0.08411840000000001
0.0811545
1000
0.8197867
0.8194625999999998
10000
8.1923545
8.093739
Access to elements
100
0.08037949999999938
0.08028559999999985
1000
0.8094719000000019
0.8007852
10000
7.924639500000001
8.026118599999997


Обычный словарь работает быстрее чем OrderedDict().
"""