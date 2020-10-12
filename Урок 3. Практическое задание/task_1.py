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
def timer_func(func):
    def time_res(arg, *kwargs):
        start = time.time()
        func(arg, *kwargs)
        end = time.time()
        print(end - start)
    return time_res

@timer_func
def list_gen(count_elem):
    my_list = []
    for i in range(count_elem):
        my_list.append(i)
    return print(my_list)

@timer_func
def dict_gen(elem, value):
    import random
    my_dict = {}
    for i in range(elem):
        my_dict[i] = random.randint(0, value)
    return print(my_dict)

list_gen(10000)

dict_gen(10000, 10000)
'''
Честно говоря плохо понял задание...

Но если все сделал правильно, то список генерируется быстрее словаря.
'''