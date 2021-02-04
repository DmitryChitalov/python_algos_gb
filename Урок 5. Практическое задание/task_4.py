"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
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
Insertion of elements(first element is default dictionary, second - ordered)
100
0.11657260000000001
0.13479539999999998
1000
1.1451972000000001
1.1726967
10000
13.8865764
14.622254300000002
Access to elements
100
0.13089829999999836
0.14055979999999835
1000
1.3226176000000045
1.4730764999999977
10000
13.7401756
14.5860044


Как видно из отчета на Пайтоне 3.8 обычный словарь работает быстрее в любом случае чем OrderedDict(). 
Возможно есть смысл использовать второй словарь в случае более давней версии пайтона.
"""
