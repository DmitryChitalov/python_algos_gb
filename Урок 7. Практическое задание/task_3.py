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
from random import randint


def get_median(lst: list):
    elements_count = len(lst)
    for global_pass_index in range(elements_count):
        left_half_count, right_half_count, equals_count = 0, 0, 0
        for local_pass_index in range(elements_count):
            if local_pass_index == global_pass_index:
                # пропускаем т.к. мы не берём в расчёт текущий элемент (тот, что с индексом global_pass_index)
                continue
            if lst[local_pass_index] > lst[global_pass_index]:
                left_half_count += 1
            if lst[local_pass_index] < lst[global_pass_index]:
                right_half_count += 1
            if lst[local_pass_index] == lst[global_pass_index] and global_pass_index > local_pass_index:
                left_half_count += 1
            if lst[local_pass_index] == lst[global_pass_index] and global_pass_index < local_pass_index:
                right_half_count += 1
        if left_half_count == right_half_count:
            return lst[global_pass_index]
    return None


m = 500
list1 = [randint(0, 100) for _ in range(2 * m + 1)]
print('get_median:', get_median(list1))
print('statistics.median:', median(list1))
