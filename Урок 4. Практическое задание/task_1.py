"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

"""Решение через рекурсию"""
def func_2(nums,counter, new_arr):
    if counter != len(nums):
        if nums[counter] % 2 == 0:
            new_arr.append(nums[counter])
            counter = counter + 1
            func_2(nums, counter, new_arr)
        else:
            counter = counter + 1
            func_2(nums, counter, new_arr)
    else:
        print(new_arr)


new_arr=[]
counter = 0
nums = [el for el in range(995)]

"""Проблемы решения:
Максимально допустимая возможность вызова функции самой себя. Из-за этого пришлось сделать range в nums 995.
Соответственно, посчитать модулем timeit тоже не выйдет, так как функция снова вызывает саму себя, что превышает значение
максимального вызова функции. Кроме того, выносить за функцию нужно еще 2 аргумента"""

"""Решение через генераторное выражение"""
def func_3(nums):
    return [i for i, el in enumerate(nums) if el % 2 == 0]

print(timeit.timeit("func_1(nums)",
                    setup="from __main__ import func_1, nums",
                    number=1000))

print(timeit.timeit("func_3(nums)",
                    setup="from __main__ import func_3, nums",
                    number=1000))






