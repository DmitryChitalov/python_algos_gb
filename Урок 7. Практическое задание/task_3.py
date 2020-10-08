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
from random import randint, choice
from statistics import median

nums = int(input('Введите m, для массива 2m + 1: '))
orig_list = [randint(-100, 100) for _ in range(2 * nums + 1)]
print(f'(проверка через median) Медиана списка {orig_list} равна {median(orig_list)}')
print("*" * 30)

def mediana_lst(lst):
    if len(lst) <= 1:
        return lst
    else:
        i = choice(lst)
        L = []
        M = []
        R = []
        for el in lst:
            if el < i:
                L.append(el)
            elif el > i:
                R.append(el)
            else:
                M.append(el)
        return mediana_lst(L) + M + mediana_lst(R)

sorted_list = mediana_lst(orig_list)
med = sorted_list[nums]

print(f'Исходный список: {orig_list}')
print(f'Отсортированный список: {sorted_list}')
print(f'Медиана: {med}')