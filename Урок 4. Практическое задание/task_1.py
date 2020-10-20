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
##определяем nums
nums = [elem for elem in range(1000)]
#печатаем список
print(nums)


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

## делаем другую функцию
def func_2(nums):
    return [x for x in nums if not x%2]


##проверяем работу функции
print(func_1(nums))
print(func_2(nums))

##производим замеры
print(timeit.timeit("func_1(nums)", setup="from __main__ import func_1, nums", number=1000))
print(timeit.timeit("func_2(nums)", setup="from __main__ import func_2, nums", number=1000))


## первая функция медленнее из-за фора.
##Если список не очень большой, то разница не так бросается, но
##стоит его увеличить, разница по времени очевидна