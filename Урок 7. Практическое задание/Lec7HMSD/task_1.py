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


def bubble_sort_inverse(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_inverse_opt(lst_obj):
    n = 1
    doit = 1
    while n < len(lst_obj) or doit == 1:
        doit = 0
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                doit = 1
        n += 1
    return lst_obj


# orig_list = [random.randint(-100, 100) for _ in range(10)]
# print(orig_list)
# print(bubble_sort(orig_list))
# print(bubble_sort_inverse(orig_list))

orig_list = [random.randint(-100, 100) for _ in range(100)]
print(orig_list)

# замеры 1000
print(timeit.timeit("bubble_sort_inverse(orig_list[:])", \
                    setup="from __main__ import bubble_sort_inverse, orig_list", number=10000))

print(timeit.timeit("bubble_sort_inverse_opt(orig_list[:])", \
                    setup="from __main__ import bubble_sort_inverse_opt, orig_list", number=10000))

# print(bubble_sort(orig_list))
print(bubble_sort_inverse(orig_list))

# 14.2302133
# 13.994540000000002
# Вывод. При небольшой оптимизации, алгоритм на несколько процентов быстрее,но не в 100% случаях.
# Видимо операция присвоения также вносит временные задержки, и иногда время даже больше.
# 15.278856699999999
# 15.610569300000002
