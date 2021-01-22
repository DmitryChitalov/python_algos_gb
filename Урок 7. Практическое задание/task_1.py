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

from timeit import timeit
from random import randint

test_list = [randint(-100,100) for _ in range(10)]


def bubble_sort(my_list):
    for k in range(1, len(my_list)):
        have_change = 0
        for i in range(len(my_list)-k):
            if my_list[i] < my_list[i+1]:  # здесь мы реализуем сортировку по убыванию
                my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
                have_change = 1
        if have_change == 0:  # условие выхода если список отсортирован
            break
    return f'Sorted list   {my_list}'


print(f'Unsorted list {test_list}')

print(timeit("bubble_sort(test_list[:])", setup="from __main__ import bubble_sort, test_list", number=1000))

print(bubble_sort(test_list))  # Запуск функции для того, чтобы при последующих замерах список был отсортирован

print(timeit("bubble_sort(test_list[:])", setup="from __main__ import bubble_sort, test_list", number=1000))

"""
Результаты:
    Unsorted list [12, 53, -94, 94, -75, 72, 82, -72, -16, 3]
    0.011407727999999995
    Sorted list   [94, 82, 72, 53, 12, 3, -16, -72, -75, -94]
    0.0029929969999999972
Мы видим, что если список уже отсортирован то происходит существенное сокращение времени исмполнения функции
"""