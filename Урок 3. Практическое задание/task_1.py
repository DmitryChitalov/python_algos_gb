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


def lst(lst):
    for i in range(10000000):
        lst.append(i)


def dct(dct):
    for i in range(10000000):
        dct[i] = i


my_list = []
my_dict = {}

start_time = time.time()
lst(my_list)
print(f"!!! {time.time() - start_time} seconds !!!")

start_time = time.time()
dct(my_dict)
print(f"!!! {time.time() - start_time} seconds !!!")

"""Примерно до 400000 операций выполняется быстрее списком, а после 400000 - быстрее начинает действовать словарь
возможно, это из-за того, что числа становятся большие, которые я вставляю в список, а для словаря как был хэш, так и 
остаётся."""


def lst_pop(lst):
    for i in range(200):
        lst.remove(i)
        # lst.pop()


def dct_pop(dct):
    for i in range(200):
        del dct[i]


start_time = time.time()
lst_pop(my_list)
print(f"!!! {time.time() - start_time} seconds !!!")

start_time = time.time()
dct_pop(my_dict)
print(f"!!! {time.time() - start_time} seconds !!!")


"""Удаление немного дольше из словаря, при условии, что удаляем просто элемент, но намного дольше из списка 
(особенно если он большой) , если ищем удаляемые элементы, так как поиск по словарю намного быстрее"""