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

import statistics
import random

def median(lst, m):
    start = True
    while start:
        med_el = lst[m]
        left = []
        right = []
        for el in lst[:m]:
            if el <= lst[m]:
                left.append(el)
            else:
                right.append(el)
        for el in lst[m+1:]:
            if el >= lst[m]:
                right.append(el)
            else:
                left.append(el)
        if len(left) == len(right):
            start = False
        else:
            lst = left + [lst[m]] + right
    return med_el



m = int(input('Введите m для построения массива длиной 2m+1: '))
my_lst = [random.randrange(0, 100) for _ in range(2*m+1)]

print('Массив: ', my_lst)
print('Медиана равна: ', median(my_lst, m))
print('Проверка: ', statistics.median(my_lst))
