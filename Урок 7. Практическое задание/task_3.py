"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. ---- 1
Найдите в массиве медиану. ---- 2
Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива. ---- 3

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, ...  ---- 4 или ---- 3

arr[m]
from statistics import median
"""
from random import randint


# сортировка методом Шелла (источник https://habr.com/ru/post/415935/) ---- 4
# разобрал пошагово дебагером
def shell(lst_obj):
    inc = len(lst_obj) // 2
    while inc:
        for i, j in enumerate(lst_obj):
            while i >= inc and lst_obj[i - inc] > j:
                lst_obj[i] = lst_obj[i - inc]
                i -= inc
            lst_obj[i] = j
        inc = 1 if inc == 2 else int(inc * 5 / 11)
    return f'Отсортированный список {lst_obj}\n' \
           f'Медиана {lst_obj[len(lst_obj) // 2]}'  # поиск медианы ---- 2


m = 7
random_list = [randint(0, 100) for _ in range(2 * m + 1)]
print(f'Исходный список: {random_list}')
print(shell(random_list))

"""
Результат:

Исходный список: [95, 21, 2, 19, 59, 7, 43, 74, 95, 30, 0, 58, 45, 37, 62]
Отсортированный список [0, 2, 7, 19, 21, 30, 37, 43, 45, 58, 59, 62, 74, 95, 95]
Медиана 43
"""