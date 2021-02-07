"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным
образом.
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
from statistics import median


def shell_funk(data):
    inc = len(data) // 2
    while inc:
        for i, el in enumerate(data):
            while i >= inc and data[i - inc] > el:
                data[i] = data[i - inc]
                i -= inc
            data[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
    return data


def shell_median_funk(rand_list):
    return shell_funk(rand_list)[len(rand_list) // 2]


m = 10
rand_list = [randint(0, 100) for i in range(2 * m + 1)]
print(f"Исходный список -> {rand_list}")
print(f"Медиана (встроенной функции) -> {shell_funk(rand_list)}")
print(f"Медиана (SHELL) -> {shell_median_funk(rand_list)}")
