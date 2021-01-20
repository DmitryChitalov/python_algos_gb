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


def bubble_sort_reverse(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_reverse2(lst_obj):
    n = 1
    count = 0
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
                count += 1
        if count == 0:
            break
        n += 1
    return lst_obj


if __name__ == "__main__":
    test_list1 = [randint(-100, 100) for _ in range(100)]
    print(test_list1)
    print("Профилировка времени работы функции bubble_sort_reverse")
    print(timeit(
        "bubble_sort_reverse(test_list1[:])",
        setup="from __main__ import bubble_sort_reverse, test_list1", number=1000)
    )
    print("Профилировка времени работы функции bubble_sort_reverse2")
    print(timeit(
        "bubble_sort_reverse2(test_list1[:])",
        setup="from __main__ import bubble_sort_reverse2, test_list1", number=1000)
    )

"""
Вывод: профилировка времени функций bubble_sort_reverse и bubble_sort_reverse2 показала, что оптимизация алгоритма 
сортировки пузырьком не дала результатов по сокращению временных затрат на сортировку масива. Скорее наоборот, 
время сортировки увеличилось, незначительно, но возросло.
"""

