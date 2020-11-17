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


from random import random
from statistics import median


def find_median(lst_obj):
    for i in range(len(lst_obj)):
        left = []
        right = []
        for k in range(len(lst_obj)):
            if lst_obj[i] > lst_obj[k]:
                left.append(lst_obj[k])
            if lst_obj[i] < lst_obj[k]:
                right.append(lst_obj[k])
            if lst_obj[i] == lst_obj[k]:
                if i > k:
                    left.append(lst_obj[k])
                if i < k:
                    right.append(lst_obj[k])
        if len(left) == len(right):
            return lst_obj[i]



m = int(input('Построим массив длиной 2m + 1. Введите m '))
my_list = [float('{:.4f}'.format(random() * 100)) for _ in range(m)]
print(my_list)

print(find_median(my_list)) # рабочая функция
print(median(my_list)) # для проверки



