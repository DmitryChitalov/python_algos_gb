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


def list_gen(n=int(input('Введите число элементов: '))):
    array = [uniform(0, 50) for _ in range(n)]
    return array


def merge_sort(list_obj):
    if len(list_obj) > 1:
        center = len(list_obj) // 2
        left = list_obj[:center]
        right = list_obj[center:]

        merge_sort(left)
        merge_sort(right)

        i, j, f = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list_obj[f] = left[i]
                i += 1
            else:
                list_obj[f] = right[j]
                j += 1
            f += 1

        while i < len(left):
            list_obj[f] = left[i]
            i += 1
            f += 1

        while j < len(right):
            list_obj[f] = right[j]
            j += 1
            f += 1

        return list_obj


data = list_gen()
print(f'Исходный - {data}')
print(f'Отсортированный - {merge_sort(data)}')
