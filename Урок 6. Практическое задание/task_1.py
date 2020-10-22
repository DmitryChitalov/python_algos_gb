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

from random import randint
from memory_profiler import profile

lst = [randint(0, 100) for i in range(10)]

print(lst)


@profile
def get_min():
    # Функция обеспечивает поиск минимального значения массива
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[j] < lst[i]:
                lst[i], lst[j] = lst[j], lst[i]
        return lst[i]


print(get_min())


@profile
def func_1():
    # Вариант 1
    # Функция определяет какое число встречается в массиве наибольшее число раз и подсчитывает количество повторений
    m = 0
    num = 0
    for i in lst:
        count = lst.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а).'


print(func_1())


@profile
def func_2():
    # Вариант 2
    # Функция определяет какое число встречается в массиве наибольшее число раз и подсчитывает количество повторений
    new_lst = []
    for el in lst:
        count2 = lst.count(el)
        new_lst.append(count2)

    max_2 = max(new_lst)
    elem = lst[new_lst.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а).'


print(func_2())


@profile
def func_3():
    # Вариант 3
    # Функция определяет какое число встречается в массиве наибольшее число раз и подсчитывает количество повторений
    res = max(lst, key=lst.count)
    return f'Чаще всего встречается число {res}, ' \
           f'оно появилось в массиве {lst.count(res)} раз(а).'


print(func_3())

'''
Python 3.8.2
Windows 10 x64

Filename: D:/Lessons/python_projects/algos/#6/#6_task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    26     15.5 MiB     15.5 MiB           1   @profile
    27                                         def get_min():
    28     15.5 MiB      0.0 MiB           1       for i in range(len(lst)):
    29     15.5 MiB      0.0 MiB          11           for j in range(len(lst)):
    30     15.5 MiB      0.0 MiB          10               if lst[j] < lst[i]:
    31     15.5 MiB      0.0 MiB           3                   lst[i], lst[j] = lst[j], lst[i]
    32     15.5 MiB      0.0 MiB           1           return lst[i]


0
Filename: D:/Lessons/python_projects/algos/#6/#6_task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    38     15.5 MiB     15.5 MiB           1   @profile
    39                                         def func_1():
    40     15.5 MiB      0.0 MiB           1       m = 0
    41     15.5 MiB      0.0 MiB           1       num = 0
    42     15.5 MiB      0.0 MiB          11       for i in lst:
    43     15.5 MiB      0.0 MiB          10           count = lst.count(i)
    44     15.5 MiB      0.0 MiB          10           if count > m:
    45     15.5 MiB      0.0 MiB           2               m = count
    46     15.5 MiB      0.0 MiB           2               num = i
    47     15.5 MiB      0.0 MiB           1       return f'Чаще всего встречается число {num}, ' \
    48                                                    f'оно появилось в массиве {m} раз(а).'


Чаще всего встречается число 50, оно появилось в массиве 2 раз(а).
Filename: D:/Lessons/python_projects/algos/#6/#6_task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    54     15.5 MiB     15.5 MiB           1   @profile
    55                                         def func_2():
    56     15.5 MiB      0.0 MiB           1       new_lst = []
    57     15.5 MiB      0.0 MiB          11       for el in lst:
    58     15.5 MiB      0.0 MiB          10           count2 = lst.count(el)
    59     15.5 MiB      0.0 MiB          10           new_lst.append(count2)
    60                                         
    61     15.5 MiB      0.0 MiB           1       max_2 = max(new_lst)
    62     15.5 MiB      0.0 MiB           1       elem = lst[new_lst.index(max_2)]
    63     15.5 MiB      0.0 MiB           1       return f'Чаще всего встречается число {elem}, ' \
    64                                                    f'оно появилось в массиве {max_2} раз(а).'


Чаще всего встречается число 50, оно появилось в массиве 2 раз(а).
Filename: D:/Lessons/python_projects/algos/#6/#6_task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    70     15.5 MiB     15.5 MiB           1   @profile
    71                                         def func_3():
    72     15.5 MiB      0.0 MiB           1       res = max(lst, key=lst.count)
    73     15.5 MiB      0.0 MiB           1       return f'Чаще всего встречается число {res}, ' \
    74                                                    f'оно появилось в массиве {lst.count(res)} раз(а).'


Во всех функциях профайлер показывает нулевой инкремент, т.е. прироста расхода памяти в данных функциях не наблюдается 
даже при 10-кратных прогонах по списку, что скорее всего обусловлено их простотой.
'''