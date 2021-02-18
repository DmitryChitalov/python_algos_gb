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

import timeit
import random


random_list = [random.randint(-100, 100) for _ in range(10)]
random_list_2 = random_list[:]


def bubble_sort(lst_obj):
    random_list_copy = lst_obj[:]
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return f'Исходный массив: {random_list_copy}\nOтсортированный массив: {lst_obj}'


print('Время работы функции без доработки 10, 100 и 1000 повторов:\n')
# замеры 10
print(timeit.timeit("bubble_sort(random_list[:])",
                    setup="from __main__ import bubble_sort, random_list", number=10))

# замеры 100
print(timeit.timeit("bubble_sort(random_list[:])",
                    setup="from __main__ import bubble_sort, random_list", number=100))

# замеры 1000
print(timeit.timeit("bubble_sort(random_list[:])",
                    setup="from __main__ import bubble_sort, random_list", number=1000))


def bubble_sort_2(lst_obj):
    random_list_copy = lst_obj[:]
    n = 1
    while n < len(lst_obj):
        number_of_passes = 0
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                number_of_passes += 1
        if number_of_passes == 0:
            break
        n += 1
    return f'Исходный массив: {random_list_copy}\nOтсортированный массив: {lst_obj}'


print('\nВремя работы функции c доработкой 10, 100 и 1000 повторов:\n')
# замеры 10
print(timeit.timeit("bubble_sort_2(random_list_2[:])",
                    setup="from __main__ import bubble_sort_2, random_list_2", number=10))

# замеры 100
print(timeit.timeit("bubble_sort_2(random_list_2[:])",
                    setup="from __main__ import bubble_sort_2, random_list_2", number=100))

# замеры 1000
print(timeit.timeit("bubble_sort_2(random_list_2[:])",
                    setup="from __main__ import bubble_sort_2, random_list_2", number=1000))
print()
if __name__ == "__main__":
    print(bubble_sort(random_list))
    print(bubble_sort_2(random_list_2))

""" 
Время работы функции без доработки 10, 100 и 1000 повторов:

0.00010820000000000274
0.0010041000000000008
0.009863399999999998

Время работы функции c доработкой 10, 100 и 1000 повторов:

0.00010079999999999811
0.0009751000000000065
0.009615700000000005

Исходный массив: [-25, -76, 88, 21, 97, 78, -4, 7, -36, 4]
Oтсортированный массив: [97, 88, 78, 21, 7, 4, -4, -25, -36, -76]
Исходный массив: [-25, -76, 88, 21, 97, 78, -4, 7, -36, 4]
Oтсортированный массив: [97, 88, 78, 21, 7, 4, -4, -25, -36, -76]


Функция с доработкой дает незначительный прирост. Однако существенной разницы 
не наблюдалось. Получил смешанные цифры, нет четко прослеживаемого преимущества от доработки.
"""