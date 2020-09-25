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
    new_arr = [i for i in nums if i % 2 == 0]
    return new_arr


if __name__ == '__main__':
    n = [i for i in range(99)]
    # print(func_1(n))
    # print(func_2(n))
    
    print(timeit.timeit("func_1(n)", setup="from __main__ import func_1, n", number=10000))
    print(timeit.timeit("func_2(n)", setup="from __main__ import func_2, n", number=10000))

"""
Я решил что эту задачу будет эффективней сделать через генератор
при расчете времени работы скрипта, подтвердилось что решение через генератор примерно в 2 раза быстрей
Так же возможно лучше читается код
"""
