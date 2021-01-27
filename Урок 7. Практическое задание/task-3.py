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
from random import randint
from statistics import median

n = randint(0, 9)
my_list = [random.randint(-1000, 1000) for _ in range(2 * n + 1)]


def shell(my_list):
    inc = len(my_list) // 2
    while inc:
        for i, el in enumerate(my_list):
            while i >= inc and my_list[i - inc] > el:
                my_list[i] = my_list[i - inc]
                i -= inc
            my_list[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
    mediana = my_list[len(my_list) // 2]
    print(f'Отсортированный список - {my_list}\nМедиана - {mediana}')


print(f'Исходный список - {my_list}')
shell(my_list)


