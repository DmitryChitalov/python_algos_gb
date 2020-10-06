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


def sort_alg(_list):
    if len(_list) > 1:
        center = len(_list) // 2
        left = _list[:center]
        right = _list[center:]
        sort_alg(left)
        sort_alg(right)
        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                _list[k] = left[i]
                i += 1
            else:
                _list[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            _list[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            _list[k] = right[j]
            j += 1
            k += 1
        return _list


count = int(input('Введите число элементов: '))
orig_list = [uniform(0, 50) for el in range(count)]

print(f'Оригинальный список: {orig_list}')
sort_alg(orig_list)
print(f'Отсортированный список: {orig_list}')
