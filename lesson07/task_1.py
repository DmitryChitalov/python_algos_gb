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


def buble_sort(list_arg):
    for idx1 in range(len(list_arg) - 1):
        for idx2 in range(len(list_arg) - idx1 - 1):
            if list_arg[idx2] < list_arg[idx2 + 1]:
                list_arg[idx2], list_arg[idx2 + 1] = list_arg[idx2 + 1], \
                                                     list_arg[idx2]
    return list_arg


def buble_sort_optimazed(list_arg):
    for idx1 in range(len(list_arg) - 1):
        was_reversed = False
        for idx2 in range(len(list_arg) - idx1 - 1):
            if list_arg[idx2] < list_arg[idx2 + 1]:
                list_arg[idx2], list_arg[idx2 + 1] = list_arg[idx2 + 1], \
                                                     list_arg[idx2]
                was_reversed = True
        if was_reversed == False: break
    return list_arg


for num in (10, 100, 1000):
    my_list = [randint(0, 100) for el in range(num)]
    print(f"buble_sort({num}): ",
          timeit(f"buble_sort(my_list[:])", globals=globals(), number=1000))
    print(f"buble_sort_optimazed({num}): ",
          timeit(f"buble_sort_optimazed(my_list[:])", globals=globals(),
                 number=1000))

# buble_sort(10):  0.039751400000000006
# buble_sort_optimazed(10):  0.022019200000000017
# buble_sort(100):  2.6547207000000004
# buble_sort_optimazed(100):  1.9884780000000002
# buble_sort(1000):  211.6230023
# buble_sort_optimazed(1000):  216.61465460000002

# Оптимизация в том, что я прекращаю проходы как только в очередном проходе не
# было ни одной перестановки. Не помогло:)
