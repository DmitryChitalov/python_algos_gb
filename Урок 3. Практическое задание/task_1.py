"""
Задание 1.

Докажите, что словари обрабатываются быстрее, чем списки.

Реализуйте две функции, в первой нужно заполнить элементами список, во второй-словарь
Сделайте замеры времени выполнения каждой из функций

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""


import time


def time_test_func(func):
    def inner_func(*args, **kwargs):
        start_time = time.time()
        func(args[0])
        end_time = time.time()
        print(f' time of working function : {end_time - start_time}')
    return inner_func

@time_test_func
def test_func_list(el):
    test_list = []
    for i in range(el):
        test_list.append(i)
    return test_list

@time_test_func
def test_func_dict(el):
    test_dict = {}
    for i in range(el):
        test_dict[i] = i
    return test_dict

print(f'Program "Test time of filling a list or dictionary"')
fill_max_el = 1000000
print(f' 1. Filling random LIST with {fill_max_el} elements')
test_func_list(1000000)
print(f' 2. Filling random DICTIONARY with {fill_max_el} elements')
test_func_dict(1000000)
