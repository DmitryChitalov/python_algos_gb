"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""

from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


def func_3(nums_dict):
    new_arr = []
    for key, val in nums_dict.items():
        if val % 2 == 0:
            new_arr.append(key)
    return new_arr


nums = [0, 4, 4, 3, 3, 2]
nums_dict = {
    0: 0,
    1: 4,
    2: 4,
    3: 3,
    4: 3,
    5: 2
}

print(timeit("func_1(nums)", setup="from __main__ import func_1, nums", number=100000))
print(timeit("func_2(nums)", setup="from __main__ import func_2, nums", number=100000))
print(timeit("func_3(nums_dict)", setup="from __main__ import func_3, nums_dict", number=100000))

"""
Если данные хранить не в списке, а в словаре, где ключ - это индекс, а значение - это сам элемент массива,
то перебор у словаря будет быстрее, т.к. словарь, это хеш таблица, а перебор(доступ к элементам) по хешам
осуществляется быстрее, чем по индексам.
"""
