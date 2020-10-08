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
########################################################################################################################

from random import randint
from timeit import timeit
import memory_profiler

some_list = []
for i in range(15):
    some_list.append(randint(-100, 100))
a = sorted(some_list)
a.reverse()
print(some_list)

m1 = memory_profiler.memory_usage()


def bubble_sort(lst):
    n = 1
    while n < len(lst):
        for y in range(len(lst) - n):
            if lst[y] < lst[y+1]:
                lst[y], lst[y+1] = lst[y+1], lst[y]
        n += 1
    return lst


m2 = memory_profiler.memory_usage()

print(
    timeit(
        'bubble_sort(some_list)',
        setup='from __main__ import bubble_sort, some_list',
        number=10000
    )
)

print(m2[0] - m1[0])
print(bubble_sort(some_list))


some_list_2 = []
for i in range(15):
    some_list_2.append(randint(-100, 100))
print(some_list_2)

m3 = memory_profiler.memory_usage()


def bubble_sort_2(lst):
    n = 1
    while n < len(lst):
        for y in range(len(lst) - n):
            if lst[y] < lst[y+1]:
                lst[y], lst[y+1] = lst[y+1], lst[y]
            else:
                n += 1
        n += 1
    return lst


m4 = memory_profiler.memory_usage()

print(
    timeit(
        'bubble_sort_2(some_list_2)',
        setup='from __main__ import bubble_sort_2, some_list_2',
        number=10000
    )
)
print(m4[0] - m3[0])
print(bubble_sort_2(some_list_2))

"""
Сортировка методом "Пузырёк", время:        0.25207 сек.
Сортировка методом "Пузырёк_2", время:      0.03866 сек.

Вывод:
    Удалось оптимизовать программу, ускорить в 7 раз, путем добавления условия,
    если первое не верное, пропускаются целые циклы. 
    
    
Run:

Исходный some_list:             [-70, -90, 96, -69, 34, 3, -46, -18, 56, -60, 32, -40, -84, 64, 94]
Время:                          0.25207759900000004
Отсортированный some_list:      [96, 94, 64, 56, 34, 32, 3, -18, -40, -46, -60, -69, -70, -84, -90]


Исходный some_list_2:           [-60, -80, -19, 1, 54, 70, 63, -60, 11, -30, -97, 99, -78, -17, 38]
Время:                          0.03866634200000002
Отсортированный some_list_2:    [99, 70, 63, 54, 38, 11, 1, -17, -19, -30, -60, -60, -78, -80, -97]
"""

"""
Так же сделал замеры потребляемой памяти:

Сортировка методом "Пузырёк", память:       0.0078125 Мб
Сортировка методом "Пузырёк_2", память:     0.0 Мб

Вывод:

    Метод "Пузырёк_2" лучше по всем параметрам.
"""