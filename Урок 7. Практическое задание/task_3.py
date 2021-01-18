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
from timeit import timeit

a = [randint(1, 100) for i in range(2 * 50 + 1)]
b = [randint(1, 100) for i in range(2 * 50 + 1)]


def get_median(a):
    for i in a:
        middle = i
        more = 0
        less = 0
        for i in a:
            if i > middle:
                more += 1
            elif i < middle:
                less += 1
        if abs(more - less) > a.count(middle):
            continue
        else:
            return middle


print(f'{get_median(a)} - медиана без сортировки, {median(a)} - проверка')


print(timeit('get_median(a)', 'from __main__ import a, get_median', number=5000))
# 0.1659759
print(timeit('median(a)', 'from __main__ import a, median', number=5000))
# 0.01979049999999999
# Удалось сделать без сортировки :) но очень медленно

def gnome(data):
    data = data.copy()
    i, size = 1, len(data)
    while i < size:
        if data[i - 1] <= data[i]:
            i += 1
        else:
            data[i - 1], data[i] = data[i], data[i - 1]
            if i > 1:
                i -= 1
    return data[len(data) // 2]


def gnome_opt(data):
    """J позволяет вернуться в последнюю точку, где была проведена сортировка,
    вместо пробега с начала массива"""
    data = data.copy()
    i, j, size = 1, 2, len(data)
    while i < size:
        if data[i - 1] <= data[i]:
            i, j = j, j + 1
        else:
            data[i - 1], data[i] = data[i], data[i - 1]
            i -= 1
            if i == 0:
                i, j = j, j + 1
    return data[len(data) // 2]

print(f'{gnome(a)} - медиана через Гномью сортировку, {median(a)} - проверка')
print(f'{gnome_opt(b)} - медиана через оптимизированную Гномью сортировку, '
      f'{median(b)} - проверка')
print(timeit('gnome(a)', 'from __main__ import gnome, a', number=5000))
# 3.0690264
print(timeit('gnome_opt(b)', 'from __main__ import gnome_opt, b', number=5000))
# 2.6371153