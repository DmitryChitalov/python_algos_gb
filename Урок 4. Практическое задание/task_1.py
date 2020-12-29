"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""
import random
from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):  # тоже самое через выражение
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr


def func_3(nums):  # для количества добьем, но будет плохо
    new_arr = [i[0] for i in enumerate(nums) if i[1] % 2 == 0]
    return new_arr


def func_4(nums):  # кажется я придумал самый долгий способ для этой задачи...
    num_nums = enumerate(nums)
    new_arr = [i[0] for i in list(filter(lambda x: x[1] % 2 == 0, num_nums))]
    return new_arr


if __name__ == '__main__':
    my_nums = [random.randint(1, 1000) for i in range(100)]
    # print(func_1(my_nums))
    print(timeit("func_1(my_nums)", setup="from __main__ import func_1, my_nums", number=10000))
    # print(func_2(my_nums))
    print(timeit("func_2(my_nums)", setup="from __main__ import func_2, my_nums", number=10000))
    # print(func_3(my_nums))
    print(timeit("func_3(my_nums)", setup="from __main__ import func_3, my_nums", number=10000))
    # print(func_4(my_nums))
    print(timeit("func_4(my_nums)", setup="from __main__ import func_4, my_nums", number=10000))

"""
0.08471609999999999
0.0709262
0.09563930000000001
0.17466719999999997

вариант с нумерацией изначально был плохой идеей, но я хотел использовать фильтры, думал так будет быстрее.
в итоге вторая функция с генераторным выражением оказалась быстрее всех в замерах. Сложность там таже что и в первом 
O(n), но за счет использования генераторного выражения повышается скорость.
"""
