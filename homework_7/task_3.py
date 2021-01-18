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

def shell(seq):
    inc = len(seq) // 2
    while inc:
        for i, el in enumerate(seq):
            while i >= inc and seq[i - inc] > el:
                seq[i] = seq[i - inc]
                i -= inc
            seq[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)

m = int(input('Введите число m: '))
n = 2*m + 1
data= [random.uniform(0, 50) for _ in range(n)]
shell(data)
print(data)

median = data[len(data) // 2]
print(median)