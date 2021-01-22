"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках
"""

import copy
import timeit
from random import randint
from statistics import median


def without_sort(lst_obj):
    temp = lst_obj
    left_list = []
    right_list = []
    for i in range(len(temp)):
        for j in range(len(temp)):
            if temp[i] > temp[j]:
                left_list.append(temp[j])
            if temp[i] < temp[j]:
                right_list.append(temp[j])
            if temp[i] == temp[j] and i > j:
                left_list.append(temp[j])
            if temp[i] == temp[j] and i < j:
                right_list.append(temp[j])
        if len(left_list) == len(right_list):
            return temp[i]
        left_list.clear()
        right_list.clear()


def gnome_sort(sort_list):
    """
    Сортировка списка методом gnome_sort
    """
    i = 1
    while i < len(sort_list):
        if not i or sort_list[i - 1] <= sort_list[i]:
            i += 1
        else:
            sort_list[i], sort_list[i - 1] = sort_list[i - 1], sort_list[i]
            i -= 1
    return sort_list


def another_way(lst_obj):
    """
    Возвращает медиану массива путем удаления максимальных элементов,
    пока максимальным не будет медиана.
    """
    temp_list = lst_obj
    for i in range(len(lst_obj) // 2):
        temp_list.remove(max(temp_list))
    return max(temp_list)





def gnome_median(sort_list):
    return gnome_sort(sort_list)[len(sort_list) // 2]


m = int(input('Введите m: '))
orig_list = [randint(0, 100) for i in range(2 * m + 1)]
print(f'Исходный массив:\n{orig_list}\n')


# Нахождение медианы через встроенную функцию
print(f'Медиана - {median(orig_list)}')
# Нахождение медианы без сортировки исходного массива
print(f'Медиана (без сортировки) - {without_sort(orig_list)}')
# Нахождение медианы еще одним вариантом без сортировки исходного массива
print(f'Медиана (без сортировки) - {another_way(orig_list)}')
# Нахождение медианы с сортировкой исходного массива
print(f'Медиана (с сортировкой) - {gnome_sort(orig_list)[m]}')

print(timeit.timeit("median(orig_list[:])", setup="from __main__ import orig_list, median", number=10000))
#print(timeit.timeit("without_sort(orig_list[:])", setup="from __main__ import orig_list, without_sort", number=10000))
#print(timeit.timeit("another_way(orig_list[:])", setup="from __main__ import orig_list, another_way", number=10000))
print(timeit.timeit("gnome_sort(orig_list[:])", setup="from __main__ import orig_list, gnome_sort", number=10000))

"""
Замеры на моём компьютере [краткий вывод - без сортировки плохо, встроенная функция работает лучше всего].

m = 10

0.14261296600000062
2.3400350239999987
0.34022327100000105
0.1573166239999999

m = 100
0.03330660400000074
53.670766265000005
4.740386803
0.536520080999999

m = 1000    #не хватило терпения дождаться результата
0.21938380599999974
больше десяти минут
---
---
"""


