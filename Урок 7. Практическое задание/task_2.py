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
from collections import deque


def merge_sort(raw):
    if len(raw) <= 1:
        return raw
    else:
        half = len(raw) // 2
        left = merge_sort(raw[:half])
        right = merge_sort(raw[half:])
    return merge(left, right)


def merge(left, right):
    result = []
    if left and right is not None:
        left = deque(left)
        right = deque(right)
        while left and right:
            if left[0] <= right[0]:
                result.append(left.popleft())
            else:
                result.append(right.popleft())
    if left is not None:
        left = deque(left)
        while left:
            result.append(left.popleft())
    if right is not None:
        right = deque(right)
        while right:
            result.append(right.popleft())
    return result


m = int(input('Введите число элементов : '))
arr = [uniform(0, 50) for _ in range(m)]
print(f'Исходный : {arr}')
print(f'Сортированный : {merge_sort(arr)}')
