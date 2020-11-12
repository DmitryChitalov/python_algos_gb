"""
Задание 1.

Докажите, что словари обрабатываются быстрее, чем списки.

Реализуйте две функции, в первой нужно заполнить элементами список, во второй-словарь
Сделайте замеры времени выполнения каждой из функций

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""

from random import randrange
import time

number = 10000000


def timer(func):
    start = time.time()
    func()
    return time.time() - start


def add_list():
    lst = [i for i in range(number)]


def add_dict():
    dct = {i: i for i in range(number)}


print(timer(add_list))
print(timer(add_dict))
