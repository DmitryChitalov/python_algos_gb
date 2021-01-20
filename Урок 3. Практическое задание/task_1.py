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


def benchmark(func):
    def wrapper():
        start = time.time()
        test = func()
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end - start))
        return test, end - start

    return wrapper


@benchmark
def list_insert():
    my_list = []
    for i in range(9000):
        my_list.append(i)
    return my_list


@benchmark
def dict_insert():
    my_dict = {}
    for i, j in enumerate(range(0, 1000)):
        my_dict[i] = j
    return my_dict


x, list_time = list_insert()
my_test_dict, dict_time = dict_insert()


@benchmark
def list_retype():
    for y in x:
        x[int(y)] = str(y * 10)
    return x


@benchmark
def dict_retype():
    for key, value in my_test_dict.items():
        my_test_dict[key] = str(value * 2)
    return my_test_dict


list_retype()
dict_retype()
