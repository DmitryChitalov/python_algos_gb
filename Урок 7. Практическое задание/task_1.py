"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""

import timeit
import random
from memory_profiler import profile


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] > lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_fast(lst_obj):
    n = 1

    while n < len(lst_obj):
        changes = 0
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
                changes += 1
        if changes == 0:
            return lst_obj
        else:
            n += 1
    return lst_obj


orig_list = [random.randint(-100, 100) for _ in range(10)]
print(orig_list)
print(timeit.timeit("bubble_sort(orig_list)", setup="from __main__ import bubble_sort, orig_list", number=1000))
print(timeit.timeit("bubble_sort_fast(orig_list)", setup="from __main__ import bubble_sort_fast, orig_list", number=1000))

"""
Для оптимизации алгоритма в функции bubble_sort_fast добавлена проверка в конце каждой проходки: если за проходку
не было совершено ни одной замены, то алгоритм завершает работу.

Такая оптимизация дает экономию времени:
bubble_sort:        0.004929199999999995
bubble_sort_fast:   0.000837300000000013

"""
