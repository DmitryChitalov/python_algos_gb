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

random_list = [randint(0, 10) for _ in range(9)]


def find_median(in_list: list):
    left = []
    right = []

    # Без сортировки
    while len(in_list) != 1:
        left.append(in_list.pop(in_list.index(min(in_list))))
        right.append(in_list.pop(in_list.index(max(in_list))))
    return in_list[0]


print(f'Исходный массив: {random_list}')
print(f'Медиана от встроенной функции: {median(random_list)}')
print(f'Медиана от кастомной функции: {find_median(random_list[:])}')
print(f'Отсортированный массив: {sorted(random_list)}')
