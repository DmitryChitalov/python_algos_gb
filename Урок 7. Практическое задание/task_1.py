"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""


from random import randint
from timeit import timeit

#my_list = [randint(-100, 100) for i in range(10)]
my_list = [6, 5, 4, 3, 2, 1, 0]
print(f'Original list is {my_list}.')


# Function with decreasing sorting:

def bubble_sort_decr(lst):
    decrease = True
    while decrease:
        decrease = False
        for i in range(len(lst) - 1):
            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                decrease = True
    return lst

print(f'Decreasing function gets the following list: {bubble_sort_decr(my_list)}')

res_1 = print(round(timeit('bubble_sort_decr(my_list[:])', setup='from __main__ import bubble_sort_decr, my_list', number= 10000), 3))


# Standart bubble sorting:

def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] > lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj

print(f'Increasing - standart - function gets the following list: {bubble_sort(my_list)}')

res_2 = print(round(timeit('bubble_sort(my_list[:])', setup= 'from __main__ import bubble_sort, my_list', number= 10000), 3))

'''
        To sum up:

В моем конкретном случае разница между временем исполнения первой - обратной - и второй - показанной Вами на уроке стандартной
реализацией - есть: она видна во всех случаях в пользу первой - bubble_sort_decr() - функции: 

Decreasing function gets the following list: [93, 89, 82, 76, 21, -8, -51, -60, -84, -90]
0.036
Increasing - standard - function gets the following list: [-90, -84, -60, -51, -8, 21, 76, 82, 89, 93]
0.14

Тоже самое актуально и в случае использования второго - заданного сразу и упорядоченного заранее - списка: здесь уже срабатывает 
улучшение, когда функция bubble_sort_decr() проверяет, нужно ли вообще менять список:

Original list is [6, 5, 4, 3, 2, 1, 0].
Decreasing function gets the following list: [6, 5, 4, 3, 2, 1, 0]
0.025
Increasing - standart - function gets the following list: [0, 1, 2, 3, 4, 5, 6]
0.094
'''


