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


def func_2(obj: list) -> list:
    # Списковое включение работает быстрее, чем обычный цикл, к тому же мы избавились от доплнительного действия в виде
    # добавления элемента в список (append). Так же большую прибавку в скорости дает использование оператора not вместо
    # оператора сравнения.
    return [i for i in range(len(obj)) if not obj[i] % 2]


if __name__ == '__main__':
    a = [randint(1, 100) for i in range(100)]
    b = timeit('func_1(a)', number=100000, globals=globals())
    c = timeit('func_2(a)', number=100000, globals=globals())
    print(b)
    print(c)
