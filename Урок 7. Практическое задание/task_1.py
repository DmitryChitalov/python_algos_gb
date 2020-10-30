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

def bubble_sort(array):
    """
    Классический метод сортировки пузырьком.
    """
    for i in range(len(array)):
        for j in range(len(array)):
            if array[j] < array[i]:
                array[i], array[j] = array[j], array[i]

def bubble_sort_impr(array):
    """
    Улучшенный алгоритм сортировки пузырьком.
    """
    changed = True
    while changed:
        changed = False
        for i in range(len(array) - 1):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                changed = True

if __name__ == '__main__':
    random_array = [randint(-100, 100) for i in range(1000)]
    print('Исходный массив:')
    print(random_array)
    copy_array = random_array[:]
    bubble_sort_impr(copy_array)
    print('Отсортированный массив:')
    print(copy_array)
    print('Время сортировки обычным "пузырьком": ',
          timeit('bubble_sort(random_array[:])',
                 setup='from __main__ import bubble_sort, random_array',
                 number=1000)) # 82.33458075800081
    print('Время сортировки улучшенным "пузырьком": ',
          timeit('bubble_sort_impr(random_array[:])',
                 setup='from __main__ import bubble_sort_impr, random_array',
                 number=1000)) # 142.38318027099922
"""
Если массив полностью неупорядочен, то классический алгоритм показывает
лучшие результаты. Однако, когда хотя бы половина массива упорядочена,
улучшенный алгоритм начинает показывать результаты, превосходящие
классический алгоритм.
"""