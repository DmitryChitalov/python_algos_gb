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


def get_time(function_to_decorate):
    def my_function(n):
        time_start = time.time()
        function_to_decorate(n)
        print(time.time() - time_start)
    return my_function


@get_time
def fill_list(n):
    print('заполнение списка ', end=' ')
    for i in range(1, str_1):
        n.append(i)


@get_time
def fill_dict(n):
    print('заполнение cловаря', end=' ')
    for i in range(1, str_1):
        n[i] = i


@get_time
def get_list_element(n):
    print('получение элементов списка ', end=' ')
    for i in n:
        n.index(i)


@get_time
def get_dict_element(n):
    print('получение элементов словаря', end=' ')
    for i in n:
        n.get(i)


str_1 = 10000
test_list = []
test_dict = {}


fill_list(test_list)
fill_dict(test_dict)

get_list_element(test_list)
get_dict_element(test_dict)

print('''
Выводы: От итерации к итерации заполнение списка быстрее, одинаково или медленнее заполнения словаря.
Cкорее всего причина кроется в способе реализации задачи, но по логике для добавления в список требуется 1 действие -
добавить элемент, в словарь - 2: добавить ключ, добавить значение.

Получение элементов из списка стабильно дольше, что подтверждает правило на уроке - посик по хешу быстрее.''')
