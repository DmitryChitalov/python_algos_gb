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
"""
from statistics import median
import random
import copy


def gnome(data):
    i, size = 1, len(data)
    while i < size:
        if data[i - 1] <= data[i]:
            i += 1
        else:
            data[i - 1], data[i] = data[i], data[i - 1] 
            if i > 1:
                i -= 1    

    index = (len(data) - 1) // 2    
    if len(data) % 2 == 1:
        median = data[index]
    else:
        median = (data[index] + data[index + 1])/2.0
    return median

orig_list = [random.randint(-100, 100) for _ in range(10)]
new_list = copy.copy(orig_list)
print(orig_list)
print(gnome(new_list))
print(median(new_list))