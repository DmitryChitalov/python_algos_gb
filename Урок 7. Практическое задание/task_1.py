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
from timeit import timeit


def bubble_sort_reverse_1(my_list):
    for i in range(len(my_list) - 1):
        for j in range(len(my_list) - 1 - i):
            if my_list[j] < my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    return my_list


sorted_list = [12, 11, 10, 9, 8, 5, 3, 2, 1, 0]
not_sorted_list = [random.randint(-100, 100) for _ in range(10)]
print(bubble_sort_reverse_1(sorted_list))

print(timeit("bubble_sort_reverse_1(sorted_list)",
             setup="from __main__ import bubble_sort_reverse_1, sorted_list", number=50))


#  не смог придумать как оптимизировать, чтобы после одного прохода, если не меняется, то вернуть исходный список(
