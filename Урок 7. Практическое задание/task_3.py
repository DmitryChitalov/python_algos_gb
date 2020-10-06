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
med = sorted_list[m]

print(f'Исходный список: {lst_1}')
print(f'Отсортированный список: {sorted_list}')
print(f'Медиана: {med}')
print(f'Проверка медианы через statistics: {median(lst_1)}')

"""
Введите число m для массива размером 2m + 1: 6
Исходный список: [7, 10, -8, 10, 7, 5, -3, 4, -9, -1, -9, -5, 4]
Отсортированный список: [-9, -9, -8, -5, -3, -1, 4, 4, 5, 7, 7, 10, 10]
Медиана: 4
Проверка медианы через statistics: 4
"""
