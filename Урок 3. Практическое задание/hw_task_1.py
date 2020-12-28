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

KEYS = range(10)
VALUES = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetuer', 'adipiscing', 'elit', 'Aenean', 'commodo']

t1 = time.perf_counter()
u_dicts = dict(zip(KEYS, VALUES))
print(u_dicts)
print(time.perf_counter() - t1, 'seconds')  # --> 2.0700000000012375e-05 seconds

t2 = time.perf_counter()
u_list = [i for i in range(10)]
print(u_list)
print(time.perf_counter() - t2, 'seconds')  # --> 1.1999999999998123e-05 seconds

# list() быстрее наполняется
