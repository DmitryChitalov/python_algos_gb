"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
from random import randint


def merge(l_part, r_part):
    sorted_list = []
    l_part_idx = r_part_idx = 0
    # Длина списков часто используется, поэтому создадим переменные для удобства
    l_part_len, r_part_len = len(l_part), len(r_part)
    for _ in range(l_part_len + r_part_len):
        if l_part_idx < l_part_len and r_part_idx < r_part_len:
            # Сравниваем первые элементы в начале каждого списка
            # Если первый элемент левого подсписка меньше, добавляем его
            # в отсортированный массив
            if l_part[l_part_idx] <= r_part[r_part_idx]:
                sorted_list.append(l_part[l_part_idx])
                l_part_idx += 1
            # Если первый элемент правого подсписка меньше, добавляем его
            # в отсортированный массив
            else:
                sorted_list.append(r_part[r_part_idx])
                r_part_idx += 1
        # Если достигнут конец левого списка, элементы правого списка
        # добавляем в конец результирующего списка
        elif l_part_idx == l_part_len:
            sorted_list.append(r_part[r_part_idx])
            r_part_idx += 1
        # Если достигнут конец правого списка, элементы левого списка
        # добавляем в отсортированный массив
        elif r_part_idx == r_part_len:
            sorted_list.append(l_part[l_part_idx])
            l_part_idx += 1
    return sorted_list


def merge_sort(nums):
    # Возвращаем список, если он состоит из одного элемента
    if len(nums) <= 1:
        return nums
    # Для того чтобы найти середину списка, используем деление без остатка
    # Индексы должны быть integer
    mid = len(nums) // 2
    # Сортируем и объединяем подсписки
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])
    # Объединяем отсортированные списки в результирующий
    return merge(left_list, right_list)

# Проверяем, что оно работает
test_data = [randint(0, 50) for _ in range(100)]
print(test_data)
sorted_list = merge_sort(test_data)
print(sorted_list)
