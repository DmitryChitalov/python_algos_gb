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

"""
Информативоно позанимался с данным заднием, раньше не знал что внутри гениратора можно волшебством пользоваться=)
Хотя сокрей всего это волшебстово модуля random, но всё равно интерстно.
__round__(3) меня прям поразил)
"""
user_num_input = int(input('Введите число элементов: '))
l = [random.uniform(0, 50).__round__(3) for _ in range(user_num_input)]


def merge_sort(lst):
    if len(lst) > 1:
        center = len(lst) // 2
        left = lst[:center]
        right = lst[center:]

        merge_sort(left)

        merge_sort(right)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1

        return lst


print(f'Исходный список - {l}')
print(f'Отсортированый список - {merge_sort(l)}')
