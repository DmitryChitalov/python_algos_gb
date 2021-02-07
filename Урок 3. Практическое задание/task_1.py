"""
Задание 1.

Реализуйте заполнение списка и словаря, сделайте замеры и сделайте выводы, обоснуйте результат.
Сделайте несколько операций с каждым из объектов, сделайте замеры и сделайте выводы, обоснуйте результат.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""

from time import time


def timer_decorator(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f"Время выполнения : {t2 - t1}")
        return result

    return wrapper


@timer_decorator
def fill_list(lenght):
    ret_list = []
    for i in range(lenght):
        ret_list.append(i)
    return ret_list


@timer_decorator
def fill_dict(lenght):
    ret_dict = {}
    for i in range(lenght):
        ret_dict[i] = i
    return ret_dict


@timer_decorator
def get_from_list_value(input_list):
    for i in input_list:
        if i == 40000:
            return i


@timer_decorator
def get_from_list_key(input_list):
    return input_list[40000]


@timer_decorator
def get_from_dict_key(input_dict):
    return input_dict[40000]


@timer_decorator
def get_from_dict_value(input_dict):
    for i in input_dict.values():
        if i == 40000:
            return i


print("Заполнение списка:")
list1 = fill_list(100000)
list2 = fill_list(1000000)
print("Заполнение словаря:")
dict1 = fill_dict(100000)
dict2 = fill_dict(1000000)
# Вемя заполнения словаря больше т.к. необходимо рассчитывать хешь для индекса.

print(f"Список по ключу: ")
get_from_list_key(list1)
get_from_list_key(list2)
print("Словарь по ключу:")
get_from_dict_key(dict1)
get_from_dict_key(dict2)
# Поиск по ключу должен работать быстро т.к. использует хешь,
# а вот по значению медленно т.к. нужно перебирать все значения.
print("Список по значению:")
get_from_list_value(list1)
get_from_list_value(list2)
print("Словарь по значению:")
get_from_dict_value(dict1)
get_from_dict_value(dict2)
