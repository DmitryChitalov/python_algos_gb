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


def medium(nums):
    L = []
    R = []
    med = 0
    c = 0
    while len(R) != 4 or len(R) != 5:
        for i in range(len(nums) - 1):
            med = nums[i]
            if nums[i] < nums[c]:
                L.append(nums[i])
            else:
                R.append(nums[i])
        if len(R) == 4 or len(L) == 5:
            break
        else:
            L = []
            R = []
            c += 1
            continue

    return f'Левый стек {L}, медиана - {med}, правый стек - {R}'


orig_list = [random.randint(0, 100) for i in range(9)]
print(medium(orig_list))

