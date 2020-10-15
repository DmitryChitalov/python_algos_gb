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


def check_time(func):
    def wrapper(num):
        start = time()
        return_value = func(num)
        delta = time()-start
        print(f'Время выполнения: {delta} секунд.')
        return return_value

    return wrapper


@check_time
def create_lst(num: int) -> list:
    lst = [i for i in range(num)]
    return lst


@check_time
def create_dct(num: int) -> dict:
    dct = {i: i * 2 for i in range(num)}
    return dct


lst = create_lst(10)
dct = create_dct(10)

print(lst, dct)


@check_time
def append(lst):
    lst.append(8900)
    return lst


print(append(lst))


@check_time
def pop(lst):
    lst.pop()
    return lst


print(pop(lst))


@check_time
def reverse(lst):
    lst.reverse()
    return lst


print(reverse(lst))


@check_time
def copy(lst):
    lst2 = lst.copy()
    return lst2


print(copy(lst))


@check_time
def pop_dct(dct):
    dct = dct.pop(4)
    return dct


print(pop_dct(dct))


@check_time
def copy_dct(dct):
    dct = dct.copy()
    return dct


print(copy_dct(dct))


@check_time
def values_dct(dct):
    dct = dct.values()
    return dct


print(values_dct(dct))

# Вывод: работа со списками происходит быстрее
