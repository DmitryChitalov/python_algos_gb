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
from random import randint
from statistics import median


def get_median(lst):
    """Без сортировки"""
    for x in lst:
        left = 0
        right = 0
        for y in lst:
            if x >= y:
                left += 1
            else:
                right += 1
        if left >= len(lst) // 2 and right == len(lst) // 2:
            return x


def gnome_sort(lst):
    """Гномья сортировка"""
    i = 1
    j = 2
    while i < len(lst):
        if lst[i - 1] > lst[i]:
            i = j
            j += 1
        else:
            lst[i - 1], lst[i] = lst[i], lst[i - 1]
            i = i - 1
            if i == 0:
                i = j
                j = j + 1

    return lst


def shell(lst):
    """Cортировка Шелла"""
    inc = len(lst) // 2
    while inc:
        for i, el in enumerate(lst):
            while i >= inc and lst[i - inc] > el:
                lst[i] = lst[i - inc]
                i -= inc
            lst[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)

    return lst


if __name__ == "__main__":
    m = randint(1, 10)
    lst_obj = [randint(0, 50) for _ in range(2 * m + 1)]

    print(f'Исходный - {lst_obj}, где m = {m}')
    print('Без сортировки:', get_median(lst_obj[:]))
    print('Медиана по Гномьей сортировка:', gnome_sort(lst_obj[:])[m])
    print('Медиана по сортировки Шелла:', shell(lst_obj[:])[m])
    print('Встренная функция:', median(lst_obj[:]))
