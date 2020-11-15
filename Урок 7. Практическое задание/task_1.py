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
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


def better_bubble_sort(lst_obj):
    n = 1
    flag = False
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                flag = True
        if flag:
            break
        n += 1
    return lst_obj


orig_list = [random.randint(-100, 100) for _ in range(10)]
print("\nСортировка массва длинной 10:")
print(f'обычная пузырьковая: \
    {timeit.timeit("bubble_sort(orig_list)", setup="from __main__ import bubble_sort, orig_list", number=1000)} сек')
orig_list = [random.randint(-100, 100) for _ in range(10)]
print(f'улучшенная пузырьковая: \
{timeit.timeit("bubble_sort(orig_list)", setup="from __main__ import bubble_sort, orig_list", number=1000)} сек')

orig_list = [random.randint(-100, 100) for _ in range(100)]
print("\nСортировка массва длинной 100:")
print(f'обычная пузырьковая: \
{timeit.timeit("bubble_sort(orig_list)", setup="from __main__ import bubble_sort, orig_list", number=100)} сек')
orig_list = [random.randint(-100, 100) for _ in range(100)]
print(f'улучшенная пузырьковая: \
{timeit.timeit("bubble_sort(orig_list)", setup="from __main__ import bubble_sort, orig_list", number=100)} сек')

orig_list = [random.randint(-100, 100) for _ in range(1000)]
print("\nСортировка массва длинной 1000:")
print(f'обычная пузырьковая: \
{timeit.timeit("bubble_sort(orig_list)", setup="from __main__ import bubble_sort, orig_list", number=10)} сек')
orig_list = [random.randint(-100, 100) for _ in range(1000)]
print(f'улучшенная пузырьковая: \
{timeit.timeit("bubble_sort(orig_list)", setup="from __main__ import bubble_sort, orig_list", number=10)} сек')

"""
Сортировка массва длинной 10:
обычная пузырьковая: 0.046772190000410774 сек
улучшенная пузырьковая: 0.05777309699988109 сек

Сортировка массва длинной 100:
обычная пузырьковая: 0.25546205899991037 сек
улучшенная пузырьковая: 0.22354361700035952 сек

Сортировка массва длинной 1000:
обычная пузырьковая: 1.4228838119997818 сек
улучшенная пузырьковая: 1.3004445770002349 сек

Улучшение пузырьковой сортировки в основном даёт некоторый выигрыш на длинных массивах, на средних и коротких
преимущество едва различимое, или даже случается проигрыш
"""
