"""
Задание 1.

Реализуйте заполнение списка и словаря, сделайте замеры и сделайте выводы, обоснуйте результат.
Сделайте несколько операций с каждым из объектов, сделайте замеры и сделайте выводы, обоснуйте результат.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""

import functools
import time


def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Функция {func.__name__!r} выполняется за {run_time:.4f} секунд")
        return value
    return wrapper_timer


@timer
def populate_list(num_elements):
    test_list = [element for element in range(num_elements)]
    return test_list


@timer
def populate_dict(num_elements):
    test_dict = {k: v for k, v in enumerate(range(num_elements), start=0)}
    return test_dict


@timer
def search_list(input_list, element):
    print(f'индекс элемента {element}: {test_list.index(element)}')


@timer
def search_dict(input_dict, key):
    print(f'значение элемента с ключом {key}: {input_dict.get(key)}')


test_list = populate_list(100000)
test_dict = populate_dict(100000)
#  словарь заполняется медленнее, чем список, за счет использования хеш-таблиц, формирование которых занимает время.

search_list(test_list, 90000)
search_dict(test_dict, 90000)
'''
Поиск по индексу в словаре происходит существенно быстрее за счет механизма хеш-таблиц.
Хеш-таблицы позволяют снизить сложность операции поиска по ключу в словаре до O(1), 
в то время как в списке сложность поиска по индексу - O(N).
'''
