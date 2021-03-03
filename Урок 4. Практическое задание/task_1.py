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
    return [i for i, el in enumerate(nums) if el % 2 == 0]

NUMS = [el for el in range(1000)]
print(timeit.timeit('func_1(NUMS)', setup='from_main_import func_1, NUMS', number=1000))

print(timeit.timeit('func_2(NUMS)', setup='from_main_import func_2, NUMS', number=1000))

'''
Пока смотришь вебинар все понятно, как только стоит самостоятельно, все плывем.
Сделал все как разбирали на 5 уроке всеравно ошибка.
По сложности и времени обработки цикла for и генераторного выражения enumerate понятно,
что цикл будет уступать генераторному выражению и по времени и по сложности'''







