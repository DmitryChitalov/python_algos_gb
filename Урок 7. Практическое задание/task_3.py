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

import random
from statistics import median


def gnome_sort(sample):
    i = 1
    while i < len(sample):
        if not i or sample[i - 1] <= sample[i]:
            i += 1
        else:
            sample[i], sample[i - 1] = sample[i - 1], sample[i]
            i -= 1
    return sample


def my_median(sample):
    return gnome_sort(sample)[len(sample) // 2]


m = int(input('Введите m - '))
my_sample = [random.randint(-100, 100) for _ in range(2*m + 1)]

print('Медиана с сортировкой массива -', my_median(list.copy(my_sample)))
print('Медиана через statistics-', median(list.copy(my_sample)))
