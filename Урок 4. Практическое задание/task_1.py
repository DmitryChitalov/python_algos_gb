"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""
import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    result = [i for i, el in enumerate(nums) if el % 2 == 0]
    return result


nums = [el for el in range(5000)]

#t1 = timeit.Timer("func_1([el for el in range(5000)])", "from __main__ import func_1")
#t1.timeit(number=1000),"seconds")

t1 = timeit.timeit("func_1(nums)", globals=globals(), number=1000)
print(t1)

t2 = timeit.timeit("func_2(nums)", globals=globals(), number=1000)
print(t2)

# списковые включения работают быстрее