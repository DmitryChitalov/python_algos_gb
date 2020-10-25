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

m = int(input('Enter a natural number: '))
lst_size = 2 * m + 1
lst = [random.randint(0, 100) for _ in range(lst_size)]


def median(lst_obj):
    sorted_lst = sorted(lst_obj)
    index = (len(lst_obj) - 1) // 2
    return f'Median - {sorted_lst[index]}'


# Верся 2 для возможность чётного числа элементов в списке.
def median_v2(lst_object):
    sorted_lst_obj = sorted(lst_object)
    index = (len(lst_object) - 1) // 2
    if index % 2:
        return f'Median - {sorted_lst_obj[index]}'
    return f'Median - {(sorted_lst_obj[index] + sorted_lst_obj[index + 1]) / 2}'


print(lst)
print(f'Sorted - {sorted(lst)}')
print(median(lst))
