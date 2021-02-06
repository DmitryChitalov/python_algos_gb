"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные по длине части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, Кучей...

[5, 3, 4, 3, 3, 3, 3]

[3, 3, 3, 3, 3, 4, 5]

my_lst
new_lts

arr[m]


from statistics import median

[3, 4, 3, 3, 5, 3, 3]


left.clear()
right.clear()


m = 3
len = 7
i
left = []
right = []

left == right and

for i in
    for
    left == right
    left.clear()
    right.clear()


"""
from statistics import median
import random


# Нахождение медианы без сортировки
def my_median(l_obj):
    len_obj = len(l_obj)
    middle = len_obj // 2
    for i in range(len_obj):
        left = [el for el in l_obj if el <= l_obj[i]]
        right = [el for el in l_obj if el >= l_obj[i]]
        if (len(left) > middle and len(right) > middle) or (len(left) == middle and len(right) == middle):
            return l_obj[i]


# Нахождение медианы с предварительной гномьей сортировкой
def gnome(data):
    i, size = 1, len(data)
    while i < size:
        if data[i - 1] <= data[i]:
            i += 1
        else:
            data[i - 1], data[i] = data[i], data[i - 1]
            if i > 1:
                i -= 1
    return data, data[size//2]


# Список на нахождение медианы и результаты
orig_list = [random.randint(0, 100) for _ in range(21)]
gnome_list, gnome_med = gnome(orig_list)
print(orig_list)
print("Медиана, найденная средствами Python", median(orig_list))
print("Медиана, найденная my_median", my_median(orig_list))
print("Список с 'гномьей' сортировкой", gnome_list)
print("Медиана с 'гномьей' сортировкой", gnome_med)
