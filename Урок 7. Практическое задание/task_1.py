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
print(timeit("bubble_sort(copy_list)", setup="from __main__ import bubble_sort, copy_list", number=100))
print(timeit("bubble_sort_2(copy_list)", setup="from __main__ import bubble_sort_2, copy_list", number=100))

print('замеры 1000')
print(timeit("bubble_sort(copy_list)", setup="from __main__ import bubble_sort, copy_list", number=1000))
print(timeit("bubble_sort_2(copy_list)", setup="from __main__ import bubble_sort_2, copy_list", number=1000))

print('замеры 10000')
print(timeit("bubble_sort(copy_list)", setup="from __main__ import bubble_sort, copy_list", number=10000))
print(timeit("bubble_sort_2(copy_list)", setup="from __main__ import bubble_sort_2, copy_list", number=10000))

"""
Исходный - [-92, 89, 54, 37, 43, -39, -5, -26, 50, 30, 20, -89, 3, -86, -32]
Отсортированный 1 - [89, 54, 50, 43, 37, 30, 20, 3, -5, -26, -32, -39, -86, -89, -92]
Отсортированный 2 - [89, 54, 50, 43, 37, 30, 20, 3, -5, -26, -32, -39, -86, -89, -92]

замеры 100
0.0018270000000000022
0.00022909999999999944
замеры 1000
0.019298799999999998
0.0022936999999999957
замеры 10000
0.19204569999999999
0.022897600000000018

По результатам замеров видим, что оптимизированная сортировка пузырьком работает на порядок быстрее.
"""