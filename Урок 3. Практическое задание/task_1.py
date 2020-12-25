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


def func_time(func):
    def wrap(*args, **kwargs):
        start_time = time.time()
        func(args[0])
        print(time.time() - start_time)
    return wrap


@func_time
def list_check(n):
    my_list = []
    for i in range(n):
        my_list.append(i)
        my_list.index(i)
    return my_list


@func_time
def dictionary_check(n):
    my_dict = dict()
    for i in range(n):
        my_dict[i] = i
        my_dict.get(i)
    return my_dict


print("Время работы списка:")
list_check(20000)
print("Время работы словаря:")
dictionary_check(20000)

# Время работы списка значительно медленнее, чем время работы словаря, за счет того что словарь реализован как
# хеш-таблица