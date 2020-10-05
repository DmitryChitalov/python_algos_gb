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
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(lst_obj) - 1):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                swapped = True
    return lst_obj


orig_list = [randint(-100, 100) for _ in range(10)]
print(orig_list)
# [65, -59, 100, -66, 93, 96, 92, -91, -21, -87]

# замеры 10
print(timeit("bubble_sort(orig_list)", \
             setup="from __main__ import bubble_sort, orig_list", number=1))
# 1.2140022590756416e-05
print(bubble_sort(orig_list))
# [100, 96, 93, 92, 65, -21, -59, -66, -87, -91]

orig_list = [randint(-100, 100) for _ in range(100)]

# замеры 100
print(timeit("bubble_sort(orig_list)", \
             setup="from __main__ import bubble_sort, orig_list", number=1))
# 0.0010861470072995871

orig_list = [randint(-100, 100) for _ in range(1000)]

# замеры 1000
print(timeit("bubble_sort(orig_list)", \
             setup="from __main__ import bubble_sort, orig_list", number=1))
# 0.10591145200305618

orig_list = [randint(-100, 100) for _ in range(100000)]

# замеры 100000
print(timeit("bubble_sort(orig_list)", \
             setup="from __main__ import bubble_sort, orig_list", number=1))
# 1051.8811158440076


'''
def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] > lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


orig_list = [randint(-100, 100) for _ in range(10)]

# замеры 10
print(timeit("bubble_sort(orig_list)", \
             setup="from __main__ import bubble_sort, orig_list", number=1))
# 1.6178993973881006e-05

orig_list = [randint(-100, 100) for _ in range(100)]

# замеры 100
print(timeit("bubble_sort(orig_list)", \
             setup="from __main__ import bubble_sort, orig_list", number=1))
# 0.0007023389916867018


orig_list = [randint(-100, 100) for _ in range(1000)]

# замеры 1000
print(timeit("bubble_sort(orig_list)", \
             setup="from __main__ import bubble_sort, orig_list", number=1))
# 0.06537282699719071

orig_list = [randint(-100, 100) for _ in range(100000)]

# замеры 100000
print(timeit("bubble_sort(orig_list)", \
             setup="from __main__ import bubble_sort, orig_list", number=1))
# 645.0994719610026'''

'''Вывод: сортировка с проверкой когда элементы не меняются местами, ожидаемого улучшения
 по времени не дала.'''