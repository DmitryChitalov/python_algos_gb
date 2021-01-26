"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
import random
import timeit


def merge_sort(lst_obj):
    n = len(lst_obj)
    if n < 2:
        return lst_obj

    left = merge_sort(lst_obj[:n // 2])
    right = merge_sort(lst_obj[n // 2:n])

    i = j = 0
    res = []
    while i < len(left) or j < len(right):
        if not i < len(left):
            res.append(right[j])
            j += 1
        elif not j < len(right):
            res.append(left[i])
            i += 1
        elif left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    return res


count = int(input("Введите число элементов: "))
orig_list = [random.uniform(0, 50) for _ in range(count)]
print(f'Исходный: {orig_list}')
print(f'Отсортированный: {merge_sort(orig_list)}')


orig_list = [random.uniform(0, 50) for _ in range(10)]

# замеры 10
print(timeit.timeit("merge_sort(orig_list)", setup="from __main__ import merge_sort, orig_list", number=1))

orig_list = [random.uniform(0, 50) for _ in range(100)]

# замеры 100
print(timeit.timeit("merge_sort(orig_list)", setup="from __main__ import merge_sort, orig_list", number=1))

orig_list = [random.uniform(0, 50) for _ in range(1000)]

# замеры 1000
print(timeit.timeit("merge_sort(orig_list)", setup="from __main__ import merge_sort, orig_list", number=1))

"""
Замеры на 10 элементов: 5.4700000000185156e-05
Замеры на 100 элементов: 0.0005731999999998294
Замеры на 1000 элементов: 0.007149000000000072
Результаты замеров показали что, с ростом количества элементов массива, время работы алгоритма остается приемлемым.
Тем самым, можно сделать вывод что сортировка выполнена корректно.
"""
