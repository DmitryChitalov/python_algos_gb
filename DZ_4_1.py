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


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr


def func_3(nums):
    new_arr = []
    i = 0
    while i < len(nums):
        if nums[i] % 2 == 0:
            new_arr.append(i)
        i += 1
    return new_arr


num = [i for i in range(1000)]

el_time_for = (timeit.timeit("func_1(num)", setup="from __main__ import func_1, num", number=5000)) / 10
el_time_gen = (timeit.timeit("func_2(num)", setup="from __main__ import func_2, num", number=5000)) / 10
el_time_while = (timeit.timeit("func_3(num)", setup="from __main__ import func_3, num", number=5000)) / 10

print(f"Время с циклом for - {el_time_for}")
print(f"Время с генераторным выражением - {el_time_gen}")
print(f"Время с циклом while - {el_time_while}")

# ---------------------------ВЫВОДЫ-----------------------------------
# Очевидно что генераторное выражение быстрее чем цикл for
# Лично для меня (как для новичка) цикл while более интуитивно понятен,
# но очевидно что он самый медленный.
