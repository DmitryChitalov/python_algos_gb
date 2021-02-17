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
from random import randint
from timeit import timeit


def merge(alst, blst):
    clst = []
    i = 0
    j = 0
    while True:
        if alst[i] < blst[j]:
            clst.append(alst[i])
            i += 1
            if i == len(alst):
                clst.extend(blst[j:])
                break

        else:
            clst.append(blst[j])
            j += 1
            if j == len(blst):
                clst.extend(alst[i:])
                break

    return clst


def bottom_up_merge_sort(a):
    k = 1
    while k < len(a):
        for i in range(0, len(a) - k, 2 * k):
            a[i : i + 2 * k] = merge(a[i : i + k], a[i + k : i + 2 * k])
        k *= 2
    return a


test_array = [randint(0, 50) for i in range(10)]

print(test_array)
print(bottom_up_merge_sort(test_array[:]))
print(
    timeit(
        "bottom_up_merge_sort(test_array[:])", globals=globals(), number=1000
    )
)

test_array = [randint(0, 50) for i in range(100)]
print(
    timeit(
        "bottom_up_merge_sort(test_array[:])", globals=globals(), number=1000
    )
)

test_array = [randint(0, 50) for i in range(1000)]
print(
    timeit(
        "bottom_up_merge_sort(test_array[:])", globals=globals(), number=1000
    )
)

# Варинант сортировки слиянием снизу вверх.
