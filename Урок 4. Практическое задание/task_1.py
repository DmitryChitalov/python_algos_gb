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


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

a = [1, 2, 3, 4, 56, 342, 2134, 4143]

print(func_1(a))
print(timeit(stmt="func_1(a)", setup='from __main__ import func_1, a', number=100000))



def func_2(num):
    return [i for i in range(len(num)) if not num[i] % 2]

b = [1, 2, 3, 4, 56, 342, 2134, 4143]

print(func_2(b))
print(timeit(stmt="func_2(b)", setup='from __main__ import func_2, b', number=100000))


# каждый раз показывает разные результаты, то включение списков работает немного быстре, то цикл for!


def memorize(func):
    def wrapper(nums, new_set=set(), i=0, memory={}):
        result = memory.get(i)
        if result == None:
            result = func(nums, new_set, i)
            memory[i] = result
        return result

    return wrapper


@memorize
def func_3(nums, new_set=set(), i=0):
    if i != len(nums):
        if nums[i] % 2 == 0:
            new_set.add(nums.index(nums[i]))
        return func_3(nums, new_set, i + 1)
    else:
        return new_set

c = [1, 2, 3, 4, 56, 342, 2134, 4143]

print(func_3(c))
print(timeit('func_3(c)', setup='from __main__ import func_3, c', number=10000))

#рекурсия и мемоизация показывает значительное ускорение выполнения