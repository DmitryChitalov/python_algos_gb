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
import operator
import random
import timeit


def merge_sort(L, compare=operator.lt):
    if len(L) < 2:
        return L[:]
    else:
        middle = int(len(L) / 2)
        left = merge_sort(L[:middle], compare)
        right = merge_sort(L[middle:], compare)
        return merge(left, right, compare)


def merge(left, right, compare):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
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


print("Для 10 вещественных элементов")
orig_list = [random.uniform(0, 49.99) for _ in range(10)]
print(orig_list)
print(merge_sort(orig_list[:]))
print(
    timeit.timeit(
        "merge_sort(orig_list[:])",
        globals=globals(),
        number=1000))

print("Для 100 вещественных элементов")
orig_list = [random.uniform(0, 49.99) for _ in range(100)]
print(
    timeit.timeit(
        "merge_sort(orig_list[:])",
        globals=globals(),
        number=1000))

print("Для 1000 вещественных элементов")
orig_list = [random.uniform(0, 49.99) for _ in range(1000)]
print(
    timeit.timeit(
        "merge_sort(orig_list[:])",
        globals=globals(),
        number=1000))

print("Для 10000 вещественных элементов")
orig_list = [random.uniform(0, 49.99) for _ in range(10000)]
print(
    timeit.timeit(
        "merge_sort(orig_list[:])",
        globals=globals(),
        number=1000))

'''
Сложность алгоритма O(n log2n)
Замеры
Для 10 вещественных элементов
0.019003300000000004
Для 100 вещественных элементов
0.3139554
Для 1000 вещественных элементов
4.3046968
Для 10000 вещественных элементов
56.694819800000005
'''
