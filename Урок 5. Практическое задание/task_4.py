"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

from collections import OrderedDict
from random import randint
from timeit import timeit

N = 1000000

my_dict = {str(i): randint(0, 99) for i in range(0, 10)}
my_ordered_dict = OrderedDict(my_dict)

print(
    "Добавление случайных значений в словарь -               ",
    timeit(
        'my_dict.update({str(randint(N, N*N)): randint(0, 99)})',
        setup='from random import randint; from __main__ import my_dict, N',
        number=2*N))

print(
    "Добавление случайных значений в упорядоченный словарь - ",
    timeit(
        'my_ordered_dict.update({str(randint(N, N*N)): randint(0, 99)})',
        setup='from random import randint; from __main__ import my_ordered_dict, N',
        number=2*N))

print(
    "Выборка случайных ключей из словаря -                ",
    timeit(
        'x = my_dict.get(str(randint(N, N*N)))',
        setup='from random import randint; from __main__ import my_dict, N',
        number=N))

print(
    "Выборка случайных ключей из упорядоченного словаря - ",
    timeit(
        'x = my_ordered_dict.get(str(randint(N, N*N)))',
        setup='from random import randint; from __main__ import my_ordered_dict, N',
        number=N))

print(
    "Удаление ключей из словаря -                ",
    timeit(
        'my_dict.popitem()',
        setup='from __main__ import my_dict',
        number=N))

print(
    "Удаление ключей из упорядоченного словаря - ",
    timeit(
        'my_ordered_dict.popitem()',
        setup='from __main__ import my_ordered_dict',
        number=N))


# Вывод:
# Использовать упорядоченный словарь есть смысл только при критически важном времени выборки "случайных" значений.
# В противном случае (операции добавления и удаления) обычный словарь

