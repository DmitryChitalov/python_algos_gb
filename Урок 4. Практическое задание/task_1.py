"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""

from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [nums[i] for i in range(len(nums)) if nums[i] % 2 == 0]


def func_3(nums):
    return list(filter(lambda x: x % 2 == 0, nums))


n = [i for i in range(1000)]
print(func_1(n))
print(func_2(n))
print(func_3(n))

print(timeit("func_1(n)", setup="from __main__ import func_1, n", number=1000))
"""0.15530850000000002"""
print(timeit("func_2(n)", setup="from __main__ import func_2, n", number=1000))
"""0.12881469999999998"""
print(timeit("func_3(n)", setup="from __main__ import func_3, n", number=1000))
"""0.11406260000000001"""

n = [i for i in range(100000)]

print(timeit("func_1(n)", setup="from __main__ import func_1, n", number=1000))
"""15.780626400000001"""
print(timeit("func_2(n)", setup="from __main__ import func_2, n", number=1000))
"""16.956090200000002"""
print(timeit("func_3(n)", setup="from __main__ import func_3, n", number=1000))
"""15.508269400000003"""

n = [i for i in range(1000000)]

print(timeit("func_1(n)", setup="from __main__ import func_1, n", number=1000))
"""187.571168"""
print(timeit("func_2(n)", setup="from __main__ import func_2, n", number=1000))
"""211.60162729999996"""
print(timeit("func_3(n)", setup="from __main__ import func_3, n", number=1000))
"""192.05540040000005"""

"""
Я сделал две оптимизации функции, первую через генератор, вторую через встроенную функцию filter.
Первый замер сделал для списка из 1 тыс. элементов.
Как и ожидалось, замеры показали, что реализация через генератор оказалась лучше приведенного кода,
а через встроенную функцию filter ещё лучше, чем через генератор.
Второй замер сделал для списка из 100 тыс. элементов.
И в этом случае меня результаты удивили.
Оказалось, что реализация через генератор уже показывает результат хуже приведенного кода,
а через встроенную функцию filter чуть-чуть лучше.
Тогда я решил провести третий замер для списка из 1 млн. элементов.
И подозрения подтвердились, мои оптимизации показали замеры хуже, чем приведенный код.

Дмитрий, расскажите пожалуйста на разборе ДЗ, почему так происходит?
"""
