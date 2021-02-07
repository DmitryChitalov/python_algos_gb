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
from statistics import median
import random

my_list = [random.randint(0, 50) for _ in range(11)]


def find_median(array):
    if len(array) == 1:
        return array[0]
    else:
        max_ind = max(enumerate(array), key=lambda x: x[1])[0]
        array.pop(max_ind)
        min_ind = min(enumerate(array), key=lambda x: x[1])[0]
        array.pop(min_ind)
        return find_median(array)


print(my_list)
print(find_median(my_list))
print(median(my_list))

'''
Использовал рекурсию (очень нравиться) просто удалял по максимальному и минимальному элементу из списка за один проход
Для выхода использовал длинну м ассива в 1 элемент он и будет медианой. 
'''


