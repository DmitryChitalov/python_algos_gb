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

def time_f(function):
    def time_score(*args):
        start_time = time.time()
        function(args[0])
        print(time.time() - start_time)
    return time_score

@time_f
def list_f(n):
    list_obj = []
    for i in range(n):
        list_obj.append(i)
    return list_obj

@time_f
def dict_f(n):
    dict_obj = dict()
    for i in range(n):
        dict_obj[i] = i
    return dict_obj

list_f(10000000)
dict_f(10000000)

# Список заполняется дольше чем словарь