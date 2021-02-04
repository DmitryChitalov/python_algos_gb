"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание считается не принятым
"""

import random as r, timeit as t

def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    even = [i for i in nums if i % 2 == 0]
    return even


ll = []
[ll.append(r.randint(1, 300)) for z in range(1, 1000)]


print(t.timeit("func_1(ll)", globals=globals(), number=10000))
print(t.timeit("func_2(ll)", globals=globals(), number=10000))


# Вторая функция была сделана как списковое вложение, как показывают результаты списковое вложения
# выводит результаты с более высокой скоростью
