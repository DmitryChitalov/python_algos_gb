"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

from collections import OrderedDict
import timeit


def dict(u_d):
    keys = u_d.keys()
    keys = sorted(keys)
    for key in keys:
        print(key, u_d[key])
    return


def o_dict(u_d):
    new_d = OrderedDict(sorted(u_d.items()))
    for key in new_d:
        print(key, new_d[key])
    return

x = float(round(timeit.timeit("dict({'бананы': 3, 'яблоки': 1, 'груши': 2, 'апельсины': 4})",
                          setup="from __main__ import dict", number=100000), 4))

print(f'скорость выполнения Упорядоченный Словарь:',
      round(timeit.timeit("o_dict({'бананы': 3, 'яблоки': 1, 'груши': 2, 'апельсины': 4})",
                          setup="from __main__ import o_dict", number=100000), 4))
print(f'скорость выполнения Словаря:',x)
"""
Задача 4.
Упорядоченный Словарь быстрее, видимо за счет первоначально упорядоченной структуры. 
"""
