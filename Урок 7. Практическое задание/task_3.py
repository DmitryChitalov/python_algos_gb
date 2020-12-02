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
from random import randint


def first_metod(unsorted_list: list):
    temp = unsorted_list
    left_half = []
    right_half = []

    for i in range(len(temp)):
        for j in range(len(temp)):
            if temp[i] < temp[j]:
                right_half.append(temp[j])
            elif temp[i] > temp[j]:
                left_half.append(temp[j])
            elif temp[i] == temp[j] and i < j:
                right_half.append(temp[j])
            elif temp[i] == temp[j] and i > j:
                left_half.append(temp[j])
            else:
                pass
        if len(left_half) == len(right_half):
            return temp[i]
        left_half.clear()
        right_half.clear()


def second_metod(unsorted_list: list, m):
    inc = len(unsorted_list) // 2
    while inc:
        for i, el in enumerate(unsorted_list):
            while i >= inc and unsorted_list[i - inc] > el:
                unsorted_list[i] = unsorted_list[i - inc]
                i -= inc
            unsorted_list[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
    return unsorted_list[m]


m = int(input('Введите m: '))
find_list = [randint(0, 100) for i in range(2 * m + 1)]
print(f'Список для поиска: {find_list}')

print(f'Встроеная функция: {median(find_list)}')
print(f'Способ без сортировки: {first_metod(find_list)}')
print(f'Способ c сортировкой: {second_metod(find_list, m)}')

'''
Способ без сортировки я уже знал. Решал подобную задачу в универе.
Нашел сортировку Шелла и разобрался в её принцие работы.
'''
