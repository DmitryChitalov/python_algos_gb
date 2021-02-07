"""
Задание 1.

Реализуйте заполнение списка и словаря, сделайте замеры и сделайте выводы, обоснуйте результат.
Сделайте несколько операций с каждым из объектов, сделайте замеры и сделайте выводы, обоснуйте результат.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""
from time import process_time


def benchmark(func):
    def wrapper(*args, **kwargs):
        t = process_time()
        res = func(*args, **kwargs)
        print(func.__name__, process_time() - t)
        return res
    return wrapper


my_list = [el for el in range(1, 10000000)]
my_dict = {el: el for el in range(1, 10000000)}


@benchmark
def multi_list(a):
    print('для списка: ')
    return [el * 2 for el in a]


@benchmark
def multi_dict(a):
    print('и для словаря: ')
    return {key: value * 2 for key, value in a.items()}


@benchmark
def div_list(a):
    print('для списка: ')
    return [el // 2 for el in a]


@benchmark
def div_dict(a):
    print('и для словаря: ')
    return {key: value // 2 for key, value in a.items()}


print('Попробуем функцию умножения...')
multi_list(my_list)
multi_dict(my_dict)
print('Попробуем функцию деления без остатка...')
div_list(my_list)
div_dict(my_dict)

print('Во всех случаях операции со словарем проходят дольше!')
