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


def bubble_sort(lst):
    n = 1
    while n < len(lst):
        for i in range(len(lst)-n):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
        n += 1
    return lst


def bubble_sort_update(lst):
    flag = True
    n = 1
    while n < len(lst) and flag:
        flag = False
        for i in range(len(lst) - n):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                flag = True
        n += 1
    return lst


orig_list = [random.randint(-100, 100) for _ in range(10)]
print(orig_list)
print(bubble_sort(orig_list[:]))
print(timeit("bubble_sort(orig_list[:])", setup="from __main__ import bubble_sort, orig_list", number=1000))
print(bubble_sort_update(orig_list[:]))
print(timeit("bubble_sort_update(orig_list[:])", setup="from __main__ import bubble_sort_update, orig_list",
             number=1000))
"""
0.012302444
0.011825172000000002
Замеры показывают что усоввершенствование алгорится критически не влияет на его скорость.
Видмо з-за того что отсортировванные списки будут встречаться редко
"""