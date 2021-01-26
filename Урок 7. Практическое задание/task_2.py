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
import timeit

number = input("Введите число: ")

orig_list = [uniform(0, 50) for _ in range(int(number))]
print(f"Оригинальный массив: {orig_list}")


def merge_sort(list_to_sort):
    if len(list_to_sort) == 1:
        return list_to_sort

    middle = len(list_to_sort) // 2
    left = merge_sort(list_to_sort[:middle])
    right = merge_sort(list_to_sort[middle:])

    return merge_two_list(left, right)


def merge_two_list(first, second):
    sorted_list =[]
    i = j = 0

    while i < len(first) and j < len(second):
        if first[i] < second[j]:
            sorted_list.append(first[i])
            i += 1
        else:
            sorted_list.append(second[j])
            j += 1

    if i < len(first):
        sorted_list += first[i:]
    if j < len(second):
        sorted_list += second[j:]

    return sorted_list


def orig_merge_sort(lst_obj):
    if len(lst_obj) > 1:
        center = len(lst_obj) // 2
        left = lst_obj[:center]
        right = lst_obj[center:]

        merge_sort(left)
        merge_sort(right)

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


print("Время выполнения сортировки на массиве длиной 10 элементов",
      timeit.timeit("merge_sort(orig_list[:])", setup = "from __main__ import merge_sort, orig_list", number=1000))
print(merge_sort(orig_list), '\n')


print(f"Оригинальный массив: {orig_list}")
print("Время выполнения оригинальной сортировки на массиве длиной 10 элементов",
      timeit.timeit("orig_merge_sort(orig_list[:])",
                    setup = "from __main__ import orig_merge_sort, orig_list", number=1000))
print(merge_sort(orig_list), '\n')

number = input("Введите число: ")
orig_list = [uniform(0, 50) for _ in range(int(number))]
print(f"Оригинальный массив: {orig_list}")

print("Время выполнения сортировки на массиве длиной 100 элементов",
      timeit.timeit("merge_sort(orig_list[:])", setup = "from __main__ import merge_sort, orig_list", number=1000))
print(merge_sort(orig_list), '\n')


print(f"Оригинальный массив: {orig_list}")
print("Время выполнения оригинальной сортировки на массиве длиной 100 элементов",
      timeit.timeit("orig_merge_sort(orig_list[:])",
                    setup = "from __main__ import orig_merge_sort, orig_list", number=1000))

print(merge_sort(orig_list), '\n')

number = input("Введите число: ")
print(f"Оригинальный массив: {orig_list}")
print("Время выполнения сортировки на массиве длиной 1000 элементов",
      timeit.timeit("merge_sort(orig_list[:])", setup = "from __main__ import merge_sort, orig_list", number=1000))
print(merge_sort(orig_list))

print(f"Оригинальный массив: {orig_list}")
print("Время выполнения оригинальной сортировки на массиве длиной 1000 элементов",
      timeit.timeit("orig_merge_sort(orig_list[:])",
                    setup = "from __main__ import orig_merge_sort, orig_list", number=1000))

print(merge_sort(orig_list))


"""
Написанный мной алгоритм оказался чуточку медленнее, но хоть не с О(n**2)
"""