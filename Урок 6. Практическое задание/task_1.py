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
from random import randint


'''Версия операционной системы Windows 10, 64 разрядная, версия Python - 3.9
Т.к все скрипьты небольшие, нет особых вопросов с памятью.

Проблемы были с установкой  memory_profiler, т.к. она зависит от Psutil, Psutol в свою
 очередь не хотел устанавливаться и пришлось сначала устанавливать 
Microsoft Visual Studio с его библиотеками, а конкретно необхадима была  Microsoft Visual C++,
 после этого установил  Psutil, и после этого уже memory_profiler. 
'''
@profile
def function_1(lst):
    for i in lst:
        is_min = True
        for j in lst:
            if i > j:
                is_min = False
        if is_min:
            return i

'''Результаты:
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    28     19.2 MiB     19.2 MiB           1   @profile
    29                                         def function_1(lst):
    30     19.2 MiB      0.0 MiB           8       for i in lst:
    31     19.2 MiB      0.0 MiB           8           is_min = True
    32     19.2 MiB      0.0 MiB         168           for j in lst:
    33     19.2 MiB      0.0 MiB         160               if i > j:
    34     19.2 MiB      0.0 MiB          91                   is_min = False
    35     19.2 MiB      0.0 MiB           8           if is_min:
    36     19.2 MiB      0.0 MiB           1               return i
'''

@profile
def function_2(lst):
    min_value = lst[0]
    for i in lst:
        if i in lst:
            min_value = i
    return min_value

'''Результаты
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    38     19.2 MiB     19.2 MiB           1   @profile
    39                                         def function_2(lst):
    40     19.2 MiB      0.0 MiB           1       min_value = lst[0]
    41     19.2 MiB      0.0 MiB          21       for i in lst:
    42     19.2 MiB      0.0 MiB          20           if i in lst:
    43     19.2 MiB      0.0 MiB          20               min_value = i
    44     19.2 MiB      0.0 MiB           1       return min_value
'''

@profile
def function_3():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'

'''Результаты
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    46     19.2 MiB     19.2 MiB           1   @profile
    47                                         def function_3():
    48     19.2 MiB      0.0 MiB           1       m = 0
    49     19.2 MiB      0.0 MiB           1       num = 0
    50     19.2 MiB      0.0 MiB           8       for i in array:
    51     19.2 MiB      0.0 MiB           7           count = array.count(i)
    52     19.2 MiB      0.0 MiB           7           if count > m:
    53     19.2 MiB      0.0 MiB           1               m = count
    54     19.2 MiB      0.0 MiB           1               num = i
    55     19.2 MiB      0.0 MiB           2       return f'Чаще всего встречается число {num}, ' \
    56     19.2 MiB      0.0 MiB           1              f'оно появилось в массиве {m} раз(а)'

'''
@profile
def function_4():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'

'''Результаты
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    58     19.2 MiB     19.2 MiB           1   @profile
    59                                         def function_4():
    60     19.2 MiB      0.0 MiB           1       new_array = []
    61     19.2 MiB      0.0 MiB           8       for el in array:
    62     19.2 MiB      0.0 MiB           7           count2 = array.count(el)
    63     19.2 MiB      0.0 MiB           7           new_array.append(count2)
    64                                         
    65     19.2 MiB      0.0 MiB           1       max_2 = max(new_array)
    66     19.2 MiB      0.0 MiB           1       elem = array[new_array.index(max_2)]
    67     19.2 MiB      0.0 MiB           2       return f'Чаще всего встречается число {elem}, ' \
    68     19.2 MiB      0.0 MiB           1              f'оно появилось в массиве {max_2} раз(а)'

'''
@profile
def function_5(i):
    count = 1
    n = 2
    while count <= i:
        t = 1
        is_simple = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if count == i:
                break
            count += 1
        n += 1
    return n

lst1 = [randint(0, 100) for i in range(20)]
array = [1, 3, 1, 3, 4, 5, 1]

if __name__ == "__main__":
    function_1(lst1)
    function_2(lst1)
    function_3()
    function_4()
    function_5(50)

''' Результаты
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    70     19.2 MiB     19.2 MiB           1   @profile
    71                                         def function_5(i):
    72     19.2 MiB      0.0 MiB           1       count = 1
    73     19.2 MiB      0.0 MiB           1       n = 2
    74     19.2 MiB      0.0 MiB         228       while count <= i:
    75     19.2 MiB      0.0 MiB         228           t = 1
    76     19.2 MiB      0.0 MiB         228           is_simple = True
    77     19.2 MiB      0.0 MiB        5700           while t <= n:
    78     19.2 MiB      0.0 MiB        5650               if n % t == 0 and t != 1 and t != n:
    79     19.2 MiB      0.0 MiB         178                   is_simple = False
    80     19.2 MiB      0.0 MiB         178                   break
    81     19.2 MiB      0.0 MiB        5472               t += 1
    82     19.2 MiB      0.0 MiB         228           if is_simple:
    83     19.2 MiB      0.0 MiB          50               if count == i:
    84     19.2 MiB      0.0 MiB           1                   break
    85     19.2 MiB      0.0 MiB          49               count += 1
    86     19.2 MiB      0.0 MiB         227           n += 1
    87     19.2 MiB      0.0 MiB           1       return n
'''



