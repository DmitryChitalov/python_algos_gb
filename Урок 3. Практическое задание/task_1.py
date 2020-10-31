"""
Задание 1.

Реализуйте заполнение списка и словаря, сделайте замеры и сделайте выводы, обоснуйте результат.
Сделайте несколько операций с каждым из объектов, сделайте замеры и сделайте выводы, обоснуйте результат.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""

from random import randint


def time_fix(measured_function):
    import time

    def wrapper():
        time_start = time.perf_counter()
        result = measured_function
        timer = time.perf_counter() - time_start
        print(f'Функция {measured_function.__name__} отработала за {timer} секунд')
        return result

    return wrapper()


@time_fix
def list_fill():
    my_list = []
    for i in range(10000):
        my_list.append(randint(0, 100))


@time_fix
def dict_fill():
    my_dict = {}
    for i in range(10000):
        my_dict[i] = randint(0, 100)


list_fill()
dict_fill()
