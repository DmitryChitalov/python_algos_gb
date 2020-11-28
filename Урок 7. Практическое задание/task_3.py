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


"""
Решение Шеллом
"""

import random
m = random.randrange(0, 6)
my_list = [random.randrange(0, 100) for i in range(2*m + 1)]
print(my_list)
inc = len(my_list) // 2
print(inc)
while inc:
    for i, el in enumerate(my_list):
        while i >= inc and my_list[i - inc] > el:
            my_list[i] = my_list[i - inc]
            i -= inc
        my_list[i] = el
    inc = 1 if inc == 2 else int(inc * 5.0 // 11)
print(my_list)
middle = len(my_list)
if middle % 2 == 0:
    middle = len(my_list) // 2
else:
    middle = (len(my_list) // 2) + 1
counter = 0
for j in my_list:
    counter = counter + 1
    if counter == middle:
        print(j)



""" Мне, все же, более понятной показалась сортировка вставками. Вот решение через вставки"""
m = random.randrange(0, 6)
my_list = [random.randrange(0, 100) for i in range(2*m + 1)]
print(my_list)
for i in range(len(my_list)):
    k = my_list[i]
    z = i
    while (my_list[z-1] > k) and (z > 0):
        my_list[z] = my_list[z - 1]
        z = z - 1
        my_list[z] = k
print(my_list)
middle = len(my_list)
if middle % 2 == 0:
    middle = len(my_list) // 2
else:
    middle = (len(my_list) // 2) + 1
counter = 0
for j in my_list:
    counter = counter + 1
    if counter == middle:
        print(j)



