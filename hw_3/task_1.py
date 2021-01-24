"""
Задание 1.

Реализуйте свои пользовательские функции, в которых реализуйте:

a) заполнение списка и словаря программно,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!
"""
import time


def get_time(func):
    def wrapper(*args, **kwargs):
        begin = time.time()
        func(*args, **kwargs)
        return print(time.time() - begin)
    return wrapper


@get_time
def list_append(n):
    new_list = []
    for i in range(n):
        new_list.append(i)
    return new_list


@get_time
def dict_append(n):
    new_dict = {}
    for i in range(n):
        new_dict[i] = i
    return new_dict


list_append(100000)
dict_append(100000)
