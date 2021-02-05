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
import random

array = [random.randint(1, 150) for _ in range(10000)]


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


@profile
def func_3():
    dict_for_count = {}
    for el in array:
        if el in dict_for_count:
            dict_for_count[el] += 1
        else:
            dict_for_count[el] = 1
    num_count = max(dict_for_count.values())
    max_num = max(dict_for_count, key=dict_for_count.get)
    return f'Чаще всего встречается число {max_num}, ' \
           f'оно появилось в массиве {num_count} раз(а)'


print('***********************************************')
print('********************func_1*********************')
print('***********************************************')
func_1()
print('***********************************************')
print('********************func_2*********************')
print('***********************************************')
func_2()
print('***********************************************')
print('********************func_3*********************')
print('***********************************************')
func_3()

"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    21     19.8 MiB     19.8 MiB           1   @profile
    22                                         def func_1():
    23     19.8 MiB      0.0 MiB           1       m = 0
    24     19.8 MiB      0.0 MiB           1       num = 0
    25     19.8 MiB      0.0 MiB       10001       for i in array:
    26     19.8 MiB      0.0 MiB       10000           count = array.count(i)
    27     19.8 MiB      0.0 MiB       10000           if count > m:
    28     19.8 MiB      0.0 MiB           2               m = count
    29     19.8 MiB      0.0 MiB           2               num = i
    30     19.8 MiB      0.0 MiB           2       return f'Чаще всего встречается число {num}, ' \
    31     19.8 MiB      0.0 MiB           1              f'оно появилось в массиве {m} раз(а)'


***********************************************
********************func_2*********************
***********************************************
Filename: C:\Repos\Algoritms\python_algos_gb\Урок 6. Практическое задание\task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    33     19.8 MiB     19.8 MiB           1   @profile
    34                                         def func_2():
    35     19.8 MiB      0.0 MiB           1       new_array = []
    36     20.0 MiB      0.0 MiB       10001       for el in array:
    37     20.0 MiB      0.0 MiB       10000           count2 = array.count(el)
    38     20.0 MiB      0.2 MiB       10000           new_array.append(count2)
    39     20.0 MiB      0.0 MiB           1       max_2 = max(new_array)
    40     20.0 MiB      0.0 MiB           1       elem = array[new_array.index(max_2)]
    41     20.0 MiB      0.0 MiB           2       return f'Чаще всего встречается число {elem}, ' \
    42     20.0 MiB      0.0 MiB           1              f'оно появилось в массиве {max_2} раз(а)'


***********************************************
********************func_3*********************
***********************************************
Filename: C:\Repos\Algoritms\python_algos_gb\Урок 6. Практическое задание\task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    44     20.0 MiB     20.0 MiB           1   @profile
    45                                         def func_3():
    46     20.0 MiB      0.0 MiB           1       dict_for_count = {}
    47     20.0 MiB      0.0 MiB       10001       for el in array:
    48     20.0 MiB      0.0 MiB       10000           if el in dict_for_count:
    49     20.0 MiB      0.0 MiB        9995               dict_for_count[el] += 1
    50                                                 else:
    51     20.0 MiB      0.0 MiB           5               dict_for_count[el] = 1
    52     20.0 MiB      0.0 MiB           1       num_count = max(dict_for_count.values())
    53     20.0 MiB      0.0 MiB           1       max_num = max(dict_for_count, key=dict_for_count.get)
    54     20.0 MiB      0.0 MiB           2       return f'Чаще всего встречается число {max_num}, ' \
    55     20.0 MiB      0.0 MiB           1              f'оно появилось в массиве {num_count} раз(а)'


Долго сравнивал программы из пройденных курсов, и везде было всё по нулям, это значит, что все программы, написанные 
нами используют минимальное количество памяти. В данном примере, единственное, что можно заметить - небольшое выделение
памяти для заполнения нового списка (при увеличении начального размера списка программа не выполняется до конца
(ждал больше минуты).

Python 3.9.1 WINx64
"""
