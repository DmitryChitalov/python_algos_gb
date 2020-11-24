"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, ...

arr[m]
from statistics import median
"""

from statistics import median
import random
import timeit


def gnome(lst_obj):
    n = 1
    while n < len(lst_obj):
        if lst_obj[n - 1] <= lst_obj[n]:
            n += 1
        else:
            lst_obj[n - 1], lst_obj[n] = lst_obj[n], lst_obj[n - 1]
            if n > 1:
                n -= 1
    return lst_obj


def find_median():
    number = int(input('Введите число: '))
    orig_list = [random.randint(-100, 100) for _ in range(2 * number + 1)]
    sorted_list = gnome(orig_list)  # передаем функции gnome рандомный массив, и получаем отсортированный массив
    return f'Медианна массива {sorted_list} это число {sorted_list[number]}'  # медианна - число number в
    # отсортированном массиве


print(find_median())

number_2 = int(input('Введите число: '))
orig_list_2 = [random.randint(-100, 100) for _ in range(2 * number_2 + 1)]
print(f'Медианна для сравнения с результатом работы функции:  {median(orig_list_2)}')


def search_median_brute_force(unsorted_list):
    for i in range(len(unsorted_list)):
        left, right = [], []  # обнуляем списки каждый раз в случае если left != right
        for j in range(len(unsorted_list)):
            if i == j:
                continue
            if unsorted_list[j] <= unsorted_list[i]:
                left.append(unsorted_list[j])
                continue
            if unsorted_list[j] >= unsorted_list[i]:
                right.append(unsorted_list[j])
                continue
        if len(left) == len(right):
            return f'Медианна массива {unsorted_list} это число {unsorted_list[i]}'


print(search_median_brute_force(orig_list_2))

orig_list_time = [random.randint(-100, 100) for _ in range(11)]
orig_list_time_2 = orig_list_time[:]

print('\nВремя работы функции gnome 10, 100 и 1000 повторов:\n')

print(timeit.timeit("gnome(orig_list_time[:])",
                    setup="from __main__ import gnome, orig_list_time", number=10))

print(timeit.timeit("gnome(orig_list_time[:])",
                    setup="from __main__ import gnome, orig_list_time", number=100))

print(timeit.timeit("gnome(orig_list_time[:])",
                    setup="from __main__ import gnome, orig_list_time", number=1000))

print('\nВремя работы функции search_median_brute_force 10, 100 и 1000 повторов:\n')

print(timeit.timeit("search_median_brute_force(orig_list_time_2[:])",
                    setup="from __main__ import search_median_brute_force, orig_list_time_2", number=10))

print(timeit.timeit("search_median_brute_force(orig_list_time_2[:])",
                    setup="from __main__ import search_median_brute_force, orig_list_time_2", number=100))

print(timeit.timeit("search_median_brute_force(orig_list_time_2[:])",
                    setup="from __main__ import search_median_brute_force, orig_list_time_2", number=1000))

"""Использовал метод Гномья, с его помощью происходит сортировка массива.
И потом в полученном массиве выводим на печать число с индексом номера (n), которое вводит пользователь и которое
используется в формуле 2 * n + 1. Получаем сложность от O(n) в лучшем случае, до O(n**2) в худшем.

Второй способ без сортировки - перебираем числа, и сравниваем. Если число больше или равно - вправо, 
если меньше или равно - влево.
При получении одинаковых по длине списков - видим медианну, если списки не равны, тогда заходим на новый цикл.
Здесь моя функция на малых числах (напр. массив из 5 элементов - быстрее), но при увеличении длины массива - 
скорость падает (примерно в 2 раза), но бывают случаи, когда она отрабатывает быстрее и при большом массиве.

Также добавил проверку - для получения медианы (из median) - печатает в консоли число, нигде больше не используется.

Также у моей функции есть серьезные недостатки - на рандомном списке работает хорошо, но если список состоит из 
повторяющихся элементов (1, 2, 2, 2, 2) и подобных - она не возвращает медиану.
Связано с тем, что в условиях стоит <= и >=, поэтому добавляет все в один из списков.
Жду урока, чтобы посмотреть оптимальное решение."""
