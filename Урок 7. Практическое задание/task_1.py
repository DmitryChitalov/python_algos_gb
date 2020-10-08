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
from timeit import timeit
from random import randint


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_2(lst_obj):
    n = 1
    while n < len(lst_obj):
        sort = True
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
                sort = False
        if sort:
            return lst_obj
        n += 1
    return lst_obj


orig_list = [randint(-100, 100) for i in range(15)]
copy_list = orig_list.copy()

print(f'Исходный - {orig_list}')
print(f'Отсортированный 1 - {bubble_sort(copy_list)}')
print(f'Отсортированный 2 - {bubble_sort_2(copy_list)}')

print('замеры 100')
print(timeit("bubble_sort(orig_list.copy())", setup="from __main__ import bubble_sort, orig_list", number=100))
print(timeit("bubble_sort_2(orig_list.copy())", setup="from __main__ import bubble_sort_2, orig_list", number=100))

print('замеры 1000')
print(timeit("bubble_sort(orig_list.copy())", setup="from __main__ import bubble_sort, orig_list", number=1000))
print(timeit("bubble_sort_2(orig_list.copy())", setup="from __main__ import bubble_sort_2, orig_list", number=1000))

print('замеры 10000')
print(timeit("bubble_sort(orig_list.copy())", setup="from __main__ import bubble_sort, orig_list", number=10000))
print(timeit("bubble_sort_2(orig_list.copy())", setup="from __main__ import bubble_sort_2, orig_list", number=10000))

"""
Исходный - [60, -12, 17, -32, -66, -7, 43, 72, -64, 81, -42, 30, 78, -77, 7]
Отсортированный 1 - [81, 78, 72, 60, 43, 30, 17, 7, -7, -12, -32, -42, -64, -66, -77]
Отсортированный 2 - [81, 78, 72, 60, 43, 30, 17, 7, -7, -12, -32, -42, -64, -66, -77]
замеры 100
0.0034456
0.0030446000000000015
замеры 1000
0.0315103
0.033415
замеры 10000
0.32961209999999996
0.30797019999999997

По результатам замеров видим, что оптимизированная сортировка пузырьком работает так же.
"""