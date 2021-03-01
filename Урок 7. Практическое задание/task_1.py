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
"""
Взят массив 100 элементов.
bubble_sort: 21.1907706 seconds  - сортировка по убыванию пузырьком
bubble_sort_opt: 18.5912567 seconds  - оптимизированная сортировка

рассмотрены дополнительно крайние случаи - уже отсортированный массив:
bubble_sort_opt: 12.135013899999997 seconds  - обычная сортировка для случая уже отсортированного массива.
bubble_sort_opt: 0.18044780000000316 seconds  - оптимизированная сортировка для случая уже отсортированного массива.

Без сомнений такая оптимизация очень полезна. 
Особенно если мы производим достаточно регулярную сортировку массива.
Например добавляем какие-то элементы в отсортированный массив. 
Получается, что наша задача отсортировать уже частично отсортированным массивом.
"""


from random import randint
from timeit import timeit


def bubble_sort(i_list):
    i = 1

    while i < len(i_list):
        for j in range(len(i_list) - i):
            if i_list[j] < i_list[j+1]:
                i_list[j], i_list[j+1] = i_list[j+1], i_list[j]
        i += 1
    return i_list


def bubble_sort_opt(i_list):
    i = 1
    sorted_flag = True

    while i < len(i_list):
        for j in range(len(i_list) - i):
            if i_list[j] < i_list[j+1]:
                i_list[j], i_list[j+1] = i_list[j+1], i_list[j]
                sorted_flag = False
        i += 1
        if sorted_flag:
            break
    return i_list


input_list = [randint(-100, 100) for i in range(100)]

sorted_list = bubble_sort(input_list[:])  # [:] - передаем копию нашего списка.

print(input_list)
bubble_sort_opt(input_list[:])  # попробуем усовершенстованную функцию для этого же массива.
bubble_sort_opt(sorted_list)  # попробуем вызвать функцию для уже отсортированного массива.

print(f"bubble_sort: {timeit('bubble_sort(input_list[:])', globals=globals(), number=10000)} seconds")
print(f"bubble_sort_opt: {timeit('bubble_sort_opt(input_list[:])', globals=globals(), number=10000)} seconds")
print(f"bubble_sort: {timeit('bubble_sort(sorted_list)', globals=globals(), number=10000)} seconds")
print(f"bubble_sort_opt: {timeit('bubble_sort_opt(sorted_list)', globals=globals(), number=10000)} seconds")
