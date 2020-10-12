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

from time import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        print(f'Время выполнения {time() - start}')
        return result

    return wrapper


@timer
def list_append():
    my_list = []
    for i in range(1000):
        my_list.append(i)
    print(my_list)


@timer
def dict_append():
    my_dict = {}
    for i in range(1000):
        my_dict[i] = i
    print(my_dict)


list_append()  # Время выполнения 0.001999378204345703
dict_append()  # Время выполнения 0.001998424530029297

# Словарь обрабатывается немного быстрее.