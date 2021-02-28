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

import random
import timeit


def merge_sort_recursive(lst: list):
    if len(lst) < 2:
        return
    middle_index = len(lst) // 2
    left_half, right_half = lst[:middle_index], lst[middle_index:]
    merge_sort_recursive(left_half)
    merge_sort_recursive(right_half)
    left_half_index, right_half_index, list_index = 0, 0, 0
    while left_half_index < len(left_half) and right_half_index < len(right_half):  # объединяем по возрастанию
        if left_half[left_half_index] < right_half[right_half_index]:
            lst[list_index] = left_half[left_half_index]
            left_half_index += 1
        else:
            lst[list_index] = right_half[right_half_index]
            right_half_index += 1
        list_index += 1
    while left_half_index < len(left_half):  # добавляем справа уже отсортированный остаток левой половины
        lst[list_index] = left_half[left_half_index]
        left_half_index += 1
        list_index += 1
    while right_half_index < len(right_half):  # добавляем справа уже отсортированный остаток правой половины
        lst[list_index] = right_half[right_half_index]
        right_half_index += 1
        list_index += 1


count = int(input("Введите число элементов > "))
list1 = [random.random() * 50 for _ in range(count)]
print(f"Исходный: {list1}")
merge_sort_recursive(list1)
print(f"Отсортированный: {list1}")


def test_time():
    print('list1.copy():',
          timeit.repeat("list1.copy()", globals=globals(), number=20, repeat=5))
    print('merge_sort_recursive:',
          timeit.repeat("merge_sort_recursive(list1.copy())", globals=globals(), number=20, repeat=5))


list1 = [random.random() * 50 for _ in range(10)]
test_time()
# list1.copy(): [5.699999999997374e-06, 3.100000000255676e-06, 2.9999999999752447e-06, 3.200000000092018e-06,
# 2.9999999999752447e-06]
# merge_sort_recursive: [0.0004635999999997864, 0.00045300000000025875, 0.0004483999999997934, 0.0004485999999999102,
# 0.00043779999999982167]
list1 = [random.random() * 50 for _ in range(100)]
test_time()
# list1.copy(): [1.760000000006201e-05, 1.590000000017966e-05, 1.6000000000016e-05, 1.590000000017966e-05,
# 1.6099999999852344e-05]
# merge_sort_recursive: [0.007241399999999842, 0.00977719999999982, 0.009818500000000174, 0.011610200000000237,
# 0.006822699999999848]
list1 = [random.random() * 50 for _ in range(1000)]
test_time()
# list1.copy(): [8.730000000012339e-05, 8.529999999984383e-05, 8.479999999977395e-05, 8.529999999984383e-05,
# 8.490000000005438e-05]
# merge_sort_recursive: [0.10052199999999978, 0.13171420000000023, 0.1213204000000001, 0.10913299999999992,
# 0.09352850000000013]

# Выводы: в сравнении с сортировкой пузырьком сортировка слиянием очень эффективна.
