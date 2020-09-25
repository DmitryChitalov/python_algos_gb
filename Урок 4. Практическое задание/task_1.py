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


def my_func(nums):
    new_arr = [i for i in nums if i % 2 == 0]
    return new_arr


if __name__ == '__main__':
    n = [i for i in range(100)]


print(timeit("func_1(range(100))", setup="from __main__ import func_1", number=1000))
print(timeit("my_func(range(100))", setup="from __main__ import my_func", number=1000))


# Оптимизировала решение с помощью генератора, время выполнения кода
# уменьшилось с 0.03 до 0.01