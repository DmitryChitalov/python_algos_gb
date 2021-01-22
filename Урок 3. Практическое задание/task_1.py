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

"""
Проведение сравнительных замеров
"""

import time
from random import randint

def my_lst():
    start_val = time.time()
    numbers = []
    for i in range(20000):
        numbers.append(randint(0, 20000))
    return round(time.time() - start_val, 5)

my_lst()

print(f'Операция заняла {my_lst()} сек')

def my_dct():
    start_loop = time.time()
    new_dict = {el: el*3 for el in range(20000)}
    end_loop = time.time()
    return round(end_loop - start_loop, 5)

my_dct()

print(f'Операция заняла {my_dct()} сек')