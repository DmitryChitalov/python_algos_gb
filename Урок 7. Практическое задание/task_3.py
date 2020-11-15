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


def my_median(lst):
    ARRAY_LENGTH = len(lst)
    for i in range(ARRAY_LENGTH):
        smaller = []
        bigger = []
        for j in range(ARRAY_LENGTH):
            if j != i:
                if lst[j] > lst[i]:
                    bigger.append(lst[j])
                if lst[j] < lst[i]:
                    smaller.append(lst[j])
        if len(smaller) <= ARRAY_LENGTH // 2 and len(bigger) <= ARRAY_LENGTH // 2:
            return lst[i]
    return "Что-то пошло не так"


n = int(input("Введите длину массива: "))
arr = [randint(0, 50) for _ in range((n // 2) * 2 + 1)]
print(f'Исходный массив: {arr}')
print(f'Моя медиана: {my_median(arr)}')
print(f'Штатная медиана: {median(arr)}')
