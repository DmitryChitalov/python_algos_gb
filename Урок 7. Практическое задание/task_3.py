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


def gnome_sort(lst):
    i = 1
    while i < len(lst):
        if (lst[i - 1] <= lst[i]):
            i += 1
        else:
            lst[i - 1], lst[i] = lst[i], lst[i - 1]
            if i > 1:
                i -= 1
    return lst


"""
попробовал сделать без сортировки, но алгоритм периодически дает сбой на одну позицию, не могу
найти причину, точнее подозреваю что некорректно брать в качестве стартовой точки (переменная
temp_med) среднее значение ряда, в некоторых случаях разбиение на левый и правый список происходит
некорректно
"""


def lst_median(lst):
    temp_med = sum(lst) / len(lst)
    left = []
    right = []
    for el in lst:
        if el <= temp_med:
            left.append(el)
        else:
            right.append(el)
    if (len(left) - len(right)) > 1:
        temp_left = left[-1:-(len(left) - len(right))]
        right.extend(temp_left)
        return max(left)
    elif (len(right) - len(left)) > 1:
        temp_right = right[:(len(right) - len(left))]
        left.extend(temp_right)
        return min(right)
    elif (len(left) - len(right)) == 1:
        return max(left)
    elif (len(right) - len(left)) == 1:
        return min(right)


m = int(input('Введите натруальное число: '))
orig_list = [random.randint(-100, 100) for _ in range(2 * m + 1)]
print(f'Полученный массив размером 2m+1 - {orig_list}')
print(f'Отсортированный массив {gnome_sort(orig_list[:])}')
print(f'Медиана массива, полученная методом сортировки - {gnome_sort(orig_list[:])[m]}')
print(f'Медиана массива - {lst_median(orig_list)}')
print(f'Проверка - {median(orig_list)}')
