"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.

Задачу можно решить без сортировки исходного массива.
Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках: Шелла, Гномья

arr[m]
from statistics import median
"""
from statistics import median
import random
import timeit


def gnome_opt(data):
    i, j, size = 1, 2, len(data)
    while i < size:
        if data[i - 1] <= data[i]:
            i, j = j, j + 1
        else:
            data[i - 1], data[i] = data[i], data[i - 1]
            i -= 1
            if i == 0:
                i, j = j, j + 1
    return data


m = int(input('Введите медиану: '))
orig_list = [random.randint(0, 1000) for _ in range(2 * m + 1)]

print(f'Исходный массив: {orig_list}')
print(f'Медиана через гномью сортировку - {gnome_opt(orig_list)[m]}')
print(f'Медиана через встроенную функцию - {median(orig_list)}')

print(timeit.timeit("gnome_opt(orig_list[:])", setup="from __main__ import gnome_opt, orig_list", number=1000))
print(timeit.timeit("median(orig_list[:])", setup="from __main__ import median, orig_list", number=1000))

"""
Результат для m = 50
0.01497614299999972
0.0017349339999999103

Результат для m = 7
0.0024201500000002873
0.0005657139999999394

Встроенная функция выполняется на порядок быстрее гномьей (даже оптимизированной версии)
"""