"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""
from collections import OrderedDict
import timeit
import sys


def f1(li):
    """dict"""
    d = {}
    for k, v in li:
        d.setdefault(k, []).append(v)
    return d.items()


def f2(li):
    """ordereddict"""
    d = OrderedDict()
    for k, v in li:
        d.setdefault(k, []).append(v)
    return d.items()


if __name__ == '__main__':
    print(sys.version)
    few = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
    for tag, m, n in [('small', 5, 10000), ('medium', 20, 1000), ('bigger', 1000, 100), ('large', 5000, 10)]:
        for f in [f1, f2]:
            s = few * m
            res = timeit.timeit(f"{f.__name__}(s)", setup=f"from __main__ import {f.__name__}, s", number=n)
            print(f'{f.__doc__:>12}: {res/n*1000000:10.2f} micro sec/call ({len(s):,} elements, {len(f(s)):,} keys)')
            s = [(i % 10, i) for i in range(1, len(s)+1)]
            res = timeit.timeit(f"{f.__name__}(s)", setup=f"from __main__ import {f.__name__}, s", number=n)
            print(f'{f.__doc__:>12}: {res/n*1000000:10.2f} micro sec/call ({len(s):,} elements, {len(f(s)):,} keys)')
        print()


"""
значимой разницы нет. Скорей всего из-зза того, что в версии 3.8 dict уже является сортированным 
по очередности заполнения, и в целом более оптимизирован по сравнению со своими версиями до 3.6.
"""