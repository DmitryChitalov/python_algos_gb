"""
Задание 1.

Реализуйте заполнение списка и словаря, сделайте замеры и сделайте выводы,
обоснуйте результат.  Сделайте несколько операций с каждым из объектов,
сделайте замеры и сделайте выводы, обоснуйте результат.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""


import time
import random


def timing(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        wrapped = func(*args, **kwargs)
        stop = time.time()
        print(f'Elapsed: {start - stop}')
        return wrapped
    return wrapper


@timing
def list_fill(n: int):
    """Filling list with n random integers"""
    result = [random.randint(0, 1000) for i in range(n)]
    return result


@timing
def dict_fill(n: int):
    """Filling dict with n random integers"""
    result = {i: random.randint(0, 1000) for i in range(n)}
    return result


@timing
def process(obj, n):
    """Processing some operation to obj"""
    print(obj[random.randint(0, n)])
    del(obj[random.randint(0, n)])
    obj[random.randint(0, n)] = 42


if __name__ == '__main__':

    length = 1000000
    test_list = list_fill(length)  # Elapsed: -1.1190168857574463
    test_dict = dict_fill(length)  # Elapsed: -1.237342357635498
# Словарь заполняется дольше, считаю это связано с необходиомстью
# вычисления хэша для каждого ключа при создании

    process(test_list, length)  # -0.0012640953063964844
    process(test_dict, length)  # -1.5020370483398438e-05
# Все операции со словарем происходят значительно быстрее, потому что
# словарь это хэш-таблица и имеет временную сложность О(1) для этих
# операций
