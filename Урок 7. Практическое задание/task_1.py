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


def bubble_sort_revers(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_revers_upd(lst_obj):
    n = 1
    while n < len(lst_obj):
        flag = 0
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                flag = 1
        n += 1
        if flag == 0:
            break
    return lst_obj


sample = [random.randint(-100, 100) for _ in range(10)]
# замеры 10
print('10 elements: ',
      timeit.timeit("bubble_sort_revers(sample)", setup="from __main__ import bubble_sort_revers, sample", number=100))
print('10 elements(upd): ',
      timeit.timeit("bubble_sort_revers_upd(sample)", setup="from __main__ import bubble_sort_revers_upd, sample", number=100))

sample = [random.randint(-100, 100) for _ in range(100)]
# замеры 100
print('100 elements: ',
      timeit.timeit("bubble_sort_revers(sample)", setup="from __main__ import bubble_sort_revers, sample", number=100))
print('100 elements(upd): ',
      timeit.timeit("bubble_sort_revers_upd(sample)", setup="from __main__ import bubble_sort_revers_upd, sample", number=100))

sample = [random.randint(-100, 100) for _ in range(1000)]
# замеры 1000
print('1000 elements: ',
      timeit.timeit("bubble_sort_revers(sample)", setup="from __main__ import bubble_sort_revers, sample", number=100))
print('1000 elements(upd): ',
      timeit.timeit("bubble_sort_revers_upd(sample)", setup="from __main__ import bubble_sort_revers_upd, sample", number=100))

'''
Доработка алгоритма заключается в выходе из цикла, если за проход по массиву не сделана ни одна перестановка.
Разница по времени очень заметна на массиве из 1000 элементов.

10 elements:  0.001326600000000011
10 elements(upd):  0.00022369999999999335
100 elements:  0.13967859999999999
100 elements(upd):  0.0015913000000000177
1000 elements:  13.8331978
1000 elements(upd):  0.0170735999999998
'''
