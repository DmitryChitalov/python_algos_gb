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


def rev_bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        exchanges = False
        for i in range(len(lst_obj) - n):
            if lst_obj[i] > lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                exchanges = True
        if not exchanges:
            break
        n += 1
    return lst_obj

def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        exchanges = False
        for i in range(len(lst_obj)-n):
            if lst_obj[i] > lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
                exchanges = True
        if not exchanges:
            break
        n += 1
    return lst_obj

orig_list = [random.randint(-100, 100) for _ in range(10)]
orig_list_2 = [0, 3, 5, 7, 78, 79, 90, 91, 92, 97]


print(rev_bubble_sort(orig_list))

print('unsorted list, rev_bubble_sort', timeit("rev_bubble_sort(orig_list[:])", \
    setup="from __main__ import rev_bubble_sort, orig_list")) # если список не отсортирован = 1.719 и  улучшенная сортировка

print('unsorted list, bubble_sort', timeit("bubble_sort(orig_list[:])", \
    setup="from __main__ import bubble_sort, orig_list")) # если список не отсортирован = 1.1677 и обычная сортировка

print(rev_bubble_sort(orig_list_2))

print('sorted list, rev_bubble_sort', timeit("rev_bubble_sort(orig_list_2[:])", \
    setup="from __main__ import rev_bubble_sort, orig_list_2")) #1.5519  это если список отсортирован и  улучшенная сортировка

print('sorted list, bubble_sort', timeit("bubble_sort(orig_list_2[:])", \
    setup="from __main__ import bubble_sort, orig_list_2")) #1.55224  это если список отсортирован и обычная сортировка

#исходя из замеров, улучшение алгаритма, практически, никак не сказалось на улучшении времени.