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


def merge_sort(data):
    count = len(data)
    if count > 2:
        part_1 = merge_sort(data[:count // 2])
        part_2 = merge_sort(data[count // 2:])
        data = part_1 + part_2
        last_index = len(data) - 1

        for i in range(last_index):
            min_value = data[i]
            min_index = i

            for j in range(i + 1, last_index + 1):
                if min_value > data[j]:
                    min_value = data[j]
                    min_index = j

            if min_index != i:
                data[i], data[min_index] = data[min_index], data[i]

    elif len(data) > 1 and data[0] > data[1]:
        data[0], data[1] = data[1], data[0]

    return data


def merge_sort2(lst_obj):
    if len(lst_obj) > 1:
        center = len(lst_obj) // 2
        left = lst_obj[:center]
        right = lst_obj[center:]

        left = merge_sort(left)
        right = merge_sort(right)

        # перестали делить
        # выполняем слияние
        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst_obj[k] = left[i]
                i += 1
            else:
                lst_obj[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            lst_obj[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst_obj[k] = right[j]
            j += 1
            k += 1
        return lst_obj


orig_list = [random.random()*50 for _ in range(100)]
print(timeit.timeit("merge_sort(orig_list[:])", globals=globals(), number=1000))
orig_list = [random.random()*50 for _ in range(1000)]
print(timeit.timeit("merge_sort(orig_list[:])", globals=globals(), number=1000))
orig_list = [random.random()*50 for _ in range(100)]

print(timeit.timeit("merge_sort2(orig_list[:])", globals=globals(), number=1000))
orig_list = [random.random()*50 for _ in range(1000)]
print(timeit.timeit("merge_sort2(orig_list[:])", globals=globals(), number=1000))

"""
merge_sort2 из примера работает быстрее реализации из википедии
Результат:
0.4927725529996678
38.358535020030104
0.2748460250440985
19.494689764920622
"""