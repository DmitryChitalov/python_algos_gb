"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""
from collections import defaultdict
from collections import OrderedDict
from timeit import timeit

def f1(li=100):
    '''defaultdict'''
    d = defaultdict(list)
    for k in range(li):
        d[k].append(k)
    return d.items()

def f2(li=100):
    '''setdefault'''
    d={}
    for k in range(li):
        d.setdefault(k, []).append(k)
    return d.items()

def f3(li=100):
    '''OrderedDict'''
    d=OrderedDict()
    for k in range(li):
        d.setdefault(k, []).append(k)
    return d.items()

print(timeit('f1(li=100)', setup='from __main__ import f1', number=1000000))

print(timeit('f2(li=100)', setup='from __main__ import f2', number=1000000))

print(timeit('f3(li=100)', setup='from __main__ import f3', number=1000000))

'''
22.2895554 - defaultdict
15.361668199999997 - setdefault
20.098303599999994 - OrderedDict
Как показали замеры, генерация простого словаря самое быстрое
'''