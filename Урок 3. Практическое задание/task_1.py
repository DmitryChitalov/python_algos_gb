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


def time_decor(function):
    def time_diff(*args):
        start = time.time()
        function(args[0])
        print(time.time() - start)
    return time_diff


@time_decor
def list_append(n):
    list_obj = []
    for i in range(n):
        list_obj.append(i)
        list_obj.index(i)
    return list_obj


@time_decor
def dict_add(n):
    dict_obj = dict()
    for i in range(n):
        dict_obj[i] = i
        dict_obj.get(i)
    return dict_obj


list_append(10000)
dict_add(10000)

# Списки заполняются элементами быстрее, чем словари
# Но получение элементов происходит в словарях быстрее, чем в списках
