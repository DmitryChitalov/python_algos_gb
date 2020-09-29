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

nums = [elem for elem in range(10)]
print(nums)


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [i for i, elem in enumerate(nums) if elem % 2 == 0]


print(func_1(nums))
print(func_2(nums))
print(timeit.timeit("func_1(nums)", setup="from __main__ import func_1, nums", number=1000))
print(timeit.timeit("func_2(nums)", setup="from __main__ import func_2, nums", number=1000))


"""
2 вариант по времени выполнения является более выигрышным. цикл for усложняют 1 вариант функции
"""