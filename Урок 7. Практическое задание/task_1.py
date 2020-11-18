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

import random
import timeit


def buble_sort(orig_list):
    n = 1
    while n < len(orig_list):
        for i in range(len(orig_list) - n):
            if orig_list[i] < orig_list[i + 1]:
                orig_list[i], orig_list[i + 1] = orig_list[i + 1], orig_list[i]
        n += 1
    return orig_list


def buble_sort_upd(orig_list):
    n = 1
    k = 0
    while n < len(orig_list):
        for i in range(len(orig_list) - n):
            if orig_list[i] < orig_list[i + 1]:
                orig_list[i], orig_list[i + 1] = orig_list[i + 1], orig_list[i]
                k = 1
        if k == 0:
            break
        n += 1
    return orig_list


orig_list = [random.randint(-100, 100) for i in range(1000)]
print(timeit.timeit('buble_sort(orig_list[:])',
                    setup='from __main__ import buble_sort, orig_list', number=100))
print(timeit.timeit('buble_sort_upd(orig_list[:])',
                    setup='from __main__ import buble_sort_upd, orig_list', number=100))
