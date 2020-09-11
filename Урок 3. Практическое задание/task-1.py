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


def time_test(f):
    def body_function(*arguments):
        beginning = time.time()
        f(arguments[0])
        print(time.time() - beginning)
    return body_function


@time_test
def my_list(n):
    list_one = []
    for i in range(n):
        list_one.append(i)
        list_one.index(i)
    return list_one


@time_test
def my_dict(n):
    dict_one = dict()
    for i in range(n):
        dict_one[i] = i
        dict_one.get(i)
    return dict_one


my_list(10000)
my_dict(10000)
