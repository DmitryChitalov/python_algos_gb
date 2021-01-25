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

m = int(input('Задайте m в массиве размера 2m + 1: '))


def list_gen():
    array = [randint(-200, 200) for _ in range(2 * m + 1)]
    return array


def shell_sort(list_obj):
    last_index = len(list_obj) - 1
    step = len(list_obj) // 2
    while step > 0:
        for i in range(step, last_index + 1, 1):
            j = i
            delta = j - step
            while delta >= 0 and list_obj[delta] > list_obj[j]:
                list_obj[delta], list_obj[j] = list_obj[j], list_obj[delta]
                j = delta
                delta = j - step
        step //= 2
    return list_obj


def median_finder(sort_list_obj):
    if sort_list_obj == sorted(sort_list_obj):
        return sort_list_obj[m]
    else:
        return f'Список неотсортирован, медиану определить невозможно.'


data = list_gen()
sort_data = shell_sort(data[:])
print(data)
print(sort_data)
print(median_finder(sort_data))
