"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
from random import uniform
from timeit import timeit


# проверка ввода на целое число:
def is_a_digit(data):
    while not data.isdigit():
        print('Ошибка ввода. Пожалуйста, введите одно целое натуральное число.')
        data = input('Введите число: ')
    return int(data)


# задание случайного массива чисел с вводом количества элементов:
list_1 = [uniform(0, 49) for i in range(is_a_digit(input('Введите число элементов: ')))]


def devide_n_sort(array):
    def devide_array(array):
        array_len = len(array)
        if array_len > 1:
            half = len(array) // 2
            left = array[:half]
            right = array[half:]
            return merge_sort(devide_array(left), devide_array(right))
        else:
            return array

    def merge_sort(left, right):
        sorted_list = []
        left_ix = 0
        right_ix = 0
        for _ in range(len(left) + len(right)):
            if left_ix < len(left) and right_ix < len(right):
                if left[left_ix] > right[right_ix]:
                    sorted_list.append(right[right_ix])
                    right_ix += 1
                elif right[right_ix] > left[left_ix]:
                    sorted_list.append(left[left_ix])
                    left_ix += 1

            else:
                if left_ix == len(left) and right_ix != len(right):
                    sorted_list.append(right[right_ix])
                    right_ix += 1
                if right_ix == len(right) and left_ix != len(left):
                    sorted_list.append(left[left_ix])
                    left_ix += 1

        return sorted_list
    return devide_array(array)


print(f'Исходный массив: \n{list_1}')
print(f'Отсортированный массив: \n{devide_n_sort(list_1)}\n')
print('Замер времени сортировки методо слияния с массивом list_1:')
print(timeit('devide_n_sort(list_1[:])', setup='from __main__ import devide_n_sort, list_1', number=10000))
