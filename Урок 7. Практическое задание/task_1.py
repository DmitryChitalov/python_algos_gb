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
from random import randrange

massive = [randrange(-100, 100) for i in range(10)]


def sorting(array):
    sorted_array = array
    j = 0
    while j < len(sorted_array):
        for i in range(len(sorted_array)-1):
            if sorted_array[i] < sorted_array[i+1]:
                bufer = sorted_array[i+1]
                sorted_array[i+1] = sorted_array[i]
                sorted_array[i] = bufer
        j += 1
    return sorted_array


def sorting_clever(array):
    sorted_array = array
    j = 0
    while j < len(sorted_array):
        change_check = 0
        for i in range(len(sorted_array)-1):
            if sorted_array[i] < sorted_array[i+1]:
                bufer = sorted_array[i+1]
                sorted_array[i+1] = sorted_array[i]
                sorted_array[i] = bufer
                change_check = 1
        if change_check == 0:
            return sorted_array
            break;
        j += 1
    return sorted_array

print(massive)
print(sorting(massive))
print(sorting_clever(massive))

a = timeit(
    "sorting(massive)",
    setup='from __main__ import sorting, massive',
    number=10000)
b = timeit(
    "sorting_clever(massive)",
    setup='from __main__ import sorting_clever, massive',
    number=10000)
print('Не оптимизированная ',a, '\n''Оптимизированная',b)