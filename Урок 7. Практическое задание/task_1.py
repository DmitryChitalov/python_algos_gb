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


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_mod(lst_obj):
    n = 1
    while n < len(lst_obj):
        br = True
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                br = False
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        if br:
            break
        n += 1
    return lst_obj


orig_list = [random.randint(-100, 100) for _ in range(10)]

# print(orig_list)
# print(bubble_sort(orig_list[:]))

# замеры 10
print('Без оптимизации:')
print(
    timeit.timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))
print('С оптимизацией:')
print(
    timeit.timeit(
        "bubble_sort_mod(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.randint(-100, 100) for _ in range(100)]
# print(orig_list)
# print(bubble_sort(orig_list[:]))
# замеры 100
print('Без оптимизации:')
print(
    timeit.timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))
print('С оптимизацией:')
print(
    timeit.timeit(
        "bubble_sort_mod(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.randint(-100, 100) for _ in range(1000)]
# print(orig_list)
# print(bubble_sort(orig_list[:]))
# замеры 1000
print('Без оптимизации:')
print(
    timeit.timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))
print('С оптимизацией:')
print(
    timeit.timeit(
        "bubble_sort_mod(orig_list[:])",
        globals=globals(),
        number=1000))

'''
Без оптимизации:
0.016479513999001938
С оптимизацией:
0.013237590999779059
Без оптимизации:
1.018088319000526
С оптимизацией:
0.9849809299994376
Без оптимизации:
110.95028141600051
С оптимизацией:
111.60645509700043

Польза от оптимизации - сомнительна. Иногда даже вредна!.
'''
