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


def froze(function):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        end = time.time()
        return end - start, result
    return wrapper


my_list_1 = [el for el in range(10000)]


@froze
def filling_dict(lst):
    d = {}
    for el in lst:
        key = str(el+1)
        d[key] = el
    return d


@froze
def filling_lst(n):
    my_list = []
    for el in range(n):
        my_list.append(el)
    return my_list


# на выводе видно, что количество времени заполнения словаря больше, чем списка
print(filling_lst(10000))
print(filling_dict(my_list_1))

