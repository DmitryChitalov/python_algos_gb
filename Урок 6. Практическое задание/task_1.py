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

# 1-я задача: определение минимального числа в массиве.
# через цикл
@profile
def func_min_val():
    my_list = list(range(100000))
    min_val = my_list[0]
    for el in my_list[1:len(my_list)]:
        if el < min_val:
            min_val = el
    return min_val

# через встроенную функцию
@profile
def func_min_2():
    my_list = list(range(100000))
    return min(my_list)

# if __name__ == "__main__":
#     func_min_val()
#     func_min_2()

"""
Для запуска программы в 1 вар выделено 16,6 Mib, во 2м варианте 17.0 MiB.
В 1 варианте, памяти используется больше на 0,8 Mib - на 24 строке для проведения 
операция цикла было выделено больше памяти.
Среди данных вариантов - 2-я программа наиболее эффективно использует память.
  
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    20     16.6 MiB     16.6 MiB           1   @profile
    21                                         def func_min_val():
    22     20.5 MiB      3.8 MiB           1       my_list = list(range(100000))
    23     20.5 MiB      0.0 MiB           1       min_val = my_list[0]
    24     21.2 MiB      0.8 MiB      100000       for el in my_list[1:len(my_list)]:
    25     21.2 MiB      0.0 MiB       99999           if el < min_val:
    26                                                     min_val = el
    27     21.2 MiB      0.0 MiB           1       return min_val


Filename: C:/Users/Белорыбкина/PycharmProjects/algoritms/Урок 6. Практическое задание/task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    30     17.0 MiB     17.0 MiB           1   @profile
    31                                         def func_min_2():
    32     20.5 MiB      3.5 MiB           1       my_list = list(range(100000))
    33     20.5 MiB      0.0 MiB           1       return min(my_list)
"""
