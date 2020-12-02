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

n = input('Введите число элементов массива: ')

list1 = [random.uniform(0, 49) for _ in range(int(n))]

print(list1)


def merge_sort(list):
    if len(list) > 1:
        center = len(list) // 2
        left = list[:center]
        right = list[center:]

        merge_sort(left)
        merge_sort(right)

        # почему код ниже выполнится когда if сверху станет False?
        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k] = left[i]
                i += 1
            else:
                list[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1
        return list


print(f'Исходный массив - {list1}')
print(f'отсортированный массив - {merge_sort(list1[:])}')

