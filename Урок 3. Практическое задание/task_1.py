"""
Задание 1.

Реализуйте заполнение списка и словаря, сделайте замеры и сделайте выводы, обоснуйте результат.
Сделайте несколько операций с каждым из объектов, сделайте замеры и сделайте выводы, обоснуйте результат.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""


import time
from functools import wraps


def stopwatch(func):
    @wraps(func)
    def wrapper(*args):
        start_val = time.time()
        func(*args)
        end_val = time.time()
        return print(f'Операция заняла: {end_val - start_val:.10f} сек')
    return wrapper


@stopwatch
def list_generator(n):
    some_list = [i for i in range(1, n)]
    return some_list


@stopwatch
def dict_generator(n):
    some_dict = {x: x for x in range(n)}
    return some_dict


print(f'---Some List---')
for i in range(5):
    list_generator(1000)
print()

for i in range(5):
    list_generator(10000)
print()

for i in range(5):
    list_generator(100000)
print()

print(f'---Some Dict---')
for i in range(5):
    dict_generator(1000)
print()

for i in range(5):
    dict_generator(10000)
print()

for i in range(5):
    dict_generator(100000)
print()
