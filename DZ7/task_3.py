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
import timeit
import random


def gnome_sort(list_obj):
    i = 1
    while i < len(list_obj):
        if not i or list_obj[i - 1] <= list_obj[i]:
            i += 1
        else:
            list_obj[i], list_obj[i - 1] = list_obj[i - 1], list_obj[i]
            i -= 1
    return list_obj


def median_gnome(list_obj):
    return gnome_sort(list_obj)[len(list_obj) // 2 + 1]


m = int(input('Введите m: '))
list_obj = [random.randint(0, 100) for _ in range(2 * m + 1)]
print(list_obj)

# замеры 10
print(timeit.timeit("median_gnome(list_obj[:])", \
                    setup="from __main__ import median_gnome, list_obj", number=10))
print(median_gnome(list_obj))

list_obj = [random.randint(0, 100) for _ in range(2 * m + 1)]
print(list_obj)

# замеры 100
print(timeit.timeit("median_gnome(list_obj[:])", \
                    setup="from __main__ import median_gnome, list_obj", number=100))
print(median_gnome(list_obj))

list_obj = [random.randint(0, 100) for _ in range(2 * m + 1)]
print(list_obj)

# замеры 1000
print(timeit.timeit("median_gnome(list_obj[:])", \
                    setup="from __main__ import median_gnome, list_obj", number=1000))
print(median_gnome(list_obj))
