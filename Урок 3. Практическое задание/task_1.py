"""
Задание 1.

Докажите, что словари обрабатываются быстрее, чем списки.

Реализуйте две функции, в первой нужно заполнить элементами список, во второй-словарь
Сделайте замеры времени выполнения каждой из функций

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""


import time


def time_dec(func):

    def wrapper(*args):
        start = time.time()
        func(*args)
        end = time.time()
        print(f'Время выполнения: {func} {end - start} секунд.')
    return wrapper


@time_dec
def new_list(elems):
    my_list = [el for el in range(elems)]
    for i in range(elems):
        my_list.index(i)
    return my_list


@time_dec
def new_dict(elems):
    my_dict = {el: el for el in range(elems)}
    for i in range(elems):
        my_dict.get(i)
    return my_dict


new_list(10000)
new_dict(10000)
