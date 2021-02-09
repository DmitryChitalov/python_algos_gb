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
from statistics import median


def shell(seq):
    inc = len(seq) // 2
    while inc:
        for i, el in enumerate(seq):
            while i >= inc and seq[i - inc] > el:
                seq[i] = seq[i - inc]
                i -= inc
            seq[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
    return seq


def shell_median(list_sort):
    return shell(list_sort)[len(list_sort) // 2]


m = 10
list_sort = [randint(0, 100) for i in range(2 * m + 1)]
print(f'Начальный список: {list_sort}')
print(f'После сортировки:  {shell(list_sort)}')
print(f'Медиана:  {shell_median(list_sort)}')

"""
Изспользвоал метод сортировки SHELL и расчет медианы. 

"""
