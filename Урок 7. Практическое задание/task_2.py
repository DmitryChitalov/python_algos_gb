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


def sort(list_obj):

    if len(list_obj) > 1:
        mid = len(list_obj) // 2
        left = list_obj[:mid]
        right = list_obj[mid:]

        sort(left)
        sort(right)

        a = 0
        b = 0
        c = 0
        while a < len(left) and b < len(right):
            if left[a] < right[b]:
                list_obj[c] = left[a]
                a = a + 1
            else:
                list_obj[c] = right[b]
                b = b + 1
            c = c + 1

        while a < len(left):
            list_obj[c] = left[a]
            a = a + 1
            c = c + 1

        while b < len(right):
            list_obj[c] = right[b]
            b = b + 1
            c = c + 1


list_obj = [random.random() * 50 for i in range(5)]

print(f"Исходный: {list_obj}")
sort(list_obj)
print(f"Отсортированный: {list_obj}")