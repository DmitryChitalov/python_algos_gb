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


m = random.randint(1, 50)
number_elems = 2*m+1
list = [random.randint(1,10) for _ in range(1, number_elems+1)]

print(list)

def shell(list):
    inc = len(list) // 2
    while inc:
        for i, el in enumerate(list):
            while i >= inc and list[i - inc] > el:
                list[i] = list[i - inc]
                i -= inc
            list[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
    return list

shell(list)
print(list)
print(f'Медиана - {list[m]}')
