"""
Задание 1.

Реализуйте заполнение списка и словаря, сделайте замеры и сделайте выводы, обоснуйте результат.
Сделайте несколько операций с каждым из объектов, сделайте замеры и сделайте выводы, обоснуйте результат.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""

import random


def time_estimation_dec(func):
    import time

    def wrapper(*args, **kwargs):
        start = time.time()
        func_output = func(*args, **kwargs)
        end = time.time()
        print(f'Время выполнения функции {func.__name__}: {end - start} сек')
        return func_output
    return wrapper


@time_estimation_dec
def fill_list(in_list: list, *args):
    for val in args:
        in_list.append(val)


@time_estimation_dec
def fill_dict(in_dict: dict, *args, **kwargs):
    for key, val in args[0].items():
        in_dict[key] = val
    if kwargs:
        for key, val in kwargs.items():
            in_dict[key] = val


@time_estimation_dec
def pop_from_list(in_list: list, amount: int):
    # Делаем все обычным циклом чтоб быстрее, хотя хотел изначально рекурсией
    list_len = len(in_list)
    output_list = []
    while in_list and len(in_list) != (list_len - amount):
        output_list.append(in_list.pop())
    return output_list


@time_estimation_dec
def pop_from_dict(in_dict: dict, amount: int):
    dict_len = len(in_dict)
    output_dict = {}
    while in_dict and len(in_dict) != (dict_len - amount):
        x = in_dict.popitem()
        output_dict.update({x[0]: x[1]})
    return output_dict


list_of_rand_int = [random.randint(1, 100) for val in range(0, 100000)]

dict_of_rand_int = {}
for val in list_of_rand_int:
    dict_of_rand_int.update({val: val})

user_list = []
fill_list(user_list, *list_of_rand_int)
# Для случайного числа от 1 до 100
# Время выполнения функции fill_list: 0.023903846740722656 сек
# Для случайного числа от 1 до 10000
# Время выполнения функции fill_list: 0.03490257263183594 сек
# Для случайного числа от 1 до 1000000
# Время выполнения функции fill_list: 0.036936283111572266 сек

print(f'Элементы списка: {user_list}')

user_dict = {}
fill_dict(user_dict, dict_of_rand_int)
# Для случайного числа от 1 до 100
# Время выполнения функции fill_dict: 0.0 сек
# Для случайного числа от 1 до 10000
# Время выполнения функции fill_dict: 0.004987239837646484 сек
# Для случайного числа от 1 до 1000000
# Время выполнения функции fill_dict: 0.0408930778503418 сек

print(f'Элементы словаря: {user_dict}')


print(f'Элементы списка: {pop_from_list(user_list, 100000)}')
# Для случайного числа от 1 до 100
# Время выполнения функции pop_from_list: 0.05684924125671387 сек
# Для случайного числа от 1 до 10000
# Время выполнения функции pop_from_list: 0.06881213188171387 сек
# Для случайного числа от 1 до 1000000
# Время выполнения функции pop_from_list: 0.07084465026855469 сек

print(f'Элементы словаря: {pop_from_dict(user_dict, 100000)}')
# Для случайного числа от 1 до 100
# Время выполнения функции pop_from_dict: 0.0 сек
# Для случайного числа от 1 до 10000
# Время выполнения функции pop_from_dict: 0.02294158935546875 сек
# Для случайного числа от 1 до 1000000
# Время выполнения функции pop_from_dict: 0.14564299583435059 сек

# Вывод:
# Хранение информации ввиде хеш таблиц (словарей) существенно эффективнее если применяются правильные функции и
# правльная запись данных в эти таблицы. Из результатов задания видно, что при увеличени диапазона случайного числа, т.е
# с повышением вероятности уникальности числа - растет и время записи/копирования элементов из хеш таблицы. Это
# обоснованно тем, что при копировании словаря надо копировать несколько значений: его хеш (ключ) и само значение ключа.
# Точно это утверждать нельзя, так как для действия с таким количеством информации необходима глубокая оптимизация
# алгоритмов, но можно сделать вывод, что для записи/копирования большого количества информации списки - быстрее
# словарей.
