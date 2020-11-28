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
from random import sample
import timeit
m = 10
my_list_no_sort = sample(range(0, 100), 2*m + 1)
# my_list_no_sort = [80, 40, 70, 22, 93, 46, 82, 2, 8, 84, 75, 98, 14, 1, 77, 59, 72, 12, 88, 9, 27]


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
    return data


my_list_sort = gnome(my_list_no_sort)
print(f'Список без сортировки  - {my_list_no_sort}')
print(f'Результаты Гномьей сортировки - {my_list_sort}')
print(f'Медиана - {my_list_sort[(len(my_list_sort) // 2)]}')
print(f'Время выполнения сортировки гномья - '
      f'{timeit.timeit("gnome(my_list_no_sort)",setup="from __main__ import gnome, my_list_no_sort", number=10000)}')
