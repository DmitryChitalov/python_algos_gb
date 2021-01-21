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


def gnome_sort(orig_list):
    i = 1
    while i < len(orig_list):
        if not i or orig_list[i - 1] <= orig_list[i]:
            i += 1
        else:
            orig_list[i], orig_list[i - 1] = orig_list[i - 1], orig_list[i]
    return orig_list


def median(orig_list):
    return gnome_sort(orig_list)[len(orig_list) // 2]


m = int(input('Введите m: '))

orig_list = [random.randint(0, 100) for i in range(2 * m + 1)]
print(f'Исходный массив {orig_list}')
print(f'Медиана {median(orig_list)}')
