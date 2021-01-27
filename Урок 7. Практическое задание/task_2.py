"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
from random import uniform


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


n = int(input('Введите количсетво элементов: '))
lst_obj = [uniform(0, 50) for _ in range(n)]
arr = lst_obj
print(f'Исходный массив: {arr}')
print(f'Отсортированный массив: {merge_sort(lst_obj)}')
