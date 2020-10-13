"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""

# from timeit import timeit
import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if (int(nums[i]) % 2) == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    new_arr = [i for i in range(len(nums)) if int(nums[i]) % 2 == 0]
    return new_arr


if __name__ == '__main__':
    nums = "1234567890"

    print(timeit.timeit("func_1(nums)", setup="from __main__ import func_1, nums", number=10000))
    print(timeit.timeit("func_2(nums)", setup="from __main__ import func_2, nums", number=10000))
"""
    В качестве оптимизации: заменил цикл генераторным выжением
    При значении number=1000 - разница практически не заметна, но при увеличении number=10000
    герераторное выражение стабильно быстрее 
"""