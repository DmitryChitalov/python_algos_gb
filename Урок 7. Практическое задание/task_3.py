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


def median(l, half):
    if len(l) == 0:
        return 0
    if len(l) == 1:
        return l[0]

    j = l[0]

    a = []
    b = []
    c = []
    for item in l:
        if item < j:
            a.append(item)
        elif item > j:
            b.append(item)
        else:
            c.append(item)

    if len(a) > half:
        return median(a, half)
    elif len(a) + len(c) > half:
        return c[0]
    else:
        return median(b, half - len(b) - len(c))


n = 5
array = [random.randint(-99, 199) for _ in range(2 * n + 1)]
print(f'Исходный массив {array}')
print(f'Медиана {median(array, n)}')
