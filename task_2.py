"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Хотя в примерах к уроку уже есть вариант реализации слияния, попробуйте предложить другой
(придумать или найти)

И попытаться сделать замеры на массивах разной длины: 10, 100, 1000, ...

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
import timeit
import random
def merge_sort(lst):

    # дробление массива и вызов функции соединения
    def merge_div(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left_list = merge_div(arr[:mid])
        right_list = merge_div(arr[mid:])
        return merge(left_list, right_list)


    def merge(right_list, left_list):
        sorted_list = []
        left_list_index = right_list_index = 0

        left_list_length, right_list_length = len(left_list), len(right_list)

        for i in range(left_list_length + right_list_length):
            if left_list_index < left_list_length and right_list_index < right_list_length:
                # Сравниваем первые элементы в начале каждого списка и
                # добавляем меньший
                if left_list[left_list_index] <= right_list[right_list_index]:
                    sorted_list.append(left_list[left_list_index])
                    left_list_index += 1
                else:
                    sorted_list.append(right_list[right_list_index])
                    right_list_index += 1
            # Если достигнут конец списка, элементы второго списка
            # добавляем в конец результирующего списка
            elif left_list_index == left_list_length:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1
            elif right_list_index == right_list_length:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
        return sorted_list

    return merge_div(lst)

arr = [random.uniform(0, 50) for x in range(10)]
print(arr)
print(merge_sort(arr))
print(f'100: {timeit.timeit("merge_sort(arr)", globals=globals(), number=100)}')
print(f'1000: {timeit.timeit("merge_sort(arr)", globals=globals(), number=1000)}')
print(f'10000: {timeit.timeit("merge_sort(arr)", globals=globals(), number=10000)}')
