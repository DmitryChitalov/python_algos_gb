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
from timeit import Timer
import random


# Добавили новую функцию, которая бегает по циклу через enumerate, enumerate уже сам строит индексы массива
# И нам не нужно выбирать этот индекс самостоятельно из листа nums.
def func_2(nums):
    new_arr = []
    for i, num in enumerate(nums, start=0):
        if num % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


# l = [1,2,4,7,8,10,22]

l = random.randint(0, 10000000000)

t = Timer("func_1", "from __main__ import func_1")
t1 = Timer("func_2", "from __main__ import func_2")

# При больших объемах, через функцию enumerate, работает быстрее. Что показывает статистика func1= 0.0165083 func2= 0.0164659

print("func1=", t.timeit(number=1000000), "func2=", t1.timeit(number=1000000))
