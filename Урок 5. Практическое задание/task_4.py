"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""
from collections import deque
from random import choice
from string import ascii_lowercase
from timeit import timeit
from collections import OrderedDict


def ins_dict():
    cm_di = dict()
    letters = ascii_lowercase
    for i in range(5000):
        cm_di[i] = choice(letters)


def ins_ord():
    or_di = OrderedDict()
    letters = ascii_lowercase
    for i in range(5000):
        or_di[i] = choice(letters)


def get_dict():
    cm_di = dict()
    letters = ascii_lowercase
    for i in range(5000):
        cm_di[i] = choice(letters)
    for i in range(5000):
        bb = cm_di[i]


def get_ord():
    or_di = OrderedDict()
    letters = ascii_lowercase
    for i in range(5000):
        or_di[i] = choice(letters)
    for i in range(5000):
        bb = or_di[i]


print('ins_dict()', timeit('ins_dict()',
                           setup='from __main__ import ins_dict', number=1000))
print('ins_ord()', timeit('ins_ord()',
                          setup='from __main__ import ins_ord', number=1000))
print('get_dict()', timeit('get_dict()',
                           setup='from __main__ import get_dict', number=1000))
print('get_ord()', timeit('get_ord()',
                          setup='from __main__ import get_ord', number=1000))
# Словарь dict быстрее словаря OrderedDict для вставки и извлечения.
# Видимо, обеспечение упорядоченности влечет дополнительные
# затраты по времени.
