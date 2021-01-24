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

def the_list(elems):
    completed_list = []
    start = time.time()
    for i in range(elems):
        completed_list.append(i)
    end = time.time()
    delta_time = f'Время выполнения: {end - start}'
    return completed_list, delta_time

def the_dict(elems):
    completed_dict = {}
    start = time.time()
    for i in range(elems):
        completed_dict[i] = i+1
    end = time.time()
    delta_time = f'Время выполнения: {end - start}'
    return completed_dict, delta_time


print(the_list(10))
print(the_dict(10))