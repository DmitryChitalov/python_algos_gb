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
from memory_profiler import profile, memory_usage
from random import randint


# import numpy as np

@profile
def func_1():
    array_data = [randint(-100, 100) for _ in range(5000)]
    m = 0
    num = 0
    for i in array_data:
        count = array_data.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


@profile
def func_2():
    array_data = [randint(-100, 100) for _ in range(5000)]
    new_array = []
    for el in array_data:
        count2 = array_data.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array_data[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


@profile
def func_3():
    array_data = [randint(-100, 100) for _ in range(5000)]
    max_el = sorted([(i, array_data.count(i)) for i in set(array_data)], key=lambda t: t[1])[-1]
    return f'Чаще всего встречается число {max_el[0]}, ' \
           f'оно появилось в массиве {max_el[1]} раз(а)'


def gen(numbers):
    for num in numbers:
        yield numbers.count(num)  # np.sum(numbers==num)


@profile
def func_4():
    # lst_obj = np.array([randint(-100, 100) for _ in range(5000)])
    lst_obj = [randint(-100, 100) for _ in range(5000)]
    t = tuple(i for i in gen(lst_obj))
    max_2 = max(t)
    elem = lst_obj[t.index(max_2)]
    del lst_obj
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


if __name__ == "__main__":
    m1 = memory_usage()
    result1 = func_1()
    m2 = memory_usage()
    print(f"Результат 1 - {result1}, затрачено памяти: {m2[0] - m1[0]}")

    m1 = memory_usage()
    result2 = func_2()
    m2 = memory_usage()
    print(f"Результат 2 - {result2}, затрачено памяти: {m2[0] - m1[0]}")

    m1 = memory_usage()
    result3 = func_3()
    m2 = memory_usage()
    print(f"Результат 3 - {result3}, затрачено памяти: {m2[0] - m1[0]}")

    m1 = memory_usage()
    result4 = func_4()
    m2 = memory_usage()
    print(f"Результат 4 - {result4}, затрачено памяти: {m2[0] - m1[0]}")

"""
ОС: Windows 10 64-x
Версия Python: 3.7.9
Использовал numpy, в итоге память увеличилась почти в два раза - 30.4 MiB.
Использовал в функции 4 генератор и кортеж, но результата не увидел.

Результат 1 - Чаще всего встречается число 63, оно появилось в массиве 39 раз(а), затрачено памяти: 0.17578125
Результат 2 - Чаще всего встречается число 39, оно появилось в массиве 38 раз(а), затрачено памяти: 0.0
Результат 3 - Чаще всего встречается число -22, оно появилось в массиве 38 раз(а), затрачено памяти: 0.0
Результат 4 - Чаще всего встречается число 97, оно появилось в массиве 39 раз(а), затрачено памяти: 0.0

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    21     18.7 MiB     18.7 MiB           1   @profile
    22                                         def func_1():
    23     18.8 MiB      0.1 MiB        5003       array_data = [randint(-100, 100) for _ in range(5000)]
    24     18.8 MiB      0.0 MiB           1       m = 0
    25     18.8 MiB      0.0 MiB           1       num = 0
    26     18.8 MiB      0.0 MiB        5001       for i in array_data:
    27     18.8 MiB      0.0 MiB        5000           count = array_data.count(i)
    28     18.8 MiB      0.0 MiB        5000           if count > m:
    29     18.8 MiB      0.0 MiB           8               m = count
    30     18.8 MiB      0.0 MiB           8               num = i
    31     18.8 MiB      0.0 MiB           1       return f'Чаще всего встречается число {num}, ' \
    32                                                    f'оно появилось в массиве {m} раз(а)'


Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    34     18.8 MiB     18.8 MiB           1   @profile
    35                                         def func_2():
    36     18.8 MiB      0.0 MiB        5003       array_data = [randint(-100, 100) for _ in range(5000)]
    37     18.8 MiB      0.0 MiB           1       new_array = []
    38     18.9 MiB      0.0 MiB        5001       for el in array_data:
    39     18.9 MiB      0.0 MiB        5000           count2 = array_data.count(el)
    40     18.9 MiB      0.0 MiB        5000           new_array.append(count2)
    41                                         
    42     18.9 MiB      0.0 MiB           1       max_2 = max(new_array)
    43     18.9 MiB      0.0 MiB           1       elem = array_data[new_array.index(max_2)]
    44     18.9 MiB      0.0 MiB           1       return f'Чаще всего встречается число {elem}, ' \
    45                                                    f'оно появилось в массиве {max_2} раз(а)'


Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    63     18.9 MiB     18.9 MiB           1   @profile
    64                                         def func_3():
    65     18.9 MiB      0.0 MiB        5003       array_data = [randint(-100, 100) for _ in range(5000)]
    66     18.9 MiB      0.0 MiB         606       max_el = sorted([(i, array_data.count(i)) for i in set(array_data)], key=lambda t: t[1])[-1]
    67     18.9 MiB      0.0 MiB           1       return f'Чаще всего встречается число {max_el[0]}, ' \
    68                                                    f'оно появилось в массиве {max_el[1]} раз(а)'


Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    52     18.9 MiB     18.9 MiB           1   @profile
    53                                         def func_4():
    54                                             # lst_obj = np.array([randint(-100, 100) for _ in range(5000)])
    55     18.9 MiB      0.0 MiB        5003       lst_obj = [randint(-100, 100) for _ in range(5000)]
    56     18.9 MiB      0.0 MiB       10003       t = tuple(i for i in gen(lst_obj))
    57     18.9 MiB      0.0 MiB           1       max_2 = max(t)
    58     18.9 MiB      0.0 MiB           1       elem = lst_obj[t.index(max_2)]
    59     18.9 MiB      0.0 MiB           1       del lst_obj
    60     18.9 MiB      0.0 MiB           1       return f'Чаще всего встречается число {elem}, ' \
    61                                                    f'оно появилось в массиве {max_2} раз(а)'

"""
