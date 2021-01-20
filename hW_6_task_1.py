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
"""
Задача № 1
И так я взял 4 различных реализациии отбора четных числе из массива в 100 000 числел
При этом я тестировал все функции по 2-м параметрам: время выполнения функции и ежесекундный
контроль использования памяти функцией при помощи memory_usage.
Результат теста выводит профилирование использования памяти, время выполнения функции, а также минимальное
и максимальное количество используемой памяти в процессе работы функции с интервалом 1 секунда.
Из результатов видно, что наиболее оптимизированно отработала реализация под №3 - генераторное выражение
с использованием нумерованного массива. Эта версия и работает быстрее остальных вариантов, дает наименьший 
инкремент памяти в процессе выполнения и наименьшее максимальное количество используемой памяти в процессе
выполнения.
Для задачи № 2 - формирование словаря из элементов списка чисел от 1 до 100 000 не кратных числу 3, где в качестве
ключа использутся индекс значения в списке а в качестве значения само значение и дальнейшее получение списка из 
ключей сформированного словаря я сделал аналогичные измерения.
"Листирование" ключей словаря работает быстрее, чем выборка ключей словаря при помощи генераторного выражения и метода
iteams. Но главное - это экономия памяти более 10%.
Задача по одновременному профилированию использования памяти и времени выполнения функци также выполнена.
Результаты всех замеров приведены ниже.
Выполнение тестирования производилось на Windows10 x64, Python 3.8
"""
from timeit import Timer, timeit, default_timer
from memory_profiler import profile, memory_usage

mass_1 = [i for i in range(100000)]


@profile
def func_1():
    new_arr = []
    for i in range(len(mass_1)):
        if mass_1[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


@profile
def func_2():
    new_arr = [i for i in range(len(mass_1)) if mass_1[i] % 2 == 0]
    return new_arr


@profile
def func_3():
    new_arr = [v for k, v in enumerate(mass_1) if v % 2 == 0]
    return new_arr


@profile
def func_4():
    new_arr = [mass_1.index(el) for el in mass_1 if el % 2 == 0]
    return new_arr


def use_time(func):
    def wrapped(*args):
        start_time = default_timer()
        func(*args)
        print(f' Эта функция выполнялась {round((default_timer() - start_time),4)} секунд')
    return  wrapped


@profile()
def create_list_1():
    my_list = [i for i in range(100000) if i % 3 != 0]
    my_dict = {i: my_list.index(i) for i in my_list}
    new_list = [k for k in my_dict.items()]
    return my_list, my_dict, new_list


@profile
def create_list_2():
    my_list = [i for i in range(100000) if i % 3 != 0]
    my_dict = {i: my_list.index(i) for i in my_list}
    new_list = list(my_dict.keys())
    return my_list, my_dict, new_list


if __name__ == '__main__':
    @use_time
    def mem_use(func):
        mem_usage = memory_usage(func, interval=1)
        print(f' Минимальное количеcтво используемой памяти \n '
              f'в процессе выполнения cоставляет {round((min(mem_usage)), 4)} MiB \n '
              f'максимальное количество используемой памяти {round((max(mem_usage)), 4)} MiB')


    mem_use(func_1)
    # mem_use(func_2)
    # mem_use(func_3)
    # mem_use(func_4)
    # mem_use(create_list_1)
    # mem_use(create_list_2)

"""

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    29     23.0 MiB     23.0 MiB           1   @profile
    30                                         def func_1():
    31     23.0 MiB      0.0 MiB           1       new_arr = []
    32     25.5 MiB      0.0 MiB      100001       for i in range(len(mass_1)):
    33     25.5 MiB      1.5 MiB      100000           if mass_1[i] % 2 == 0:
    34     25.5 MiB      0.9 MiB       50000               new_arr.append(i)
    35     25.5 MiB      0.0 MiB           1       return new_arr


 Минимальное количеcтво используемой памяти 
 в процессе выполнения cоставляет 22.5547 MiB 
 максимальное количество используемой памяти 25.5195 MiB
 Эта функция выполнялась 5.4342 секунд

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    38     23.2 MiB     23.2 MiB           1   @profile
    39                                         def func_2():
    40     25.0 MiB      1.9 MiB      100003       new_arr = [i for i in range(len(mass_1)) if mass_1[i] % 2 == 0]
    41     25.0 MiB      0.0 MiB           1       return new_arr


 Минимальное количеcтво используемой памяти 
 в процессе выполнения cоставляет 23.1523 MiB 
 максимальное количество используемой памяти 25.043 MiB
 Эта функция выполнялась 2.2426 секунд

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    44     23.4 MiB     23.4 MiB           1   @profile
    45                                         def func_3():
    46     24.0 MiB      0.6 MiB      100003       new_arr = [v for k, v in enumerate(mass_1) if v % 2 == 0]
    47     24.0 MiB      0.0 MiB           1       return new_arr


 Минимальное количеcтво используемой памяти 
 в процессе выполнения cоставляет 23.4023 MiB 
 максимальное количество используемой памяти 24.043 MiB
 Эта функция выполнялась 2.2186 секунд

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    50     23.4 MiB     23.4 MiB           1   @profile
    51                                         def func_4():
    52     25.1 MiB      1.7 MiB      100003       new_arr = [mass_1.index(el) for el in mass_1 if el % 2 == 0]
    53     25.1 MiB      0.0 MiB           1       return new_arr


 Минимальное количеcтво используемой памяти 
 в процессе выполнения cоставляет 23.4023 MiB 
 максимальное количество используемой памяти 25.0742 MiB
 Эта функция выполнялась 26.8483 секунд
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    62     23.5 MiB     23.5 MiB           1   @profile()
    63                                         def create_list_1():
    64     25.5 MiB      2.0 MiB      100003       my_list = [i for i in range(100000) if i%3 != 0]
    65     30.0 MiB     -5.0 MiB       66669       my_dict = {i:my_list.index(i) for i in my_list}
    66     34.9 MiB      4.8 MiB       66669       new_list = [k for k in my_dict.items()]
    67     34.9 MiB      0.0 MiB           1       return my_list, my_dict, new_list


 Минимальное количеcтво используемой памяти
 в процессе выполнения cоставляет 23.4961 MiB
 максимальное количество используемой памяти 34.8672 MiB
 Эта функция выполнялась 26.1308 секунд

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    69     23.8 MiB     23.8 MiB           1   @profile
    70                                         def create_list_2():
    71     25.5 MiB      1.8 MiB      100003       my_list = [i for i in range(100000) if i%3 != 0]
    72     30.1 MiB      4.5 MiB       66669       my_dict = {i:my_list.index(i) for i in my_list}
    73     30.6 MiB      0.5 MiB           1       new_list = list(my_dict.keys())
    74     30.6 MiB      0.0 MiB           1       return my_list, my_dict, new_list


 Минимальное количеcтво используемой памяти
 в процессе выполнения cоставляет 23.7773 MiB
 максимальное количество используемой памяти 30.582 MiB
 Эта функция выполнялась 24.7524 секунд
"""

