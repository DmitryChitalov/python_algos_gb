"""Генерация списков"""
from timeit import Timer


def test_concat():
    my_lst = []
    for i in range(1000):
        my_lst = my_lst + [i]


def test_cycle():
    my_lst = []
    for i in range(1000):
        my_lst.append(i)


def test_gener():
    my_lst = [i for i in range(1000)]


def test_range():
    my_lst = list(range(1000))

t1= Timer("test_concat()","from ___main__ import test_concat()")) # создаем объект  <timeit.Timer object at 0x00000000020B6710>

