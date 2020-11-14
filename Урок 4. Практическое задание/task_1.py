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

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


print(timeit('func_1(nums)', setup='from __main__ import func_1, nums', number=10000))


# 0.0254 - 0.0269 секунд


def memorize(func):
    def wrapper(nums, new_set=set(), i=0, memory={}):
        result = memory.get(i)
        if result == None:
            result = func(nums, new_set, i)
            memory[i] = result
        return result

    return wrapper


@memorize
def func_2(nums, new_set=set(), i=0):
    if i != len(nums):
        if nums[i] % 2 == 0:
            new_set.add(nums.index(nums[i]))
        return func_2(nums, new_set, i + 1)
    else:
        return new_set


print(timeit('func_2(nums)', setup='from __main__ import func_2, nums', number=10000))

# 0.00318 - 0.00425 секунд

'''
Изначально курс моего решения был направлен на рекурсию с мемоизацией.
Просто применив к начальному коду указанные решения, прибавки времени не вышло.
Изменив формат набора индексов на множество, убрав цикл for и добавив метод .index для списка,
вместе с рекурсией и мемоизацией удалось получить значительное ускорение выполнения.   
'''
