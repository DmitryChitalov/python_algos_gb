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

# Сортировка массива методом Шелла
def shell(data):
    inc = len(data) // 2
    while inc:
        for i, el in enumerate(data):
            while i >= inc and data[i - inc] > el:
                data[i] = data[i - inc]
                i -= inc
            data[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
    return data

m = int(input("Введите натуральное число m: "))
orig_list = [random.randint(-10, 10) for i in range((2 * m) + 1)]
print(f'Исходный массив: {orig_list}')
print(f'Отсортированный массив: {shell(orig_list)}')

# Находим медиану в отсортированном массиве методом Шелла
def shell_med(sort_list):
    return shell(sort_list)[len(sort_list) // 2]
print(f'Медиана отсортированного массива: {shell_med(orig_list)}')
print(timeit.timeit("shell_med(orig_list[:])", setup="from __main__ import orig_list, shell_med", number=10000))


# Находим медиану через встроенную функцию
print(f'Медиана через встроенную ф-цию: {median(orig_list)}')
print(timeit.timeit("median(orig_list[:])", setup="from __main__ import orig_list, median", number=10000))

""" Встроенная функция поиска медианы работает значительно быстрее, 
чем поиск через сортировку массива
"""
