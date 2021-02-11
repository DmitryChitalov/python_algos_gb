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

import random



def med(arr):
    # находим среднее арифметическое последовательности
    # строим списки слева и справа от среднего арифметического
    average = sum(arr) / len(arr)
    left_lst = [x for x in arr if x < average]
    right_lst = [x for x in arr if x >= average]
    right_lst_len = len(right_lst)
    left_lst_len = len(left_lst)
    inx = left_lst_len - right_lst_len
    # сравниваем длинну списков
    # более длинный список сортируем быстрой сортировкой
    # находим медиану(изначального списка) в более длинном списке(отсортированном)
    # по индексу(разница длинны списков)
    if len(left_lst) > len(right_lst):
        inx = -inx + inx // 2
        return quick_sort(left_lst)[inx]
    else:
        inx = abs(inx) - 1 - abs(inx) // 2
        return quick_sort(right_lst)[inx]

def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr.pop()
        less = [x for x in arr if x < pivot]
        more = [x for x in arr if x >= pivot]
        return quick_sort(less) + [pivot] + quick_sort(more)

lst = [random.randint(0,10) for _ in range(9)]

print(sorted(lst))
print(med(lst))
