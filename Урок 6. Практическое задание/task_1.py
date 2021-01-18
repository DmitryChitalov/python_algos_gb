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
import numpy as np

nums = [i for i in range(1000000)]


@profile
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


@profile
def func_2(nums):
    new_arr = [j for i, j in enumerate(nums) if not i % 2]
    return new_arr


@profile
def func_3(nums):
    new_arr = np.array([j for i, j in enumerate(nums) if not i % 2], dtype=np.int32)
    return new_arr


func_1(nums)
func_2(nums)
func_3(nums)

r"""
Filename: D:\GB Study\python_algos_gb\Урок 6. Практическое задание\task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    22     69.2 MiB     69.2 MiB           1   @profile
    23                                         def func_1(nums):
    24     69.2 MiB      0.0 MiB           1       new_arr = []
    25     89.3 MiB -20627.6 MiB     1000001       for i in range(len(nums)):
    26     89.3 MiB -20612.1 MiB     1000000           if nums[i] % 2 == 0:
    27     89.3 MiB -10308.9 MiB      500000               new_arr.append(i)
    28     89.3 MiB      0.0 MiB           1       return new_arr


Filename: D:\GB Study\python_algos_gb\Урок 6. Практическое задание\task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    31     70.3 MiB     70.3 MiB           1   @profile
    32                                         def func_2(nums):
    33     74.0 MiB -97144.5 MiB     1000003       new_arr = [j for i, j in enumerate(nums) if not i % 2]
    34     74.0 MiB      0.0 MiB           1       return new_arr


Filename: D:\GB Study\python_algos_gb\Урок 6. Практическое задание\task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    37     70.2 MiB     70.2 MiB           1   @profile
    38                                         def func_3(nums):
    39     74.0 MiB -96784.3 MiB     1000003       new_arr = np.array([j for i, j in enumerate(nums) if not i % 2], dtype=np.int32)
    40     72.1 MiB     -1.9 MiB           1       return new_arr

Выше приведены результаты профилирования  памяти для 3-х разных функций выполняющих одну и ту же задачу
как видно из замеров, наиболее неэффективная с точки зрения использование памяти - func_1() порядка 20,1 MiB такой
результат получается из-за работы с двумя объемными массивами nums и new_arr.
Более эффективной функция становится при использовании list comprehensions - func_2() использует уже 3,7 MiB
Максимально сократить результирующее использование памяти в результате получилось в func_3() - пиковая нагрузка 
составляет 3,8 MiB, однако в итоге удается сократить количество памяти на 1,9 MiB при помощи использования 
библиотеки numpy и по завершению получается 1,9 MiB использует последняя функция.
Использован python 3.9 и Win10x64 
"""