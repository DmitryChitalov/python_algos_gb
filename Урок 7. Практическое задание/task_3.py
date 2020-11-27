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
from statistics import median
import timeit


def lst_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        i = random.choice(lst)
        L = []
        M = []
        R = []
        for el in lst:
            if el < i:
                L.append(el)
            elif el > i:
                R.append(el)
            else:
                M.append(el)
        return lst_sort(L) + M + lst_sort(R)


m = int(input('Введите число m для массива размером 2m + 1: '))
lst_1 = [random.randint(-10, 10) for i in range(2 * m + 1)]
sorted_list = lst_sort(lst_1)
my_md = sorted_list[m]

print(f'Исходный список: {lst_1}')
print(f'Отсортированный список: {sorted_list}')
print(f'Медиана: {my_md}')
print(f'Проверка медианы через statistics: {median(lst_1)}')
print(timeit.timeit('lst_sort(lst_1)',
                    setup='from __main__ import lst_sort,lst_1', number=1000))
print(timeit.timeit('median(lst_1)',
                    setup='from __main__ import median,lst_1', number=1000))

"""#Очень наглядная и лаконичная сортировка
Введите число m для массива размером 2m + 1: 5
Исходный список: [-10, -4, 4, 5, -4, -2, 5, 6, 3, -4, -5]
Отсортированный список: [-10, -5, -4, -4, -4, -2, 3, 4, 5, 5, 6]
Медиана: -2
Проверка медианы через statistics: -2
Замеры по времени 0.015215899999999394
median 0.0008920999999997292 """
# Другими способами не получилось
