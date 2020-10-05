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


def speed_sort(lst_obj):
    n = 1
    flag = 0
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                flag = 1
        n += 1
        if flag == 0:
            break
        flag = 0
    return lst_obj


orig_list = [random.randint(-100, 100) for _ in range(5)]
lst = orig_list.copy()
print(f' Исходный -  {orig_list}')
print(f' Отсортированный методом "пузырька" - {bubble_sort(orig_list)}')
print(f' Отсортированный доработанным методом - {speed_sort(lst)}')

orig_list = [random.randint(-100, 100) for _ in range(10)]
lst = orig_list.copy()
# замеры 10
print(timeit.timeit("bubble_sort(orig_list)", \
                    setup="from __main__ import bubble_sort, orig_list", number=1))
print(timeit.timeit("speed_sort(lst)", \
                    setup="from __main__ import speed_sort, lst", number=1))

orig_list = [random.randint(-100, 100) for _ in range(100)]
lst = orig_list.copy()

# замеры 100
print(timeit.timeit("bubble_sort(orig_list)", \
                    setup="from __main__ import bubble_sort, orig_list", number=1))
print(timeit.timeit("speed_sort(lst)", \
                    setup="from __main__ import speed_sort, lst", number=1))

orig_list = [random.randint(-100, 100) for _ in range(1000)]
lst = orig_list.copy()

# замеры 1000
print(timeit.timeit("bubble_sort(orig_list)", \
                    setup="from __main__ import bubble_sort, orig_list", number=1))
print(timeit.timeit("speed_sort(lst)", \
                    setup="from __main__ import speed_sort, lst", number=1))

"""
 Исходный массив -  [17, -33, 13, 62, -19]
 Отсортированный методом "пузырька" - [62, 17, 13, -19, -33]
 Отсортированный доработанным методом - [62, 17, 13, -19, -33]
- замеры 10
1.9499999999998685e-05
1.4799999999998842e-05
- замеры 100
0.001180900000000002
0.0013045999999999995
- замеры 1000
0.11897229999999999
0.11854630000000002
Доработанный алгоритм немного быстрее.
"""
