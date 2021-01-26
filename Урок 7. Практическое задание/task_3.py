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

m = 5
orig_list = [random.randint(0, 50) for _ in range(2 * m + 1)]

print(f'{orig_list}')

left = []
right = []

for k in range(len(orig_list)):
    if k == 0:
        left.append(orig_list[k])
        continue
    print(f'left => {left}\n right => {right}\n\n')
    if len(left) < len(right):
        i = 0
        while i < len(left):
            if left[i] < orig_list[k]:
                left.insert(i, orig_list[k])
                i += 1
                break
            else:
                left.insert(i+1, orig_list[k])
                i += 1
                break
    else:
        if len(right) == 0:
            right.append(orig_list[k])
            continue
        j = 0
        while j < len(right):
            if right[j] < orig_list[k]:
                right.insert(j, orig_list[k])
                j += 1
                break
            else:
                right.insert(j + 1, orig_list[k])
                j += 1
                break
