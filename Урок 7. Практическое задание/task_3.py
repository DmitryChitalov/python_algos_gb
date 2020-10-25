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
import timeit
import random

orig_list = [random.randint(0, 100) for _ in range(2*int(input("Введите число m: ")) + 1)]
print(orig_list)


def cocktail_sort(lst_obj):
    left = 0
    right = len(lst_obj) - 1
    while left <= right:
        for i in range(left, right):
            if lst_obj[i] > lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        right -= 1
        for i in range(right, left, -1):
            if lst_obj[i-1] > lst_obj[i]:
                lst_obj[i], lst_obj[i-1] = lst_obj[i-1], lst_obj[i]
        left += 1
    return lst_obj


sorted_list = cocktail_sort(orig_list)
print(sorted_list)
m = len(sorted_list) // 2
print(f"медиана: {sorted_list[m]}")

