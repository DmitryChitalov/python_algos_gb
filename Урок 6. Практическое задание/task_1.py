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
Filename: C:/Users/Катя/PycharmProjects/untitled6/1.py

Line #    Mem usage    Increment   Line Contents
================================================
    24     15.4 MiB     15.4 MiB   @profile
    25                             def func_1(nums):
    26     15.4 MiB      0.0 MiB       new_arr = []
    27     16.2 MiB      0.0 MiB       for i in range(len(nums)):
    28     16.2 MiB      0.1 MiB           if nums[i] % 2 == 0:
    29     16.2 MiB      0.0 MiB               new_arr.append(i)
    30     16.2 MiB      0.0 MiB       return new_arr


Filename: C:/Users/Катя/PycharmProjects/untitled6/1.py

Line #    Mem usage    Increment   Line Contents
================================================
    33     15.8 MiB     15.8 MiB   @profile
    34                             def func_2(nums):
    35     15.8 MiB      0.0 MiB       return [i for i in nums if i % 2 == 0]


Filename: C:/Users/Катя/PycharmProjects/untitled6/1.py

Line #    Mem usage    Increment   Line Contents
================================================
    38     15.8 MiB     15.8 MiB   @profile
    39                             def func_3(nums):
    40     16.2 MiB      0.1 MiB       return [i for i, el in enumerate(nums) if el % 2 == 0]



###############################################################################################

Версия Python 3.8.3
Разрядность ОС 64-bit


Условие задачи:
Написать код, который позволяет сохранить в массиве индексы четных элементов другого массива.


Самым оптимальным способом решения данной задачи, с точки зрения использования памяти,
является второй способ (func_2), поскольку в инкременте мы видим нулевой прирост памяти (0.0 MiB)
в то время, как в первом и третьем способе (func_1 и func_3) присутствует прирост памяти, равный
0.1 MiB.

###############################################################################################

"""