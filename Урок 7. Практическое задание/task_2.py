"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
from timeit import timeit
from random import uniform


def merge(left, right):
    res = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res += left[i:] + right[j:]
    return res


def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        left = lst[:len(lst) // 2]
        right = lst[len(lst) // 2:]

    return merge(merge_sort(left), merge_sort(right))


if __name__ == "__main__":
    orig_list_10 = [uniform(0, 50) for _ in range(10)]
    orig_list_100 = [uniform(0, 50) for _ in range(100)]
    orig_list_1000 = [uniform(0, 50) for _ in range(1000)]

    print('Исходный - ', orig_list_10)
    print('Отсортированный - ', merge_sort(orig_list_10[:]))

    print("Массив 10 - " + str(timeit("merge_sort(orig_list_10[:])",
                                      setup="from __main__ import merge_sort, orig_list_10", number=10)),
          "Массив 100 - " + str(timeit("merge_sort(orig_list_100[:])",
                                       setup="from __main__ import merge_sort, orig_list_100", number=10)),
          "Массив 1000 - " + str(timeit("merge_sort(orig_list_1000[:])",
                                        setup="from __main__ import merge_sort, orig_list_1000", number=10)),
          sep='\n')

"""
Исходный -  [37.71989387271995, 10.315665904880472, 42.83041280605055, 22.7053462595187, 32.19811161732281, 44.68798042757059, 11.122231832670437, 8.297067574969635, 24.906375355057087, 17.524900203916506]
Отсортированный -  [8.297067574969635, 10.315665904880472, 11.122231832670437, 17.524900203916506, 22.7053462595187, 24.906375355057087, 32.19811161732281, 37.71989387271995, 42.83041280605055, 44.68798042757059]
Массив 10 - 0.00037239999999999496
Массив 100 - 0.003643199999999999
Массив 1000 - 0.0447602
"""
