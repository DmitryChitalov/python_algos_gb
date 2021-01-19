"""
1.	Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи.
Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.


ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""

# Я выбрала четвертую задачу из Лекции4 - надо определяется число, которое встречается в массиве чаще всего.
# Она как раз решена тремя способами - можно их сравнить.


import random
from timeit import timeit
import sys
from memory_profiler import profile

array = [random.randint(0, 10) for el in range(100000)]  # 1 сложность зависит от кол-ва элементов в range (n)

@profile
def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'

#Line #    Mem usage    Increment  Occurences   Line Contents
#============================================================
#    25     18.4 MiB     18.4 MiB           1   @profile
#    26                                         def func_1():
#    27     18.4 MiB      0.0 MiB           1       m = 0
#    28     18.4 MiB      0.0 MiB           1       num = 0
#    29     18.4 MiB      0.0 MiB       10001       for i in array:
#    30     18.4 MiB      0.0 MiB       10000           count = array.count(i)
#    31     18.4 MiB      0.0 MiB       10000           if count > m:
#    32     18.4 MiB      0.0 MiB           2               m = count
#    33     18.4 MiB      0.0 MiB           2               num = i
#    34     18.4 MiB      0.0 MiB           1       return f'Чаще всего встречается число {num}, ' \
#    35                                                    f'оно появилось в массиве {m} раз(а)'
#Чаще всего встречается число 10, оно появилось в массиве 955 раз(а)


@profile
def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'

#Line #    Mem usage    Increment  Occurences   Line Contents
#============================================================
#    40     18.4 MiB     18.4 MiB           1   @profile
#    41                                         def func_2():
#    42     18.4 MiB      0.0 MiB           1       new_array = []
#    43     18.6 MiB      0.0 MiB       10001       for el in array:
#    44     18.6 MiB      0.0 MiB       10000           count2 = array.count(el)
#    45     18.6 MiB      0.2 MiB       10000           new_array.append(count2)
#    46
#    47     18.6 MiB      0.0 MiB           1       max_2 = max(new_array)
#    48     18.6 MiB      0.0 MiB           1       elem = array[new_array.index(max_2)]
#    49     18.6 MiB      0.0 MiB           1       return f'Чаще всего встречается число {elem}, ' \
#    50                                                    f'оно появилось в массиве {max_2} раз(а)'

@profile
def func_3():
    numb = max(array, key=array.count)
    return f"Чаще всего встречается число {numb}, оно появилось в массиве {array.count(numb)} раз(а)"


print(func_1())
print(func_2())
print(func_3())

#Line #    Mem usage    Increment  Occurences   Line Contents
#============================================================
#    52     18.5 MiB     18.5 MiB           1   @profile
#    53                                         def func_3():
#    54     18.5 MiB      0.0 MiB           1       numb = max(array, key=array.count)
#    55     18.5 MiB      0.0 MiB           1       return f"Чаще всего встречается число {numb}, оно появилось в массиве {array.count(numb)} раз(а)"


# У меня стоит Python 3.8, Windows 10, разрядность 64.
# Занятость памяти:
# 1 - 18.4 MiB
# 2 - 18.4 MiB
# 5 - 18.5 MiB

# Интересно, что в первом и втором случае сперва выделяется одинаковое количество памяти, затем во втором идет
# некий прирост (до 18.6 MiB), так как внутри функции создается новые массив. Третий вариант стабилен по памяти.
# Получается, что самые хорошие - первый и третий.
# * по времени самый быстрый вариант был третий, а долгий - как раз второй.

