"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в
виде функции.

Обязательно доработайте алгоритм (сделайте его умнее)!

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.

Сделайте выводы!!!
Опишите в чем была ваша доработка и помогла ли вам доработка??
"""


from timeit import timeit
from random import randint


def bubble_sort(my_list, order=1):
    """
    Сортировка позурьком, order=1 по возрастанию, order=2 по убыванию
    """

    n = 1
    while n < len(my_list):
        for i in range(len(my_list) - n):
            if order == 1:
                if my_list[i] > my_list[i + 1]:
                    my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
            else:
                if my_list[i] < my_list[i + 1]:
                    my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
        n += 1

    return my_list


def bubble_sort_improved(my_list, order=1):
    """
    Сортировка позурьком, order=1 по возрастанию, order=2 по убыванию
    """

    n = 1
    max_el = len(my_list) # вынесем выисление длины списка за цикл
    while n < max_el:
        was_switching = 0
        for i in range(max_el - n):
            if order == 1:
                if my_list[i] > my_list[i + 1]:
                    my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
                    was_switching = 1
            else:
                if my_list[i] < my_list[i + 1]:
                    my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
                    was_switching = 1
        n += 1
        if was_switching == 0: # если перестановок не было, то считаем, что список уже отсортирован
            break

    return my_list


sort_list_10 = [randint(-100, 100) for i in range(10)]
sort_list_100 = [randint(-100, 100) for i in range(100)]
sort_list_1000 = [randint(-100, 100) for i in range(1000)]

print(sort_list_10)
print(bubble_sort(sort_list_10[:], 2))

print(
    "Замер времени работы на 10 элементах: ",
    timeit(
        "bubble_sort(sort_list_10[:], 2)",
        globals=globals(),
        number=1000))

print(
    "Замер времени работы на 100 элементах: ",
    timeit(
        "bubble_sort(sort_list_100[:], 2)",
        globals=globals(),
        number=1000))

print(
    "Замер времени работы на 1000 элементах: ",
    timeit(
        "bubble_sort(sort_list_1000[:], 2)",
        globals=globals(),
        number=1000))

print("Улучшенный алгоритм пузырька:")

print(sort_list_10)
print(bubble_sort_improved(sort_list_10[:], 2))

print(
    "Замер времени работы на 10 элементах: ",
    timeit(
        "bubble_sort_improved(sort_list_10[:], 2)",
        globals=globals(),
        number=1000))

sort_list = [randint(-100, 100) for i in range(100)]

print(
    "Замер времени работы на 100 элементах: ",
    timeit(
        "bubble_sort_improved(sort_list_100[:], 2)",
        globals=globals(),
        number=1000))

print(
    "Замер времени работы на 1000 элементах: ",
    timeit(
        "bubble_sort_improved(sort_list_1000[:], 2)",
        globals=globals(),
        number=1000))

print(
    """
В улучшенном алгоритме сортировка прерывается, если за последний проход не было ни одной перестановки.
Еще убрал вычисление длинны списка из цикла.
В целом изменения дают эффект, но он зависит от данных
    """
)
