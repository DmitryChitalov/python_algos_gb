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
from random import randint


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


if __name__ == '__main__':
    lst = [randint(0, 1000) for _ in range(1000)]
    print(lst)
    print(func_1(lst))
    print(func_2(lst))
    print(timeit("func_1(lst)", "from __main__ import func_1, lst", number=1000))
    print(timeit("func_2(lst)", "from __main__ import func_2, lst", number=1000))


"""
Была написана функция func_2 создающая список при помощи генератора.
Создание списка через генератор являются самым быстрым стандартным способом для создания заполненного списка. 
В то числе за счет не использования метода append.
Быстрее только создание через []*1000, но в этом случае создается список с пустыми значениями.
"""