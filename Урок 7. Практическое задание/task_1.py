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

Ответ: используем цикл for вместо while и отказываемся от счетчика,
такая оптимизация даст небольшой прирост скорости.
Так же во второй функции реализована проверка на отсортированность массива,
где в подавляющем большинстве случаев не придется проходить массив
полностью, если массив неотсортирован и достаточно будет всего нескольких
шагов для проверки.
"""
from random import randint
from timeit import timeit


def bubble_sort1(arr):
    n = 1
    while n < len(arr):
        for i in range(len(arr)-n):
            if arr[i] < arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        n += 1
    return arr


def bubble_sort2(arr):
    n = len(arr)

    # Проверка отсортирован ли массив
    for i in range(0, n-1):
        if arr[i] < arr[i+1]:
            break
    else:
        return arr

    for i in range(1, n):
        for k in range(n-i):
            if arr[k] < arr[k+1]:
                arr[k], arr[k+1] = arr[k+1], arr[k]
    return arr


if __name__ == '__main__':
    unsorted = [randint(-100, 100) for _ in range(2000)]

    print(timeit(f'bubble_sort1(j)', setup='j = unsorted.copy()', number=1, globals=globals()))
    print(timeit(f'bubble_sort2(j)', setup='j = unsorted.copy()', number=1, globals=globals()))
    unsorted1 = unsorted.copy()
    unsorted2 = unsorted.copy()
    print(bubble_sort1(unsorted1))
    print(bubble_sort2(unsorted2))

