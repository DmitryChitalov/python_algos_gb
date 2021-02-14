"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять задачи с курса Основ
или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""

from memory_profiler import profile


@profile
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


@profile
def func_2(nums):
    return [i for i in nums if i % 2 == 0]


@profile
def func_3(nums):
    return [i for i, el in enumerate(nums) if el % 2 == 0]


if __name__ == '__main__':
    NUMS = [el for el in range(100000)]
    func_1(NUMS)
    func_2(NUMS)
    func_3(NUMS)


"""
C:\Users\DENISF\Documents\GitHub\python_algos_gb\Урок 6. Практическое задание\task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    28     23.9 MiB     23.9 MiB           1   @profile
    29                                         def func_1(nums):
    30     23.9 MiB      0.0 MiB           1       new_arr = []
    31     25.4 MiB      0.0 MiB      100001       for i in range(len(nums)):
    32     25.4 MiB      1.5 MiB      100000           if nums[i] % 2 == 0:
    33     25.4 MiB      0.0 MiB       50000               new_arr.append(i)
    34     25.4 MiB      0.0 MiB           1       return new_arr


Filename: C:\Users\DENISF\Documents\GitHub\python_algos_gb\Урок 6. Практическое задание\task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    37     23.5 MiB     23.5 MiB           1   @profile
    38                                         def func_2(nums):
    39     24.0 MiB      0.5 MiB      100003       return [i for i in nums if i % 2 == 0]


Filename: C:\Users\DENISF\Documents\GitHub\python_algos_gb\Урок 6. Практическое задание\task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    42     24.0 MiB     24.0 MiB           1   @profile
    43                                         def func_3(nums):
    44     25.3 MiB      1.3 MiB      100003       return [i for i, el in enumerate(nums) if el % 2 == 0]



Process finished with exit code 0
###############################################################################################
Версия Python 3.9.1
Разрядность ОС 64-bit
Условие задачи:
Написать код, который позволяет сохранить в массиве индексы четных элементов другого массива.
Самым оптимальным способом решения данной задачи, с точки зрения использования памяти,
является второй способ (func_2), поскольку в инкременте мы видим меньший прирост памяти 0.5 MiB
в то время, как в первом и третьем способе (func_1 и func_3) присутствует прирост памяти, равный
1.5 и 1.3 MiB.
###############################################################################################
"""