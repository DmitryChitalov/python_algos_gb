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

"""
вариант решения без сортитровки
"""
m = 5
orig_list = [random.randint(0, 50) for _ in range(2 * m + 1)]
print(f'Оригинальный массив: {orig_list}')

for i in range(len(orig_list)):
    left = []
    right = []
    for k in range(len(orig_list)):
        if i == k:
            continue
        if orig_list[k] < orig_list[i]:
            left.append(orig_list[k])
        elif orig_list[k] > orig_list[i]:
            right.insert(0, orig_list[k])
        else:
            if len(left) > len(right):
                right.append(orig_list[k])
            else:
                left.insert(0, orig_list[k])
    print(f'Итерация: {i+1}\n\tЛевая часть:  {left}\n\tПравая часть: {right}\n\n')
    if len(left) == len(right) == m:
        print(f'Медиана ====> {orig_list[i]}')
        break
    left.clear()
    right.clear()
