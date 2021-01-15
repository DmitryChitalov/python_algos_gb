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

number = range(1000)


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    new_arr = [i for i in range(len(nums)) if i % 2 == 0]
    return new_arr


def func_3(nums):
    new_arr = [nums, lambda numbers: numbers % 2 == 0]
    return new_arr


print(timeit('func_1(number)', setup='from __main__ import func_1, number', number=10000))
print(timeit('func_2(number)', setup='from __main__ import func_2, number', number=10000))
print(timeit('func_3(number)', setup='from __main__ import func_3, number', number=10000))
"""
Я сделал еще две функции, которые так же как и первая возвращаю список четных чисел. Сделал замеры времени всех функций.
Выяснил, что генераторное выражение с циклом быстрее отрабатывает, чем перебор по индексу, но с лямбда функцией работает
еще быстрее, так как нет цикла for.
1.9520012660000001
0.6214358960000002
0.001821301999999747
"""