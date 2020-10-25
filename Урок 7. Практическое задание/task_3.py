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
from random import randint


def create_arr(number):
    number = number * 2 + 1
    arr = []
    for _ in range(number):
        arr.append(randint(0, 50))
    return arr


def median_sorted(arr):
    median_small = []
    median_much = []
    print(arr)
    for _ in range(len(arr) // 2):
        median_small.append(min(arr))
        arr.remove(min(arr))
        median_much.append(max(arr))
        arr.remove(max(arr))
    median_much.reverse()
    return median_small, arr, median_much


array = create_arr(3)
print(median_sorted(array))
array = create_arr(7)
print(median_sorted(array))
