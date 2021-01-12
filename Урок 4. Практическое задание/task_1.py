"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""
import cProfile
from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    new_arr = [i for i in range(len(nums)) if i % 2 == 0]
    return new_arr


num_list = [i for i in range(10000)]
print(timeit('func_1(num_list)', 'from __main__ import func_1, num_list', number=1000))
print(timeit('func_2(num_list)', 'from __main__ import func_2, num_list', number=1000))



"""
Сделал новую функцию, с генераторным выражением
При больших объемах массива, 1000000 значений, func_2 тратит времени, приблизительно на 20 секунд меньше

При маленьких объемах 10 >= значний func_1 и func_2 работают фактически одинакого

"""
