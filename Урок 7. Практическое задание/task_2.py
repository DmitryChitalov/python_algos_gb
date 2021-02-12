"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Хотя в примерах к уроку уже есть вариант реализации слияния, попробуйте предложить другой
(придумать или найти)

И попытаться сделать замеры на массивах разной длины: 10, 100, 1000, ...

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""

from random import uniform
from timeit import timeit


def merge_sort(my_list):
    if len(my_list) < 2:
        return my_list[:]
    else:
        middle = int(len(my_list) / 2)
        list_left = merge_sort(my_list[:middle])
        list_right = merge_sort(my_list[middle:])

        res = []
        i, j = 0, 0
        while i < len(list_left) and j < len(list_right):
            if list_left[i] < list_right[j]:
                res.append(list_left[i])
                i += 1
            else:
                res.append(list_right[j])
                j += 1

        while i < len(list_left):
            res.append(list_left[i])
            i += 1

        while j < len(list_right):
            res.append(list_right[j])
            j += 1

        return res


sort_list_10 = [uniform(0, 50) for i in range(10)]
sort_list_100 = [uniform(0, 50) for i in range(100)]
sort_list_1000 = [uniform(0, 50) for i in range(1000)]

print(sort_list_10)
print(merge_sort(sort_list_10[:]))

print(
    "Замер времени работы на 10 элементах: ",
    timeit(
        "merge_sort(sort_list_10[:])",
        globals=globals(),
        number=1000))

print(
    "Замер времени работы на 100 элементах: ",
    timeit(
        "merge_sort(sort_list_100[:])",
        globals=globals(),
        number=1000))

print(
    "Замер времени работы на 1000 элементах: ",
    timeit(
        "merge_sort(sort_list_1000[:])",
        globals=globals(),
        number=1000))
