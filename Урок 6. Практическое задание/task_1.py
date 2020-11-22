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


from memory_profiler import profile
from timeit import default_timer

    # Filling up a list cubed

# via while loop:

@profile
def lst_gen_func_1():
    a = []
    i = 0
    while i < 100000:
        a.append(i ** 3)
        i += 1
    return a

start_time = default_timer()
lst_gen_func_1()
print(f'The while loop runs for {default_timer() - start_time} sec.')


# via list comprehension:

@profile
def lst_gen_func_2():
    return list(j ** 3 for j in range(0, 100000))

start_time = default_timer()
lst_gen_func_2()
print(f'The list comprehension runs for {default_timer() - start_time} sec.')


'''
    # While loop data: 
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    43     13.0 MiB     13.0 MiB           1   @profile
    44                                         def lst_gen_func_1():
    45     13.0 MiB      0.0 MiB           1       a = []
    46     13.0 MiB      0.0 MiB           1       i = 0
    47     20.0 MiB      0.0 MiB      100001       while i < 100000:
    48     20.0 MiB      7.0 MiB      100000           a.append(i ** 3)
    49     20.0 MiB      0.0 MiB      100000           i += 1
    50     20.0 MiB      0.0 MiB           1       return a


The while loop runs for 13.463636318 sec.


    #List comprehension data: 
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    59     17.9 MiB     17.9 MiB           1   @profile
    60                                         def lst_gen_func_2():
    61     18.4 MiB      0.5 MiB      200003       return list(j ** 3 for j in range(0, 100000))


The list comprehension runs for 9.073802811999998 sec.


Итак, я взял два примера реализации одной и той же функции, которая заполняет формирует/заполняет лист элементами в кубе - 
первая реализована через while, вторая - через ген. выражение. 
В итоге видно, что while-функция ожидаемо отработала хуже - и по времени, и, самое, главное, по памяти, т.к. прирост составил в среднем
7-9 MiB (после 5 прогонов). Ген. выражение сработало лучше - опять же, ожидаемо - и прирост в потреблении памяти довольно маленький - 
в среднем 0.5 - 1.5 MiB.

Что касается системы - у меня Python 3.8.6, Catalina x64
'''
























