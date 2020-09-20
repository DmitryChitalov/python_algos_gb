"""
Задание 1.

Реализуйте заполнение списка и словаря, сделайте замеры и сделайте выводы, обоснуйте результат.
Сделайте несколько операций с каждым из объектов, сделайте замеры и сделайте выводы, обоснуйте результат.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""

import random
import time


def check_list(n):
    start_val = time.time()
    list = []
    for item in range(n):
        list.append(random.random())
    end_val = time.time()
    return list, end_val - start_val


def check_list_gen(n):
    start_val = time.time()
    list = [random.random() for item in range(n)]
    end_val = time.time()
    return list, end_val - start_val


def check_voc(n):
    voc = {}
    start_voc = time.time()
    for item in range(n):
        voc[item] = {random.random(): random.random()}
    end_voc = time.time()
    return list, end_voc - start_voc


def check_voc_gen(n):
    start_voc = time.time()
    voc = {random.random(): random.random() for item in range(n)}
    end_voc = time.time()
    return list, end_voc - start_voc


print(f'Операция Список заняла {check_list(1000000)[1]} сек')
print(f'Операция Список-генератор заняла {check_list_gen(1000000)[1]} сек')
print(f'Операция Cловарь заняла {check_voc(1000000)[1]} сек')
print(f'Операция Cловарь-генератор заняла {check_voc_gen(1000000)[1]} сек')
