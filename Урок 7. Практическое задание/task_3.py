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


def median_search(user_list):
    for ind in range(0, len(user_list) - 1):
        left = [i for i in user_list if user_list[ind] <= i]
        right = [i for i in user_list if user_list[ind] >= i]
        if len(right) == len(left):
            median_result = user_list[ind]
            return median_result


input_qty = int(input("введите число (количество элементов будет 2 x число + 1)):"))
input_list = random.sample(range(-100, 100), 2*input_qty + 1)
print(f'исходный список:{input_list}')
list_median = median_search(input_list)
print(f'медиана: {list_median}')

print(f'Проверка с помощью statistics: медиана = {median(input_list)}')


'''
введите число (количество элементов будет 2 x число + 1)):10
исходный список:[4, 85, -60, 64, 72, -71, -79, -92, 34, -91, 90, 65, -99, -35, -63, -45, 6, 73, -3, 46, -89]
медиана: -3
Проверка с помощью statistics: медиана = -3
'''