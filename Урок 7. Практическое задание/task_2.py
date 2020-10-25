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

def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0
    for i in range(len(left_list) + len(right_list)):
        if left_list_index < len(left_list) and right_list_index < len(right_list):
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1
        elif left_list_index == len(left_list):
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        elif right_list_index == len(right_list):
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1
    return sorted_list

def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left_list = merge_sort(array[:mid])
    right_list = merge_sort(array[mid:])
    return merge(left_list, right_list)

if __name__ == '__main__':
    random_array = [uniform(0, 50) for i in range(1000)]
    sorted_array = merge_sort(random_array)
    print('Исходный массив:')
    print(random_array)
    print('Отсортированный массив:')
    print(sorted_array)