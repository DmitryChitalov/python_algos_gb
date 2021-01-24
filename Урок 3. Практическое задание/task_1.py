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


def time_it(func):
    def chek_time(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        print(time.time() - start_time)

    return chek_time


@time_it
def create_list(n):
    # start_time = time.time()
    my_list = [i for i in range(n)]
    # print(time.time() - start_time)
    return my_list


@time_it
def create_dict(n):
    # start_time = time.time()
    my_dict = {i: i * i for i in range(n)}
    # print(time.time() - start_time)
    return my_dict


n = 100000
create_list(n)
create_dict(n)

"""
0.008816003799438477 - список
0.036396026611328125 - словарь
Список заполняется быстрее, чем словарь, потому что количество операций для заполнения меньше
"""
