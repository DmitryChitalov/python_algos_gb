"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-5 ваших разных скриптов!.
Сделать их разные реализации.

Можно взять задачи с курса Основ
или с текущего курса Алгоритмов

Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""

# Версия Python 3.8, разрядность ОС 64 бита
# Здесь в двух первых реализациях функции позволяют сохранить в массиве индексы четных элементов другого массива
# Первый пример реализации

from memory_profiler import profile
from random import randint


@profile
def func_1():
    new_arr = []
    my_lst = [el for el in range(100000)]
    for i in range(len(my_lst)):
        if my_lst[i] % 2 == 0:
            new_arr.append(i)
    del my_lst
    return new_arr

# Второй пример реализации

@profile
def func_2():
    my_lst = [el for el in range(100000)]
    return [i for i, el in enumerate(my_lst) if el % 2 == 0]


if __name__ == "__main__":
    func_1()
    func_2()

'''В данном случае лучше сработала функция func_1 с циклом for в сравнении c func_2, где для вывода использовалось
генераторное выражение. Результаты:
 Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    31     15.9 MiB     15.9 MiB           1   @profile
    32                                         def func_1():
    33     15.9 MiB      0.0 MiB           1       new_arr = []
    34     17.9 MiB      2.0 MiB      100003       my_lst = [el for el in range(100000)]
    35     19.3 MiB      0.0 MiB      100001       for i in range(len(my_lst)):
    36     19.3 MiB      0.8 MiB      100000           if my_lst[i] % 2 == 0:
    37     19.3 MiB      0.5 MiB       50000               new_arr.append(i)
    38     17.5 MiB     -1.8 MiB           1       del my_lst
    39     17.5 MiB      0.0 MiB           1       return new_arr
    
    43     16.3 MiB     16.3 MiB           1   @profile
    44                                         def func_2():
    45     18.1 MiB    -96.3 MiB      100003       my_lst = [el for el in range(100000)]
    46     18.9 MiB      0.8 MiB      100003       return [i for i, el in enumerate(my_lst) if el % 2 == 0]
    
    Не ожидал, что вторая функция сработает хуже с точки зрения памяти, т.к. запись более лаконичная и генераторное 
    выражение срабатывает, как правило, быстрее обычного цикла. Кроме того, снизило затраты памяти указание в коде
    на del my_lst. 
    
'''

# Здесь приведены функции, формирующие из введенного числа обратное по порядку входящих в него цифр.
# Первый пример реализации

@profile
def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num

# Второй пример реализации

@profile
def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


if __name__ == "__main__":
    revers_2(randint(1000000000000, 10000000000000))
    revers_3(randint(1000000000000, 10000000000000))

''' Результаты:
 Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    76     15.9 MiB     15.9 MiB           1   @profile
    77                                         def revers_2(enter_num, revers_num=0):
    78     15.9 MiB      0.0 MiB          14       while enter_num != 0:
    79     15.9 MiB      0.0 MiB          13           num = enter_num % 10
    80     15.9 MiB      0.0 MiB          13           revers_num = (revers_num + num / 10) * 10
    81     15.9 MiB      0.0 MiB          13           enter_num //= 10
    82     15.9 MiB      0.0 MiB           1       return revers_num
    
    84     16.0 MiB     16.0 MiB           1   @profile
    85                                         def revers_3(enter_num):
    86     16.0 MiB      0.0 MiB           1       enter_num = str(enter_num)
    87     16.0 MiB      0.0 MiB           1       revers_num = enter_num[::-1]
    88     16.0 MiB      0.0 MiB           1       return revers_num
    
    Неожиданный результат. Функция со вложенным циклом сработала, с точки зрения памяти, лучше функции,
    использующей в своем теле встроенные функции, которые позволяют сделать реализацию кода быстрее. 
 '''