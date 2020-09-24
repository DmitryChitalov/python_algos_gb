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
    print(new_arr)
    return new_arr

def func_1_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    # print(new_arr)
    return new_arr

def func_2(nums):
    new_arr = [item for item in range(len(nums)) if nums[item] % 2 == 0]
    return new_arr

def func_2_2(nums):
    new_arr = [item for item in range(0,len(nums),2)]
    return new_arr

def func_3(nums):
    new_arr=list(range(0, len(nums), 2))
    return new_arr


t1 = Timer("func_1([0,1,2,3,4,5,6,7,8,9])", "from __main__ import func_1")
print("Func_1 ", t1.timeit(number=10000), "milliseconds")
t1_1 = Timer("func_1_1([0,1,2,3,4,5,6,7,8,9])", "from __main__ import func_1_1")
print("Func_1_1 ", t1_1.timeit(number=10000), "milliseconds")
t2 = Timer("func_2([0,1,2,3,4,5,6,7,8,9])", "from __main__ import func_2")
print("Func_2 ", t2.timeit(number=10000), "milliseconds")
t2_2 = Timer("func_2_2([0,1,2,3,4,5,6,7,8,9])", "from __main__ import func_2_2")
print("Func_2_2 ", t2_2.timeit(number=10000), "milliseconds")
t3 = Timer("func_3([0,1,2,3,4,5,6,7,8,9])", "from __main__ import func_3")
print("Func_3 ", t3.timeit(number=10000), "milliseconds")

"""
Задание 1.
Добавьте аналитику:
1. выкнинул лишний вывод массива (т.к. это операция сцитывания)
2. попробовал генератор, но видимо его тормозит условие
3. сделал генератор без условия (он быстрее)
4. сделал вывод функцией
"""