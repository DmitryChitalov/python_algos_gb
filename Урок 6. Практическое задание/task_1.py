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
from memory_profiler import profile, memory_usage

'''
СИСТЕМА: Microsoft Windows 10 Home (x64);
ВЕРСИЯ PYTHON: 3.9
'''


@profile
def total_multiple(first_num, second_num):
    """
    Написать функцию нахождения общих кратных для двух чисел.
    """
    array = list(range(100000))
    first_multiple = [i for i in array if i % first_num == 0]
    second_multiple = [i for i in first_multiple if i % second_num == 0]
    del array, first_multiple
    return second_multiple


total_multiple(13, 25)
'''
Для запуска программы было выделено 18.7 MiB.
При создании списков array и first_multiple было выделено еще 3.8 MiB и 0.2 MiB оответственно.
После создания итогового списка second_multiple удалил списки array и first_multiple,
тем самым освободив память (0.9 MiB).

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    28     18.7 MiB     18.7 MiB           1   @profile
    29                                         def total_multiple(first_num, second_num):
    30                                             """
    31                                             Написать функцию нахождения общих кратных для двух чисел
    32                                             """
    33     22.4 MiB      3.8 MiB           1       array = list(range(100000))
    34     22.6 MiB      0.2 MiB      100003       first_multiple = [i for i in array if i % first_num == 0]
    35     22.6 MiB      0.0 MiB        7696       second_multiple = [i for i in first_multiple if i % second_num == 0]
    36     21.7 MiB     -0.9 MiB           1       del array, first_multiple
    37     21.7 MiB      0.0 MiB           1       return second_multiple
'''


@profile
def er_simple(i):
    """
    Функция нахождения i-го по счёту простого числа через "Решето Эратосфена".
    """
    a = [el for el in range(10000)]
    a[1] = 0
    f = 2
    while f <= len(a) - 1:
        if a[f] != 0:
            j = f + f
            while j <= len(a) - 1:
                a[j] = 0
                j = j + f
        f += 1
    a = sorted(set(a))
    a.remove(0)
    return a[i - 1]


er_simple(25)
'''
Для запуска программы было выделено 18.9 MiB.
При создании списка а было выделено еще 0.4 MiB.
При переопределении переменной а со списка на отсортированное множество было освобождено 0.2 MiB.
По итогу инкремент невысокий, поэтому оптимизация не требуется.

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    67     18.9 MiB     18.9 MiB           1   @profile
    68                                         def er_simple(i):
    69                                             """
    70                                             Функция нахождения i-го по счёту простого числа через
                                                   "Решето Эратосфена".
    71                                             """
    72     19.3 MiB      0.4 MiB       10003       a = [el for el in range(10000)]
    73     19.3 MiB      0.0 MiB           1       a[1] = 0
    74     19.3 MiB      0.0 MiB           1       f = 2
    75     19.3 MiB      0.0 MiB        9999       while f <= len(a) - 1:
    76     19.3 MiB      0.0 MiB        9998           if a[f] != 0:
    77     19.3 MiB      0.0 MiB        1229               j = f + f
    78     19.3 MiB      0.0 MiB       24298               while j <= len(a) - 1:
    79     19.3 MiB      0.0 MiB       23069                   a[j] = 0
    80     19.3 MiB      0.0 MiB       23069                   j = j + f
    81     19.3 MiB      0.0 MiB        9998           f += 1
    82     19.1 MiB     -0.2 MiB           1       a = sorted(set(a))
    83     19.1 MiB      0.0 MiB           1       a.remove(0)
    84     19.1 MiB      0.0 MiB           1       return a[i - 1]
'''


def check_memory(func):
    """
    Функция, позволяющая определить среднее значение дельты (5 замеров) использования памяти между началом
    и концом программы.
    """

    def start(*args, **kwargs):
        diff_memory = []
        for i in range(5):
            memory_1 = memory_usage()
            print(f'memory_1 - {memory_1}')
            func(*args)
            memory_2 = memory_usage()
            print(f'memory_2 - {memory_2}')
            diff_memory.append(memory_2[0] - memory_1[0])

        print(f'{sum(diff_memory) / 5} MiB')

    return start


@check_memory
def total_multiple(first_num, second_num):
    """
    Написать функцию нахождения общих кратных для двух чисел.
    """
    array = list(range(100000))
    first_multiple = [i for i in array if i % first_num == 0]
    second_multiple = [i for i in first_multiple if i % second_num == 0]
    del array, first_multiple
    return second_multiple


total_multiple(13, 25)
'''
Среднее значение дельты использования памяти - 0.04375 MiB.
memory_1 - [19.609375]
memory_2 - [19.7265625]
memory_1 - [19.7265625]
memory_2 - [19.8125]
memory_1 - [19.8125]
memory_2 - [19.8125]
memory_1 - [19.8125]
memory_2 - [19.8203125]
memory_1 - [19.8203125]
memory_2 - [19.828125]
0.04375 MiB
'''
