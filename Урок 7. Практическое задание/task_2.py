"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""

import random
import timeit


def fusion_sort(test_list):

    if len(test_list) > 1:
        middle = len(test_list) // 2
        left_half = test_list[:middle]
        right_half = test_list[middle:]

        fusion_sort(left_half)
        fusion_sort(right_half)

        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                test_list[k] = left_half[i]
                i = i + 1
            else:
                test_list[k] = right_half[j]
                j = j + 1
            k = k + 1

        while i < len(left_half):
            test_list[k] = left_half[i]
            i = i + 1
            k = k + 1

        while j < len(right_half):
            test_list[k] = right_half[j]
            j = j + 1
            k = k + 1


number_el = int(input('Please enter a number of elements: '))
test_list = [random.random() * 50 for i in range(number_el)]
print('Program "Use fusion sort"')
print(f'Original test list: {test_list}')
fusion_sort(test_list)
print(f'Sorted list: {test_list}')

print(timeit.timeit("fusion_sort(test_list[:])",
                    setup='from __main__ import fusion_sort, test_list', number = 100))
print(timeit.timeit("fusion_sort(test_list[:])",
                    setup='from __main__ import fusion_sort, test_list', number = 1000))
print(timeit.timeit("fusion_sort(test_list[:])",
                    setup='from __main__ import fusion_sort, test_list', number = 10000))
print(timeit.timeit("fusion_sort(test_list[:])",
                    setup='from __main__ import fusion_sort, test_list', number = 100000))
'''
Замеры времени для 5 элементов:
0.0007566999999999435  - для 100 иттераций
0.007051100000000199   - для 1000 иттераций
0.12384720000000016    - для 10000 иттераций
0.8962246              - для 100000 иттераций

Замеры времени для 10 элементов:
0.0022773000000002597
0.016826599999999914
0.2127870999999999
2.2816394000000004

Замеры времени для 100 элементов:
0.026350499999999943
0.33498610000000006
3.6402384999999997
39.0234767

Вывод:
    Как мы видим уже изменяя число элементов с 5 до 10 элементов, для 100 прогонов(иттераций) функции,
использующей алгоритм сортировки "Метод слияния" время возрастает с 4-х знаков после запятой (0.0007), до 3-х (0.002),
но в тоже время с 10 элементов до 100 растет не так "быстро" до 2-х знаков после запятой (0.02).
'''
