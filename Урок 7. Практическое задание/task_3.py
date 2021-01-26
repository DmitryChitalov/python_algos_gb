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
import heapq

m = input("Введите число: ")

my_list = [random.randint(0, 100) for _ in range((2 * int(m) + 1))]
my_list_2 = my_list[:]
print(f"Исходный массив {my_list}")


def gnome(data):
    i, size = 1, len(data)
    while i < size:
        if data[i - 1] <= data[i]:
            i += 1
        else:
            data[i - 1], data[i] = data[i], data[i - 1]
            if i > 1:
                i -= 1
    return data


print(f"Отсортированный массив {gnome(my_list)}")
print(f"Левая часть {my_list[:int(m)]}, правая часть {my_list[int(m)+1 :]} \n")

print(f"Разделим по медиане следующий массив {my_list_2}")

my_heap = my_list_2
heapq.heapify(my_heap)
left = []

for x in range(int(m)):
    left.append(heapq.heappop(my_heap))

median = heapq.heappop(my_heap)

print(f"Левая часть {left}, правая часть {my_heap}")