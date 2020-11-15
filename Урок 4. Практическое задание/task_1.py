"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""
from timeit import Timer

def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

# свое решение - через генераторное выражение,
# т.к выражение с итератором имеет меньшую сложность O(n log n) чем цикл O(n2)
def func_2(nums):
    my_lst =[i for i in range(len(nums)) if i % 2]
    return my_lst


t1 = Timer("func_1([1, 2, 5, 8, 9, 2])", "from __main__ import func_1")
print("cicle ", t1.timeit(number=1000), "milliseconds")


t2 = Timer("func_2([1, 2, 5, 8, 9, 2])", "from __main__ import func_2")
print("iterator ", t2.timeit(number=1000), "milliseconds")

