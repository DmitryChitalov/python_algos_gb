"""
Задание 1.
Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Можно взять задачи с курса Основ или с текущего курса Алгоритмов

Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""
from memory_profiler import profile
from sys import getsizeof
from pympler import asizeof


@profile
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


@profile
def func_2(nums):
    return [i for id, i in enumerate(nums) if i % 2 == 0]


@profile
def func_3(nums):
    return list(filter(lambda x: x % 2 == 0, nums))


n = [i for i in range(1000000)]
print(asizeof.asizeof(n))  # 20348728 байт
func_1(n)
func_2(n)
func_3(n)

"""
Версия Python 3.8
64-разрядная ОС

Результаты:
func_1 - 9.5 MiB
func_2 - 1.9 MiB
func_3 - 1.9 MiB

По результатам замеров памяти, лучший показатель у функций func_2 и func_3.
В принципе, примерно этот же результат мы получали при использовании timeit.


Line #    Mem usage    Increment   Line Contents
================================================
    19     32.6 MiB     32.6 MiB   @profile
    20                             def func_1(nums):
    21     32.6 MiB      0.0 MiB       new_arr = []
    22     42.1 MiB      0.0 MiB       for i in range(len(nums)):
    23     42.1 MiB      0.1 MiB           if nums[i] % 2 == 0:
    24     42.1 MiB      0.2 MiB               new_arr.append(i)
    25     42.1 MiB      0.0 MiB       return new_arr


Line #    Mem usage    Increment   Line Contents
================================================
    28     32.8 MiB     32.8 MiB   @profile
    29                             def func_2(nums):
    30     34.7 MiB      0.2 MiB       return [i for id, i in enumerate(nums) if i % 2 == 0]


Line #    Mem usage    Increment   Line Contents
================================================
    33     32.8 MiB     32.8 MiB   @profile
    34                             def func_3(nums):
    35     34.7 MiB      0.2 MiB       return list(filter(lambda x: x % 2 == 0, nums))

"""