"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные по длине части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, Кучей...
"""

import timeit
from random import randint
from statistics import median


def med_max(lst):
    """
    Возвращает медиану массива путем удаления максимальных элементов
    """
    temp_lst = lst
    for i in range(len(lst) // 2):
        temp_lst.remove(max(temp_lst))
    return max(temp_lst)


def shell_sort(lst):
    inc = len(lst) // 2
    while inc:
        for i, el in enumerate(lst):
            while i >= inc and lst[i - inc] > el:
                lst[i] = lst[i - inc]
                i -= inc
            lst[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
    return lst


m = int(input('Введите m: '))
orig_list = [randint(0, 100) for i in range(2 * m + 1)]
print(f'Исходный массив:\n{orig_list}\n')

# Нахождение медианы через встроенную функцию
print(f'Медиана - {median(orig_list)}')
# Нахождение медианы без сортировки исходного массива
print(f'Медиана (без сортировки) - {med_max(orig_list)}')
# Нахождение медианы с сортировкой исходного массива
print(f'Отсортированный массив:\n{shell_sort(orig_list)}\n')
print(f'Медиана (с сортировкой) - {shell_sort(orig_list)[m]}')

print(
    timeit.timeit(
        "median(orig_list[:])",
        globals=globals(),
        number=10000))
print(
    timeit.timeit(
        "med_max(orig_list[:])",
        globals=globals(),
        number=10000))
print(
    timeit.timeit(
        "shell_sort(orig_list[:])",
        globals=globals(),
        number=10000))

"""
m = 10

0.0248905370000001
0.04254194699999969
0.03543447899999963

m = 100
0.02742031899999997
0.8384630439999996
0.38131935000000006

m = 1000
0.08780161100000017
68.886945595
6.989293513999996
"""