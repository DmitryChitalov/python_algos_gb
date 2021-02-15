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


def dict_append(q):
    if q == 0:
        return
    else:
        MY_DICT['new' + str(q)] = q
        return dict_append(q - 1)


def timing(func):
    def the_wrapper_around_the_original_function():
        start_val1 = time.time()
        func()
        end_val1 = time.time()
        print(f'время создания {func.__name__}: {end_val1 - start_val1}')

    return the_wrapper_around_the_original_function


@timing
def my_list_new():
    MY_LIST = [i for i in range(1, 10 ** 7)]
    return


@timing
def my_dict_new():
    MY_DICT = {x: x for x in range(1, 10 ** 7)}
    return


def list_append(q):
    if q == 0:
        return
    else:
        MY_LIST.append(q)
        return list_append(q - 1)


MY_LIST = []
MY_DICT = {}

my_list_new()
my_dict_new()

print()

start_val = time.time()
list_append(990)
end_val = time.time()
print("время добавления в список: ", end_val - start_val)

start_val = time.time()
dict_append(990)
end_val = time.time()
print("время добавления в словарь: ", end_val - start_val)

'''
 Запись (создание) у словаря будет медленнее ,т.к. надо посчитать хэш
 Добавление или обновление данных у словаря будет быстрее, т.к. словарь использует хеш
'''
