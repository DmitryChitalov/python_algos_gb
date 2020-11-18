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

print('1 вариант')

print(timeit('''
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr
'''))

print(timeit('''
def func_2(nums):
    new_arr = []
    for el in nums:
        if el % 2 == 0:
            new_arr.append(nums.index(el))
    return new_arr
'''))

# убрали лишний перебор массива
print('2 вариант')

def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

res_1 = func_1([0, 1, 2, 3, 4])


def func_2(nums):
    new_arr = []
    for el in nums:
        if el % 2 == 0:
            new_arr.append(nums.index(el))
    return new_arr

res_2 = func_2([0, 1, 2, 3, 4])


print(
    timeit(
        "func_1([0, 1, 2, 3, 4])",
        setup='from __main__ import func_1',
        number=10000))

print(
    timeit(
        "func_2([0, 1, 2, 3, 4])",
        setup='from __main__ import func_2',
        number=10000))

print('3 вариант')
def func_3(nums):
    return [i for i, el in enumerate(nums) if el % 2 == 0]

nums = [el for el in range(5)]

print(
    timeit(
        "func_3(nums)",
        setup="from __main__ import func_3, nums",
        number=10000))

# выполняется быстрее генератор, чем перебор в цикле for, но 2 вариант тоже достаточно быстро выполняется