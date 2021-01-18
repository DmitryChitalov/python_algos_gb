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


m = 5
arr = [randint(0, 50) for _ in range(m * 2 + 1)]


def gnome(data):
    i, size = 1, len(data)
    while i < size:
        if data[i - 1] <= data[i]:
            i += 1
        else:
            data[i - 1], data[i] = data[i], data[i - 1]
            if i > 1:
                i -= 1
    return data


def median_hand_made(sorted_arr):
    median_index = len(sorted_arr) - len(sorted_arr) // 2 - 1
    median = sorted_arr[median_index]
    return median


print(arr)
print(gnome(arr))
print(median_hand_made(gnome(arr)))
print(median(arr)) # проверка
