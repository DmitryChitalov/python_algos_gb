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


def bubble_sort(lst_obj):
    """Сортировка пузырьком по убыванию"""
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


def better_bubble_sort(lst_obj):
    """Улучшенная сортировка пузырьком по убыванию"""
    is_shift = 1  # Добавим проверку обменов чтобы небыло лишних проходов
    n = 1
    while is_shift:
        is_shift = 0
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                is_shift = 1
        n += 1
    return lst_obj


if __name__ == "__main__":
    orig_list_10 = [randint(-100, 100) for _ in range(10)]
    orig_list_100 = [randint(-100, 100) for _ in range(100)]
    orig_list_1000 = [randint(-100, 100) for _ in range(1000)]

    print('Стандартная: ', orig_list_10, bubble_sort(orig_list_10[:]), sep='\n')
    print('Улучшенная: ', orig_list_10, better_bubble_sort(orig_list_10[:]), sep='\n')

    print('Стандартная: ')
    print("Массив 10 - " + str(timeit("bubble_sort(orig_list_10[:])",
                                      setup="from __main__ import bubble_sort, orig_list_10", number=10)),
          "Массив 100 - " + str(timeit("bubble_sort(orig_list_100[:])",
                                       setup="from __main__ import bubble_sort, orig_list_100", number=10)),
          "Массив 1000 - " + str(timeit("bubble_sort(orig_list_1000[:])",
                                        setup="from __main__ import bubble_sort, orig_list_1000", number=10)),
          sep='\n')

    print('Улучшенная: ')
    print("Массив 10 - " + str(timeit("better_bubble_sort(orig_list_10[:])",
                                      setup="from __main__ import better_bubble_sort, orig_list_10", number=10)),
          "Массив 100 - " + str(timeit("better_bubble_sort(orig_list_100[:])",
                                       setup="from __main__ import better_bubble_sort, orig_list_100", number=10)),
          "Массив 1000 - " + str(timeit("better_bubble_sort(orig_list_1000[:])",
                                        setup="from __main__ import better_bubble_sort, orig_list_1000", number=10)),
          sep='\n')

'''
Стандартная: 
[86, -89, -52, -7, -51, 86, -15, 67, 61, 0]
[86, 86, 67, 61, 0, -7, -15, -51, -52, -89]
Улучшенная: 
[86, -89, -52, -7, -51, 86, -15, 67, 61, 0]
[86, 86, 67, 61, 0, -7, -15, -51, -52, -89]
Стандартная: 
Массив 10 - 0.00010820000000000274
Массив 100 - 0.0070734999999999965
Массив 1000 - 1.1115672
Улучшенная: 
Массив 10 - 0.00019539999999995672
Массив 100 - 0.014607799999999838
Массив 1000 - 0.9477001

После оптимизации время немного изменилось, однако если массив уже подается почти отсортированным,то скорость вырастает.
'''
