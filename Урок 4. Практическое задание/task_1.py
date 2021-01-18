"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""

from timeit import Timer, timeit, repeat, default_timer


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


foo = [i for i in range(10)]

t1 = Timer("func_1(foo)", "from __main__ import func_1, foo")
print(t1.timeit(number=1000))
print(func_1(foo))


def func_2(nums):
    new_arr = list(filter(lambda x: x % 2 == 0, nums))
    return new_arr


print(timeit("func_2(foo)", "from __main__ import func_2, foo", number=1000))
print(func_2(foo))


def func_3(nums):
    new_arr = [x for x in nums if x % 2 == 0]
    return new_arr


print(repeat("func_3(foo)", "from __main__ import func_3, foo", default_timer, 3, 1000))
print(func_3(foo))


"""
Применил встроенные функции с lambda-выражением и list comprehension.
Быстрее всех отработала функция с использованием list comprehension 
"""
print(0 % 10, 6 // 10, )