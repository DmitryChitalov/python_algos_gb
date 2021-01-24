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
import timeit
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
my_sample = [random.randint(-100, 100) for _ in range(2 * m + 1)]

print('Медиана с сортировкой массива -', my_median(list.copy(my_sample)))
print('Медиана через statistics-', median(list.copy(my_sample)))

print('Время поиска медианы с сортировкой массива: ',
      timeit.timeit("my_median(my_sample[:])", setup="from __main__ import my_median, my_sample", number=100))
print('Время поиска медианы через statistics: ',
      timeit.timeit("median(my_sample[:])", setup="from __main__ import median, my_sample", number=100))

# Результаты поиска медианы с сортировкой и через statistics совпадают, но метод модуля statistics в разы быстрее.
#
# Введите m - 100
# Медиана с сортировкой массива - -9
# Медиана через statistics- -9
# Время поиска медианы с сортировкой массива:  1.615
# Время поиска медианы через statistics:  0.002
