"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
from random import random
from timeit import timeit


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = int(len(L) / 2)
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])

        return merge(left, right)


orig_list = [random() * 50 for _ in range(10)]
print(orig_list)
print(merge_sort(orig_list))

# замеры 10
orig_list = [random() * 50 for _ in range(10)]
print()
print(f'замеры 10')
print(
    timeit(
        "merge_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random() * 50 for _ in range(100)]
# замеры 100
print()
print(f'замеры 100')
print(
    timeit(
        "merge_sort(orig_list[:])",
        globals=globals(),
        number=1000))

# замеры 1000
orig_list = [random() * 50 for _ in range(1000)]
print()
print(f'замеры 1000')
print(
    timeit(
        "merge_sort(orig_list[:])",
        globals=globals(),
        number=1000))

# [39.91015982460011, 44.855777904614, 32.585335493180345, 49.58815707493513, 28.62650547236531, 40.56427994650921, 49.83788473014959, 1.171226861130037, 48.38721327032749, 31.891446240528193]
# [1.171226861130037, 28.62650547236531, 31.891446240528193, 32.585335493180345, 39.91015982460011, 40.56427994650921, 44.855777904614, 48.38721327032749, 49.58815707493513, 49.83788473014959]
#
# замеры 10
# 0.14694140000000003
#
# замеры 100
# 0.9429567999999999
#
# замеры 1000
# 9.4781508
# по сравнению с пузырьком данная сортировка на больших массивах
# выполняется гораздо быстрее
