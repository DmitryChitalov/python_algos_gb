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


def bubble_sort1(my_list):
    n = 1
    while n < len(my_list):
        for i in range(len(my_list) - n):
            if my_list[i] < my_list[i + 1]:
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
        n += 1
    return my_list


def bubble_sort2(my_list):
    n = 1
    k = 0
    while n < len(my_list):
        for i in range(len(my_list) - n):
            if my_list[i] < my_list[i + 1]:
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
                k = 1
        if k == 0:
            break
        n += 1
    return my_list


if __name__ == '__main__':
    initial = [randint(-100, 100) for _ in range(2000)]

    print(timeit(f'bubble_sort1(j)', setup='j = initial.copy()', number=1, globals=globals()))
    print(timeit(f'bubble_sort2(j)', setup='j = initial.copy()', number=1, globals=globals()))
    unsorted1 = initial.copy()
    unsorted2 = initial.copy()
    print(initial)
    print(bubble_sort2(initial))


"""
результаты вычислений:
0.9185352
0.9865797999999999
преемуществ по скорости нет, есть даже незначительное уменьшение скорости.
"""