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


# Гномья сортировка
def gnome_sort(lst_obj):
    i = 1
    j = 2
    while i < len(lst_obj):
        if lst_obj[i-1] < lst_obj[i]:
            i = j
            j += 1
        else:
            lst_obj[i-1], lst_obj[i] = lst_obj[i], lst_obj[i-1]
            i -= 1
            if i == 0:
                i = j
                j += 1
    return lst_obj


def median_gnome_sort(list_num):
    return gnome_sort(list_num)[(len(list_num)//2)]


# Поиск медианы без сортировки
def median_no_sort(list_num):
    arr = sum(list_num) / len(list_num)
    min_num = [i for i in list_num if i < arr]
    max_num = [i for i in list_num if i >= arr]
    while len(min_num) < len(max_num):
        min_num.append(min(max_num))
        max_num.remove(min(max_num))
    while len(max_num) < len(min_num):
        max_num.append(max(min_num))
        min_num.remove(max(min_num))
    if len(min_num) > len(max_num):
        return max(min_num)
    else:
        return min(max_num)


def median_statistics(list_num):
    return median(list_num)


lst_num = [randint(1, 100) for i in range(101)]
print(lst_num)
print(f'Медиана через median_gnome_sort: {median_gnome_sort(lst_num[:])}')
print(f'Медиана через median_no_sort: {median_no_sort(lst_num[:])}')
print(f'Медиана через median_statistics: {median_statistics(lst_num[:])}')
print(f"Время выполнения поиска медианы с помощью Гномьи сортировки: "
      f"{timeit('median_gnome_sort(lst_num[:])','from __main__ import median_gnome_sort, lst_num', number=100)}")
print(f"Время выполнения поиска медианы с помощью функции без сортировки: "
      f"{timeit('median_no_sort(lst_num[:])', 'from __main__ import median_no_sort, lst_num', number=100)}")
print(f"Время выполнения поиска медианы с помощью строенной функции median библиотеки statistics: "
      f"{timeit('median_statistics(lst_num[:])', 'from __main__ import median_statistics, lst_num', number=100)}")


"""
Время выполнения поиска медианы с помощью Гномьи сортировки: 0.17428049999999998
Время выполнения поиска медианы с помощью функции без сортировки: 0.0005668999999999813
Время выполнения поиска медианы с помощью строенной функции median библиотеки statistics: 0.00018290000000004136

Как мы видим, моя функция без сортировки находит медиану намного быстрее, чем через Гномью сортировку.
Но медленней чем через функцию median библиотеки statistics
Еслши посмотреть функцию median, то можно увидеть, что там используется встроенная функция sorted,
то делает поиск очень быстрым.
"""
