"""
Задание 1.

Реализуйте заполнение списка и словаря, сделайте замеры и сделайте выводы, обоснуйте результат.
Сделайте несколько операций с каждым из объектов, сделайте замеры и сделайте выводы, обоснуйте результат.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.

Заполнение словаря выполняется дольше, т.к. необходимо вычислять хэш
Получение элемента по ключу и удаление элемента по ключу в словаре выполняеся быстрее за счет хэш таблицы
"""
from time import time
from random import randint


def time_measure(func):
    def wrapped():
        start_val = time()
        func()
        end_val = time()
        print(f"Операция выполнялась: {end_val - start_val}")
        return

    return wrapped


@time_measure
def list_create():
    for i in range(n):
        item = randint(0, 100)
        var_list.append(item)


@time_measure
def dict_create():
    for i in range(n):
        item = randint(0, 100)
        var_dict[i] = item


@time_measure
def list_pop():
    for i in range(n):
        item = var_list.pop(0)


@time_measure
def dict_pop():
    for i in range(n):
        item = var_dict.pop(i)


@time_measure
def list_del():
    for i in range(n):
        del var_list[0]


@time_measure
def dict_del():
    for i in range(n):
        del var_dict[i]


n = 100000
var_list = []
var_dict = {}

print(f"Заполнение списка")
list_create()
print()
print(f"Заполнение словаря")
dict_create()
print("------------------------------\n\r\n\r")

print(f"Получение элементов списка")
list_pop()
print()
print(f"Получение элементов словаря")
dict_pop()
print("------------------------------\n\r\n\r")

print(f"Заполнение списка")
list_create()
print()
print(f"Заполнение словаря")
dict_create()
print("------------------------------\n\r\n\r")

print(f"Удаление элементов списка")
list_del()
print()
print(f"Удаление элементов словаря")
dict_del()
print("------------------------------\n\r\n\r")
