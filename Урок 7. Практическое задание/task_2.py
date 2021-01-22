"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
import timeit
import random


def merge_sort(test_list):
    if len(test_list) > 1:
        center = len(test_list) // 2
        left = test_list[:center]
        right = test_list[center:]

        merge_sort(left)
        merge_sort(right)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                test_list[k] = left[i]
                i += 1
            else:
                test_list[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            test_list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            test_list[k] = right[j]
            j += 1
            k += 1
        return test_list


def bubble_sort(lst_obj):
    """Функция сортировки 'пузырьком' """
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] > lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


test_list = [random.random()*50 for _ in range(300)]
test_list1 = test_list.copy()

print("Исходный массив ", test_list)
# merge_sort(test_list)
print("Функция сортировки слиянием ", (timeit.timeit("merge_sort(test_list)", \
    setup="from __main__ import merge_sort, test_list", number=1)))
print("Отсортированный массив ", test_list)
print("Функция сортировки 'пузырком' ", (timeit.timeit("bubble_sort(test_list1)", \
    setup="from __main__ import bubble_sort, test_list1", number=1)))

"""По замерам Сортировка 'слиянием' заметно быстрее сортировки 'пузырьком' """
