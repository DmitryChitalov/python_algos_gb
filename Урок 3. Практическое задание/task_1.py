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
        time = process_time()
        result = func(*args, **kwargs)
        print(func.__name__, process_time() - time)
        return result
    return wrapper


range_list = [element for element in range(1, 10000000)]
range_dict = {element: element for element in range(1, 10000000)}


@benchmark
def multi_list(input_list):
    print('для списка: ')
    return [element * 2 for element in input_list]


@benchmark
def multi_dict(input_dict):
    print('и для словаря: ')
    return {key: value * 2 for key, value in input_dict.items()}


@benchmark
def div_list(input_list):
    print('для списка: ')
    return [element // 2 for element in input_list]


@benchmark
def div_dict(input_dict):
    print('и для словаря: ')
    return {key: value // 2 for key, value in input_dict.items()}


print('Умножение...')
multi_list(range_list)
multi_dict(range_dict)
print('Деления без остатка...')
div_list(range_list)
div_dict(range_dict)

print('Во всех случаях операции со словарем проходят дольше!')