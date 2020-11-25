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
from RandomWordGenerator import RandomWord
from random import randint


def benchmark(func):
    def time_estimate(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        worktime = end - start
        return return_value, worktime

    return time_estimate


@benchmark
def filldict(in_arg):
    pass
    my_dict = dict()
    for el in in_arg:
        my_dict[el] = el


@benchmark
def filllist(in_arg):
    pass
    my_list = list()
    for el in in_arg:
        my_list.append(el)
    return my_list


def generate_text_list(range_arg):
    pass
    res_list = list()
    for _ in range_arg:
        word = ""
        word_length = randint(3, 10)
        for _ in range(word_length):
            rand_char = chr(randint(32, 122))
            word += rand_char
        res_list.append(word)
    return res_list


def print_proof(dict_time, list_time, test_type):
    if list_time < dict_time:
        print(f"При выполнении теста заполнения {test_type}, списки формируются быстрее, чем словари")
    else:
        print(f"При выполнении теста заполнения {test_type}, словари формируются быстрее, чем списки")


def get_digit_fill_time(test_range, max_elements):
    pass

    my_dict, dict_filltime = filldict(test_range)
    my_list, list_filltime = filllist(test_range)
    print(f"Список из чисел на {max_elements} элементов сформирован за {list_filltime}")
    print(f"Словарь из чисел на {max_elements} элементов сформирован за {dict_filltime}")

    return dict_filltime, list_filltime


def get_text_fill_time(text_list, max_elements):
    pass

    my_dict_text, dict_filltime = filldict(text_list)
    my_list_text, list_filltime = filldict(text_list)

    print(f"Список из символов на {max_elements} элементов сформирован за {list_filltime}")
    print(f"Словарь из символов на {max_elements} элементов сформирован за {dict_filltime}")

    return dict_filltime, list_filltime


def main():
    pass
    try:
        max_elements = 10000000
        test_range = range(max_elements)
        text_list = generate_text_list(test_range)

        digit_fill_time = get_digit_fill_time(test_range, max_elements)
        text_fill_time = get_text_fill_time(text_list, max_elements)

        print_proof(digit_fill_time[0], digit_fill_time[1], "числами")
        print_proof(text_fill_time[0], text_fill_time[1], "символами")

        print("Программа завершена!")
    except Exception as ex:
        print(f"Fatal error: {ex}")


if __name__ == "__main__":
    main()

"""
Список из чисел на 10000000 элементов сформирован за 0.511406660079956
Словарь из чисел на 10000000 элементов сформирован за 0.8402631282806396
Список из символов на 10000000 элементов сформирован за 3.0390465259552
Словарь из символов на 10000000 элементов сформирован за 2.751788854598999
При выполнении теста заполнения числами, списки формируются быстрее, чем словари
При выполнении теста заполнения символами, словари формируются быстрее, чем списки
"""