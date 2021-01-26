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
"""Сортировка пузырьком"""

import timeit
import random
import copy


##с доработкой
def bubble_sort_dor(lst_obj):
    n = 1
    while n < len(lst_obj):
        count = 0
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
            else:
                count += 1
                if count == len(lst_obj) - n:
                    return lst_obj
        n += 1
    return lst_obj


#без доработки
def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


orig_list = [random.randint(-100, 100) for _ in range(10)]
orig_list_100 = [random.randint(-100, 100) for _ in range(100)]
orig_list_1000 = [random.randint(-100, 100) for _ in range(1000)]

sort_list = [number for number in range(10, 0, -1)]
sort_list_100 = [number for number in range(100, 0, -1)]
sort_list_1000 = [number for number in range(1000, 0, -1)]

copy_orig_lst = copy.copy(orig_list)
copy_orig_lst_100 = copy.copy(orig_list_100)
copy_orig_lst_1000 = copy.copy(orig_list_1000)

copy_sort_list = copy.copy(sort_list)
copy_sort_list_100 = copy.copy(sort_list_100)
copy_sort_list_1000 = copy.copy(sort_list_1000)

print('1. Сортировка по убыванию без доработки:')
print('Не сортированный список:')
print(orig_list)
print(bubble_sort(orig_list))
print('Время:')
# замеры 10
print(timeit.timeit("bubble_sort(orig_list)", \
    setup=f"from __main__ import bubble_sort, orig_list", number=1))
# замеры 100
print(timeit.timeit("bubble_sort(orig_list_100)", \
    setup="from __main__ import bubble_sort, orig_list_100", number=1))
# замеры 1000
print(timeit.timeit("bubble_sort(orig_list_1000)", \
    setup="from __main__ import bubble_sort, orig_list_1000", number=1))

print('Сортированный список:')
print(sort_list)
print(bubble_sort(sort_list))
print('Время:')
# замеры 10
print(timeit.timeit("bubble_sort(sort_list)", \
    setup=f"from __main__ import bubble_sort, sort_list", number=1))
# замеры 100
print(timeit.timeit("bubble_sort(sort_list_100)", \
    setup="from __main__ import bubble_sort, sort_list_100", number=1))
# замеры 1000
print(timeit.timeit("bubble_sort(sort_list_1000)", \
    setup="from __main__ import bubble_sort, sort_list_1000", number=1))

print('2. Сортировка по убыванию с доработкой:')
print('Не сортированный список:')
print(copy_orig_lst)
print(bubble_sort_dor(copy_orig_lst))
print('Время:')
# замеры 10
print(timeit.timeit("bubble_sort_dor(copy_orig_lst)", \
    setup=f"from __main__ import bubble_sort_dor, copy_orig_lst", number=1))
# замеры 100
print(timeit.timeit("bubble_sort_dor(copy_orig_lst_100)", \
    setup="from __main__ import bubble_sort_dor, copy_orig_lst_100", number=1))
# замеры 1000
print(timeit.timeit("bubble_sort_dor(copy_orig_lst_1000)", \
    setup="from __main__ import bubble_sort_dor, copy_orig_lst_1000", number=1))

print('Сортированный список:')
print(copy_sort_list)
print(bubble_sort_dor(copy_sort_list))
print('Время:')
# замеры 10
print(timeit.timeit("bubble_sort_dor(copy_sort_list)", \
    setup=f"from __main__ import bubble_sort_dor, copy_sort_list", number=1))
# замеры 100
print(timeit.timeit("bubble_sort_dor(copy_sort_list_100)", \
    setup="from __main__ import bubble_sort_dor, copy_sort_list_100", number=1))
# замеры 1000
print(timeit.timeit("bubble_sort_dor(copy_sort_list_1000)", \
    setup="from __main__ import bubble_sort_dor, copy_sort_list_1000", number=1))
"""
Результаты:
1. Сортировка по убыванию без доработки:
Не сортированный список:
[-90, 69, -2, -59, 6, -7, 94, 46, -38, 78]
[94, 78, 69, 46, 6, -2, -7, -38, -59, -90]
Время:
2.6761001208797097e-05
0.005007888998079579
0.5655015680022188
Сортированный список:
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
Время:
2.3812994186300784e-05
0.002671378999366425
0.27764728200418176
2. Сортировка по убыванию с доработкой:
Не сортированный список:
[-90, 69, -2, -59, 6, -7, 94, 46, -38, 78]
[94, 78, 69, 46, 6, -2, -7, -38, -59, -90]
Время:
9.467999916523695e-06
0.0062577360004070215
0.703208220002125
Сортированный список:
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
Время:
1.0987998393829912e-05
6.93929978297092e-05
0.0017095650036935695

Судя по результатам алгоритм с доработкой, работает быстрее.
"""