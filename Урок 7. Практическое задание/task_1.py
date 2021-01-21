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

from random import randint
from timeit import timeit


def bubble_sort_1(lst):
    i = 0
    while i < len(lst) - 1:
        for j in range(len(lst) - 1):
            if lst[j] < lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
        i += 1
    return lst


def bubble_sort_2(lst):
    i = 0
    n = 'list already sorted'
    while i < len(lst) - 1:
        for j in range(len(lst) - 1):
            if lst[j] < lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                n = 'list sorting'
        if n == 'list already sorted':
            break
        i += 1
    return lst


lst_1 = [randint(-100, 100) for _ in range(10)]
lst_2 = [randint(-100, 100) for _ in range(30)]
lst_3 = [randint(-100, 100) for _ in range(60)]

lst_4 = [8, 7, 6, 5, 4, 3, 2, 1]


print('sort list with original bubble sort', lst_4, 'time =',
      timeit("bubble_sort_1(lst_4)", setup="from __main__ import bubble_sort_1, lst_4", number=1000))
print('sort list with new bubble sort', lst_4, 'time =',
      timeit("bubble_sort_2(lst_4)", setup="from __main__ import bubble_sort_2, lst_4", number=1000))

print('list for sort', lst_1)
print(timeit("bubble_sort_1(lst_1[:])", setup="from __main__ import bubble_sort_1, lst_1", number=1000))
print(timeit("bubble_sort_2(lst_1[:])", setup="from __main__ import bubble_sort_2, lst_1", number=1000))


print('list for sort', lst_2)
print(timeit("bubble_sort_1(lst_2[:])", setup="from __main__ import bubble_sort_1, lst_2", number=1000))
print(timeit("bubble_sort_2(lst_2[:])", setup="from __main__ import bubble_sort_2, lst_2", number=1000))


print('list for sort', lst_3)
print(timeit("bubble_sort_1(lst_3[:])", setup="from __main__ import bubble_sort_1, lst_3", number=1000))
print(timeit("bubble_sort_2(lst_3[:])", setup="from __main__ import bubble_sort_2, lst_3", number=1000))


# -----------------------------------------------------------------------------------
# в первых замерах я на вход подала намеренно сортированный список, результат показывает, что улучшенная функция
# дает экономию в 10 раз
# sort list with original bubble sort [8, 7, 6, 5, 4, 3, 2, 1] time = 0.013256603000000006
# sort list with new bubble sort [8, 7, 6, 5, 4, 3, 2, 1] time = 0.0016426649999999876

# Когда на вход попадают неотсортированные списки, данное улучшение функции бесполезно

#------------------------------------------------------------------------------------
# list for sort [82, 48, 12, -79, -79, -36, -48, 60, 89, 59]
# 0.0187128
# 0.021533184999999982
# -----------------------------------------------------------------------------------
# list for sort [85, 80, -83, -3, 7, 67, 64, -14, -56, -83, 72, 47, -96, 80, -93, -3, -26, 63,
# 76, 39, -92, -85, -23, -55, -18, -53, -48, 23, 94, 45]
# 0.14966239199999998
# 0.153426428
# ------------------------------------------------------------------------------------
# list for sort [-89, -90, -61, -82, -40, -93, -19, 8, -10, -54, 79, 2, -62, -37, -76, -60,
# -94, 58, -100, -30, -62, -2, -6, 61, -21, 38, -86, 71, 39, 40, -62, 5, 31, 76, -35, -77, 51, -98,
# -56, 13, -81, 57, 97, -3, 73, 10, -29, 59, -44, 36, -93, -18, 22, -60, -67, -18, 61, -14, 53, -44]
# 0.627756333
# 0.5930756559999999
