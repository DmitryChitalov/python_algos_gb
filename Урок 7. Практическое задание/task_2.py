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
import operator
from task_1 import dec


lst = [uniform(0, 50) for i in range(10000)]


@dec
def merge_sort_decor(lst, compare=operator.lt):
    def merge_sort(lst, compare):
        """
        Основной алгоритм сортировки
        """
        def merge(left, right, compare):
            """
            Здесь происходит слияние двух списков длины больше еденицы
            """
            res = []
            i, j = 0, 0
            while i < len(left) and j < len(right):
                if compare(left[i], right[j]):
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1
            while i < len(left):
                res.append(left[i])
                i += 1
            while j < len(right):
                res.append(right[j])
                j += 1
            return res

        if len(lst) < 2:
            return lst[:]
        else:
            middle = int(len(lst) / 2)
            left = merge_sort(lst[:middle], compare)
            right = merge_sort(lst[middle:], compare)
            return merge(left, right, compare)

    return merge_sort(lst, compare)


print(merge_sort_decor(lst.copy()))


"""
10 элементов: Время:  4.039100000000073e-05
100 элементов: Время:  0.0009386639999999988
1000 элементов: Время:  0.008850180999999999
10000 элементов: Время:  0.09008844500000002

Видно, что алгоритм выполняется за линейно-логарифмическое время (N*log(N))
"""