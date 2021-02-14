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


def list_fill(lst, length):
    start = time.time()
    for i in range(length):
        lst.append(i)
    end = time.time()
    print(f'Заполнение списка заняло {end - start} секунд')


def dict_fill(dct, length):
    start = time.time()
    for i in range(length):
        dct[i] = i
    end = time.time()
    print(f'Заполнение словаря заняло {end - start} секунд')


def lst_search_val(lst, val):
    start = time.time()
    for i in range(len(lst)):
        if lst[i] == val:
            end = time.time()
            print(f'Поиск значения в списке занял {end - start} секунд')
            return i


def dct_serach_val(dct, val):
    start = time.time()
    for i in range(len(dct)):
        if dct.get(i) == val:
            end = time.time()
            print(f'Поиск значения в словаре занял {end - start} секунд')
            return i


def lst_get_val(lst, idx):
    start = time.time()
    for i in range(100000):
        v = lst[idx]
    print(v)
    end = time.time()
    print(f'Значение по индексу из списка получено за {end - start} секунд')


def dict_get_val(dct, k):
    start = time.time()
    for i in range(100000):
        v = dct[k]
    print(v)
    end = time.time()
    print(f'Значение по ключу из словаря получено за {end - start} секунд')


my_list = []
my_dict = {}

list_fill(my_list, 100000)
dict_fill(my_dict, 100000)
# Заполнение словаря дольше, т.к. необходимо дополнительно вычислять хэши ключей
lst_search_val(my_list, 68412)
dct_serach_val(my_dict, 68412)
# Поиск значения в словаре методом перебора значений происходит дольше
lst_get_val(my_list, 85963)
dict_get_val(my_dict, 85963)
# Получение значения из словаря по ключу происходит дольше получения значения из списка по индексу
# (для 100 тысяч итераций, для одной итерации счетчики всегда показывают 0
