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


def my_first_decorator(my_func):
    def wrapper():
        start = time.time()
        z = my_func()
        end = time.time()
        print(f"Время заполнения: {end - start}")
        return z, end - start
    return wrapper


@my_first_decorator
def fill_list():
    my_list = []
    for i in range(10000):
        my_list.append(i)
    return my_list


x, list_time = fill_list()
print(x)


@my_first_decorator
def fill_dict():
    a = 0
    my_dict = {}
    while a <= 10000:
        my_dict[str(a)] = a
        a += 1
    return my_dict


y, dict_time = fill_dict()
print(y)


print(f"Разница в заполнении: {list_time - dict_time} сек. Отрицательное число значит, "
      f"что словарь заполняется дольше и наоборот")

@my_first_decorator
def list_operations():
    for i in x:
        x[int(i)] = str(i * 10)
    return x

new_list, list_operations_time = list_operations()
print(new_list, "\n", list_operations_time)


@my_first_decorator
def dict_operations():
    for key, value in y.items():
        y[key] = value * 10
    return y

new_dict, dict_operations_time = dict_operations()
print(new_dict, "\n", dict_operations_time)
print(f"Разница в заполнении: {list_operations_time - dict_operations_time} сек. Отрицательное число значит, "
      f"что словарь заполняется дольше и наоборот")


"""
Из примеров видно, что словарь из-за своей структуры заполняется дольше, зато операции 
производятся быстрее
"""