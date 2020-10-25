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


def gnome_sort(lst_obj):
    i, size = 1, len(lst_obj)
    while i < size:
        if lst_obj[i - 1] <= lst_obj[i]:
            i += 1
        else:
            lst_obj[i - 1], lst_obj[i] = lst_obj[i], lst_obj[i - 1]
            if i > 1:
                i -= 1
    return f'Гномья: {lst_obj}, Медиана {median(lst_obj)}'


def shell_sort(lst_obj):
    inc = len(lst_obj) // 2
    while inc:
        for i, el in enumerate(lst_obj):
            while i >= inc and lst_obj[i - inc] > el:
                lst_obj[i] = lst_obj[i - inc]
                i -= inc
            lst_obj[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
    return f'Шелла: {lst_obj}, Медиана {median(lst_obj)}'


def get_median(lst_obj):
    return f'Человеческая: {sorted(lst_obj)}, Медиана {median(lst_obj)}'


lst = [randint(-100, 100) for i in range(2 * int(input('Введите m для построения списка 2m + 1: ')) + 1)]
print(f'Исходный список: {lst}')
print(gnome_sort(lst.copy()))
print(shell_sort(lst.copy()))
print(get_median(lst.copy()))