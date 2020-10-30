"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, ...

arr[m]
from statistics import median
"""
from statistics import median
from random import randint


def median_of_array(arr):
    result = None
    for idx in range(len(arr)):
        right = []
        left = []
        for jdx in range(len(arr)):
            if arr[idx] >= arr[jdx]:
                left.append(arr[jdx])
            if arr[idx] <= arr[jdx]:
                right.append(arr[jdx])
            if arr[idx] == arr[jdx] and idx > jdx:
                left.append(arr[jdx])
            if arr[idx] == arr[jdx] and idx < jdx:
                right.append(arr[jdx])
        if len(left) == len(right):
            result = arr[idx]
            return f'медиана из функции: {result}'


user_list = [randint(0, 100) for _ in range(9)]
print(user_list)
a = sorted(user_list)
print(a)
print(median_of_array(user_list))
print(f'медиана из модуля статистика: {median(user_list)}')