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
import random
import timeit


def gnome_sort(our_list):
    k = 1
    while k < len(our_list):
        if not k or our_list[k] >= our_list[k - 1]:
            k += 1
        else:
            our_list[k], our_list[k - 1] = our_list[k - 1], our_list[k]
            k -= 1
    return our_list


def gnome_median(our_list):
    return gnome_sort(our_list)[len(our_list) // 2]


m = int(input('Введите m: '))
list_sort = [random.randint(0, 100) for _ in range(2 * m + 1)]
print(f'Исходный массив: {list_sort}')

print(f'Через встроенную - {median(list_sort)}')
print(f'Через сортировку Гномья - {gnome_median(list_sort)}')

print(timeit.timeit('median(list_sort[:])',
                    setup='from __main__ import list_sort, median',
                    number=1000))

print(timeit.timeit('gnome_median(list_sort[:])',
                    setup='from __main__ import list_sort, gnome_median',
                    number=1000))


"""
Введите m: 2
Исходный массив: [40, 30, 9, 100, 64]
Через встроенную - 40
Через сортировку Гномья - 40
0.0003527000000005387
0.0008078000000004693
"""