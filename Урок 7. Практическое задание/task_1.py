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
from random import randint
from timeit import timeit


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


def speed_bubble_sort(lst_obj):
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


lst_obj = [randint(-100, 100) for i in range(20)]
print(f'Исходный массив:\n{lst_obj}')
print(f'Массив отсортированный обычным пузырьковым меотодом:\n{bubble_sort(lst_obj.copy())}')
print(f'Массив отсортированный быстрым пузырьковым меотодом:\n{speed_bubble_sort(lst_obj.copy())}')
print(timeit('bubble_sort(lst_obj.copy())', setup='from __main__ import bubble_sort, lst_obj', number=10000))
print(timeit('speed_bubble_sort(lst_obj.copy())', setup='from __main__ import speed_bubble_sort, lst_obj', number=10000))
"""
Оптимизация дает небольшой результат:
0.5940265 - без оптимизации
0.5216014999999999 - с оптимизацией
"""

