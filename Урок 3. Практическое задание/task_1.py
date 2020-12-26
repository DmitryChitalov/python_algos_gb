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


def time_of_operation(function):
    def wrapper(*args):
        start = time.perf_counter()
        function(args[0])
        print(time.perf_counter() - start)
    return wrapper


@time_of_operation
def list_for_in(num):
    user_list = []
    for el in range(num):
        user_list.append(el)
    return user_list


print(f'Заполнение списка через цикл for in составило')
list_for_in(1000000)


@time_of_operation
def list_generator(num):
    user_list = [el for el in range(num)]
    return user_list


print('Заполнение списка при помощи гененратора составило')
list_generator(1000000)


@time_of_operation
def dict_for_in(num):
    user_dict = {}
    for el in range(num):
        user_dict[el] = el
    return user_dict


print('Заполнение словаря через for in составило')
dict_for_in(1000000)


@time_of_operation
def dict_for_in(num):
    user_dict = {}
    for el, els in enumerate(range(num)):
        user_dict[el] = els
    return user_dict


print('Заполнение словаря через for in с функцийе enumerate составило')
dict_for_in(1000000)


@time_of_operation
def dict_generator(num):
    user_dict = {el: el for el in range(num)}
    return user_dict


print('Заполнение словаря при помощи генератора составило')
dict_generator(1000000)


@time_of_operation
def dict_generator2(num):
    user_dict = {el: els for el, els in enumerate(range(num))}
    return user_dict


print('Заполнение словаря при помощи генератора с функцией enumerate составило')
dict_generator2(1000000)
