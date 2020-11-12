"""
Задание 1.

Реализуйте заполнение списка и словаря, сделайте замеры и сделайте выводы, обоснуйте результат.
Сделайте несколько операций с каждым из объектов, сделайте замеры и сделайте выводы, обоснуйте результат.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""
from random import randint, random
import time

# 1 вариант: работает, но без декоратора
def filling_list(n, my_list):
    if n == 1:
        return my_list
    else:
        my_list.append(randint(0, 100))
        return filling_list(n - 1, my_list)

def check_1():
    start_val = time.time()
    print(filling_list(500, []))
    end_val = time.time()
    return f'Операция заняла {round((end_val - start_val), 10)} сек.'


def filling_dict(n, my_dict):
    if n == 1:
        return my_dict
    else:
        my_dict[round(random(), 2)] = randint(0, 100)
        return filling_dict(n - 1, my_dict)

def check_2():
    start_val = time.time()
    print(filling_dict(500, {}))
    end_val = time.time()
    return f'Операция заняла {round((end_val - start_val), 10)} сек.'

print(check_1())
print(check_2())
# Выводы: словарь выполняется немного дольше.

# вариант 2 с декоратором, не работает, не могу понять ошибки

# def check(func):
#     def wrapper(*args, **kwargs):
#         start_val = time.time()
#
#         func(*args, **kwargs)
#
#         end_val = time.time()
#         print(f'Операция заняла {end_val - start_val} сек.')
#     return wrapper
#
# @check
# def filling_list(n, my_list):
#     if n == 1:
#         return my_list
#     else:
#         my_list.append(randint(0, 100))
#         return filling_list(n - 1, my_list)
#
# @check
# def filling_dict(n, my_dict):
#     if n == 1:
#         return my_dict
#     else:
#         my_dict[round(random(), 2)] = randint(0, 100)
#         return filling_dict(n - 1, my_dict)
#
# filling_list(50, [])
# filling_dict(50, [])


