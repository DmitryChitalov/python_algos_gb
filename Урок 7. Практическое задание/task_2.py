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


def merge_sort(orig_list):
    while len(orig_list) > 1:
        center = len(orig_list) // 2
        left = orig_list[:center]
        right = orig_list[center:]

        merge_sort(left)
        merge_sort(right)

        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                orig_list[k] = left[i]
                i += 1
            else:
                orig_list[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            orig_list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            orig_list[k] = right[j]
            j += 1
            k += 1

        return orig_list


def merge_sort_custom(orig_list):
    if len(orig_list) > 2:
        left = merge_sort_custom(orig_list[:len(orig_list) // 2])
        right = merge_sort_custom(orig_list[len(orig_list) // 2:])
        orig_list = left + right
        last_index = len(orig_list) - 1

        for i in range(last_index):
            min_value = orig_list[i]
            min_index = i

            for j in range(i + 1, last_index + 1):
                if min_value > orig_list[j]:
                    min_value = orig_list[j]
                    min_index = j

            if min_index != i:
                orig_list[i], orig_list[min_index] = orig_list[min_index], orig_list[i]

    elif len(orig_list) > 1 and orig_list[0] > orig_list[1]:
        orig_list[0], orig_list[1] = orig_list[1], orig_list[0]

    return orig_list


count = int(input('Введите число элементов: '))
orig_list1 = [random.randint(0, 50) for _ in range(count)]
print(f'Исходный: {orig_list1}\nОтсортированный: {merge_sort(orig_list1)}')

orig_list2 = [random.randint(0, 50) for _ in range(count)]
print(f'Исходный: {orig_list2}\nОтсортированный: {merge_sort_custom(orig_list2)}')

# замеры 10
orig_list = [random.randint(0, 50) for _ in range(10)]
print("Начальный вариант: 10 эл => ", timeit.timeit("merge_sort(orig_list[:])", \
                                                    setup="from __main__ import merge_sort, orig_list",
                                                    number=100))
orig_list = [random.randint(0, 50) for _ in range(10)]
print("Другой вариант: 10 эл => ", timeit.timeit("merge_sort_custom(orig_list[:])", \
                                                 setup="from __main__ import merge_sort_custom, orig_list",
                                                 number=100))

# замеры 100
orig_list = [random.randint(0, 50) for _ in range(100)]
print("Начальный вариант: 100 эл => ", timeit.timeit("merge_sort(orig_list[:])", \
                                                     setup="from __main__ import merge_sort, orig_list",
                                                     number=100))
orig_list = [random.randint(0, 50) for _ in range(100)]
print("Другой вариант: 100 эл => ", timeit.timeit("merge_sort_custom(orig_list[:])", \
                                                  setup="from __main__ import merge_sort_custom, orig_list",
                                                  number=100))

# замеры 1000
orig_list = [random.randint(0, 50) for _ in range(1000)]
print("Начальный вариант: 1000 эл => ", timeit.timeit("merge_sort(orig_list[:])", \
                                                      setup="from __main__ import merge_sort, orig_list",
                                                      number=100))
orig_list = [random.randint(0, 50) for _ in range(1000)]
print("Другой вариант: 1000 эл => ", timeit.timeit("merge_sort_custom(orig_list[:])", \
                                                   setup="from __main__ import merge_sort_custom, orig_list",
                                                   number=100))

"""
Начальный вариант: 10 эл =>  0.002884480000000078
Другой вариант: 10 эл =>  0.0026695039999999892
Начальный вариант: 100 эл =>  0.028895026999999907
Другой вариант: 100 эл =>  0.08393742500000023
Начальный вариант: 1000 эл =>  0.3938792659999999
Другой вариант: 1000 эл =>  6.57194119

второй вариант медленнее из-за вложенности циклов. сложность получается квадратическая
"""
