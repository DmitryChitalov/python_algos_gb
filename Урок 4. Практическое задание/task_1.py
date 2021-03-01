"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""
from random import randint
from timeit import Timer, timeit



def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


# используем list comprehensions:
def func_2(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]

# чисто для себя...
def check_by_timer():
    print("Замер с помощью инструмента Timer ")
    t1 = Timer("func_1(my_list)", globals=globals())
    print("func_1", t1.timeit(10000), "seconds")  # number=100000

    t2 = Timer("func_2(my_list)", globals=globals())
    print("func_2", t2.timeit(10000), "seconds")  # number=100000


def check_by_timeit():
    print("Замер с помощью инструмента timeit ")
    print(f"func_1 {timeit('func_1(my_list)', globals=globals(), number=10000)} seconds")
    print(f"func_2 {timeit('func_2(my_list)', globals=globals(), number=10000)} seconds")


my_list = [randint(-1000, 1001) for i in range(1000)]
check_by_timer()
check_by_timeit()
