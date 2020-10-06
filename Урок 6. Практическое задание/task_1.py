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
from timeit import timeit
from random import randint

'''
nums = [randint(-100, 100) for _ in range(100000)]

@profile
def func_1():
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

print(timeit("func_1()", setup="from __main__ import func_1", number=1))

Line #    Mem usage    Increment   Line Contents
================================================
    93     16.2 MiB     16.2 MiB   @profile
    94                             def func_1():
    95     16.2 MiB      0.0 MiB       new_arr = []
    96     18.2 MiB      0.3 MiB       for i in range(len(nums)):
    97     18.2 MiB      0.0 MiB           if nums[i] % 2 == 0:
    98     18.2 MiB      0.3 MiB               new_arr.append(i)
    99     18.2 MiB      0.0 MiB       return new_arr


11.885895677987719
'''
'''
nums = [randint(-100, 100) for _ in range(100000)]
@profile
def func_2():
    new_arr = []
    for i, _ in enumerate(nums):  # заменил range -> enumerate
        if i % 2 == 0:
            new_arr.append(i)
    del new_arr


print(timeit("func_2()", setup="from __main__ import func_2", number=1))

Line #    Mem usage    Increment   Line Contents
================================================
   118     16.1 MiB     16.1 MiB   @profile
   119                             def func_2():
   120     16.1 MiB      0.0 MiB       new_arr = []
   121     18.3 MiB      0.3 MiB       for i, _ in enumerate(nums):  # заменил range -> enumerate
   122     18.3 MiB      0.0 MiB           if i % 2 == 0:
   123     18.3 MiB      0.3 MiB               new_arr.append(i)
   124     16.7 MiB      0.0 MiB       del new_arr


12.188914469006704
'''

# Вывод: При практически одинковых функциях видим, что
# 1) память на выполнение функий выделяется практически одинаково (Mem usage почти одинаково);
# 2) for i in range(len(nums)) и for i, _ in enumerate(nums) используют одинаковое количество памяти (Increment в обоих случаях = 0.3 MiB);
# 3) Сборщик мусора работает т.к. в примере № 2 был использован del new_arr, что позволило освободить 18.3 MiB - 16.7 MiB = 1.6 MiB
# 4) Алгоритм работы profile надо дорабатывать т.к. он считает память не всегда корректно,
# пример #1 стока 120 и 121 инкремент отсутствует значение увеличилось, #2 строка 121 и 122 инкремент есть значение Mem usage не изменилось.

# Python 3.8.2
# Linux Mint 20 Ulyana x64
