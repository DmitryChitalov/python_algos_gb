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


list1 = [i for i in range(100)]
list2 = [i for i in range(1000)]
list3 = [i for i in range(10000)]


print(timeit("func_1(list1)", globals=globals(), number=1000)) # -> 0.015368
print(timeit("func_1(list2)", globals=globals(), number=1000)) # -> 0.1579729
print(timeit("func_1(list3)", globals=globals(), number=1000)) # -> 1.1616849

print(timeit("func_2(list1)", globals=globals(), number=1000)) # -> 0.007228699999999977
print(timeit("func_2(list2)", globals=globals(), number=1000)) # -> 0.08669489999999991
print(timeit("func_2(list3)", globals=globals(), number=1000)) # -> 1.0194534999999998

"""
Списковые выражения быстрее цикла, хотя были сомнения, так как пришлось использовать enumerate 
"""

