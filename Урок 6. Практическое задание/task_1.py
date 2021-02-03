"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять задачи с курса Основ
или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайзаказчте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""
from random import randint
from memory_profiler import profile


@profile
def simple(i):
    """Без использования «Решета Эратосфена»"""
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


@profile
def simple_2(i):
    simples = []
    cur_numb = 2
    cur_indx = 1
    while cur_indx < i + 1:
        is_simple = True
        for j in simples:
            if cur_numb % j == 0:
                cur_numb += 1
                is_simple = False
                break
        if is_simple:
            simples.append(cur_numb)
            cur_indx += 1
    return cur_numb


i = 550
# print(simple(i))
# print(simple_2(i))

"""
Тест памяти  показал конкретного значения использования памяти, но, стало понятно, почему второй алгоритм втрое быстрее
выполняется: профилировщик показывает число выполнений каждого этапа алгоритма, и, на конкретных цифрах - в перовм 
алгоритме 1млн О(1) опрераций, во втором - 300тыс. отсюда и разница во времени выполнения
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    25     17.7 MiB     17.7 MiB           1   @profile
    26                                         def simple(i):
    27                                            
    28     17.7 MiB      0.0 MiB           1       count = 1
    29     17.7 MiB      0.0 MiB           1       n = 2
    30     17.7 MiB      0.0 MiB        3988       while count <= i:
    31     17.7 MiB      0.0 MiB        3988           t = 1
    32     17.7 MiB      0.0 MiB        3988           is_simple = True
    33     17.7 MiB      0.0 MiB     1030328           while t <= n:
    34     17.7 MiB      0.0 MiB     1029778               if n % t == 0 and t != 1 and t != n:
    35     17.7 MiB      0.0 MiB        3438                   is_simple = False
    36     17.7 MiB      0.0 MiB        3438                   break
    37     17.7 MiB      0.0 MiB     1026340               t += 1
    38     17.7 MiB      0.0 MiB        3988           if is_simple:
    39     17.7 MiB      0.0 MiB         550               if count == i:
    40     17.7 MiB      0.0 MiB           1                   break
    41     17.7 MiB      0.0 MiB         549               count += 1
    42     17.7 MiB      0.0 MiB        3987           n += 1
    43     17.7 MiB      0.0 MiB           1       return n


3989
Filename: /home/alex/geekbrains/python_algos_gb/Урок 6. Практическое задание/task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    45     17.7 MiB     17.7 MiB           1   @profile
    46                                         def simple_2(i):
    47     17.7 MiB      0.0 MiB           1       simples = []
    48     17.7 MiB      0.0 MiB           1       cur_numb = 2
    49     17.7 MiB      0.0 MiB           1       cur_indx = 1
    50     17.7 MiB      0.0 MiB        4538       while cur_indx < i + 1:
    51     17.7 MiB      0.0 MiB        4537           is_simple = True
    52     17.7 MiB      0.0 MiB      310215           for j in simples:
    53     17.7 MiB      0.0 MiB      309665               if cur_numb % j == 0:
    54     17.7 MiB      0.0 MiB        3987                   cur_numb += 1
    55     17.7 MiB      0.0 MiB        3987                   is_simple = False
    56     17.7 MiB      0.0 MiB        3987                   break
    57     17.7 MiB      0.0 MiB        4537           if is_simple:
    58     17.7 MiB      0.0 MiB         550               simples.append(cur_numb)
    59     17.7 MiB      0.0 MiB         550               cur_indx += 1
    60     17.7 MiB      0.0 MiB           1       return cur_numb


3989
"""




#######################################################################################################################
"""
Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке. Для выполнения задания обязательно использовать
генератор списка. (Можно использовать list.count()).
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
"""


@profile
def first(in_list):
    res = [el for el in in_list if in_list.count(el) == 1]
    return res


"""
По следующим алгоритмам потребление памяти измерить не удалось по причине малого потребления.
Но профилирование помогает оценить сложность в нотации big О() и увидеть зависимость времени выполнения от сложности.

Время выполнения: 
    0.012377024989982601 
    0.028858142269891685
    0.07359166106994962
    0.03938548205005645
    0.0006511509199481224
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   126     17.8 MiB     17.8 MiB           1   @profile
   127                                         def first(in_list):
   128     17.8 MiB      0.0 MiB        1003       res = [el for el in in_list if in_list.count(el) == 1]
   129     17.8 MiB      0.0 MiB           1       return res
"""


@profile
def second(in_list):
    no_double_indexes = [el for el in range(0, len(in_list))]  # список индексов
    i = 0
    while i < len(no_double_indexes):
        i_in = i + 1
        len_change = False
        len_no_double_indexes = len(no_double_indexes)
        while i_in < len_no_double_indexes:
            if in_list[no_double_indexes[i]] == in_list[no_double_indexes[i_in]]:
                no_double_indexes.remove(no_double_indexes[i_in])
                len_no_double_indexes = len(no_double_indexes)
                len_change = True
            else:
                i_in += 1
        if len_change:
            no_double_indexes.remove(no_double_indexes[i])
        else:
            i += 1
    res = [in_list[i] for i in no_double_indexes]
    print(res)


"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   136     17.8 MiB     17.8 MiB           1   @profile
   137                                         def second(in_list):
   138     17.8 MiB      0.0 MiB        1003       no_double_indexes = [el for el in range(0, len(in_list))]  # список индексов
   139     17.8 MiB      0.0 MiB           1       i = 0
   140     17.8 MiB      0.0 MiB         645       while i < len(no_double_indexes):
   141     17.8 MiB      0.0 MiB         644           i_in = i + 1
   142     17.8 MiB      0.0 MiB         644           len_change = False
   143     17.8 MiB      0.0 MiB         644           len_no_double_indexes = len(no_double_indexes)
   144     17.8 MiB      0.0 MiB      289540           while i_in < len_no_double_indexes:
   145     17.8 MiB      0.0 MiB      288896               if in_list[no_double_indexes[i]] == in_list[no_double_indexes[i_in]]:
   146     17.8 MiB      0.0 MiB         356                   no_double_indexes.remove(no_double_indexes[i_in])
   147     17.8 MiB      0.0 MiB         356                   len_no_double_indexes = len(no_double_indexes)
   148     17.8 MiB      0.0 MiB         356                   len_change = True
   149                                                     else:
   150     17.8 MiB      0.0 MiB      288540                   i_in += 1
   151     17.8 MiB      0.0 MiB         644           if len_change:
   152     17.8 MiB      0.0 MiB         259               no_double_indexes.remove(no_double_indexes[i])
   153                                                 else:
   154     17.8 MiB      0.0 MiB         385               i += 1
   155     17.8 MiB      0.0 MiB         388       res = [in_list[i] for i in no_double_indexes]
   156     17.8 MiB      0.0 MiB           1       print(res)
"""


@profile
def third(in_list):
    i = 0
    res = []
    len_list = len(in_list)
    while i < len_list:
        i_in = 0
        is_double = False
        while i_in < len_list:
            if in_list[i] == in_list[i_in] and i != i_in:
                is_double = True
            i_in += 1
        if not is_double:
            res.append(in_list[i])
        i += 1

    print(res)


"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   163     17.8 MiB     17.8 MiB           1   @profile
   164                                         def third(in_list):
   165     17.8 MiB      0.0 MiB           1       i = 0
   166     17.8 MiB      0.0 MiB           1       res = []
   167     17.8 MiB      0.0 MiB           1       len_list = len(in_list)
   168     17.8 MiB      0.0 MiB        1001       while i < len_list:
   169     17.8 MiB      0.0 MiB        1000           i_in = 0
   170     17.8 MiB      0.0 MiB        1000           is_double = False
   171     17.8 MiB      0.0 MiB     1001000           while i_in < len_list:
   172     17.8 MiB      0.0 MiB     1000000               if in_list[i] == in_list[i_in] and i != i_in:
   173     17.8 MiB      0.0 MiB         954                   is_double = True
   174     17.8 MiB      0.0 MiB     1000000               i_in += 1
   175     17.8 MiB      0.0 MiB        1000           if not is_double:
   176     17.8 MiB      0.0 MiB         385               res.append(in_list[i])
   177     17.8 MiB      0.0 MiB        1000           i += 1
   178                                         
   179     17.8 MiB      0.0 MiB           1       print(res)
   """


@profile
def fourth(in_list):
    res = []
    len_list = len(in_list)
    for i, el in enumerate(in_list):
        is_double = False
        for i_in, el_in in enumerate(in_list):
            if el_in == el and i != i_in:
                is_double = True
        if not is_double:
            res.append(el)
    print(res)


"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   183     17.8 MiB     17.8 MiB           1   @profile
   184                                         def fourth(in_list):
   185     17.8 MiB      0.0 MiB           1       i = 0
   186     17.8 MiB      0.0 MiB           1       res = []
   187     17.8 MiB      0.0 MiB           1       len_list = len(in_list)
   188     17.8 MiB      0.0 MiB        1001       for i, el in enumerate(in_list):
   189     17.8 MiB      0.0 MiB        1000           is_double = False
   190     17.8 MiB      0.0 MiB     1001000           for i_in, el_in in enumerate(in_list):
   191     17.8 MiB      0.0 MiB     1000000               if el_in == el and i != i_in:
   192     17.8 MiB      0.0 MiB         954                   is_double = True
   193     17.8 MiB      0.0 MiB        1000           if not is_double:
   194     17.8 MiB      0.0 MiB         385               res.append(el)
   195     17.8 MiB      0.0 MiB           1       print(res)
"""


@profile
def fifth(in_list):
    counts = {}
    for el in in_list:
        if el not in counts:
            counts[el] = 0
        counts[el] += 1
    res = [el for el in counts.keys() if counts[el] == 1]
    print(res)


"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   198     17.8 MiB     17.8 MiB           1   @profile
   199                                         def fifth(in_list):
   200     17.8 MiB      0.0 MiB           1       counts = {}
   201     17.8 MiB      0.0 MiB        1001       for el in in_list:
   202     17.8 MiB      0.0 MiB        1000           if el not in counts:
   203     17.8 MiB      0.0 MiB         644               counts[el] = 0
   204     17.8 MiB      0.0 MiB        1000           counts[el] += 1
   205     17.8 MiB      0.0 MiB         647       res = [el for el in counts.keys() if counts[el] == 1]
   206     17.8 MiB      0.0 MiB           1       print(res)
"""

in_list = [randint(0, 1000) for _ in range(1000)]
# first(in_list)
# second(in_list)
# third(in_list)
# fourth(in_list)
# fifth(in_list)

########################################################################################################################
"""Задача рекурсивного разворота числа. с мемоизацией и без"""
from timeit import timeit


def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


def memoize(f):
    cache = {}

    def decorate(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorate


@memoize
def recursive_reverse_mem(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'


@profile
def test_recursion():
    t1 = timeit(
        'recursive_reverse_mem(123456789987456321123456789987456321231123456789987456321123456789987456321231123456789'
        '9874563211234567899874563212311234567899874563211234567899321123456789932112345678998745632123'
        '9874563211234567899874563212311234567899874563211234567899321123456789932112345678998745632123'
        '9874563211234567899874563212311234567899874563211234567899321123456789932112345678998745632123'
        '9874563211234567899874563212311234567899874563211234567899321123456789932112345678998745632123'
        '1)',
        globals=globals(), number=100)

    t2 = timeit('recursive_reverse(123456789987456321123456789987456321231123456789987456321123456789987456321231123456789'
           '9874563211234567899874563212311234567899874563211234567899321123456789932112345678998745632123'
           '9874563211234567899874563212311234567899874563211234567899321123456789932112345678998745632123'
           '9874563211234567899874563212311234567899874563211234567899321123456789932112345678998745632123'
           '9874563211234567899874563212311234567899874563211234567899321123456789932112345678998745632123'
           '1)',
           globals=globals(), number=100)
    print(t1, t2)

test_recursion()


"""
Для мемоизации используется кеш, который ускоряет вычисления но использует больше памяти, чем алгоритм без мемоизации 

Время
0.0023759790346957743 0.07116394100012258

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   339     17.8 MiB     17.8 MiB           1   @profile
   340                                         def test_recursion():
   341     17.8 MiB      0.0 MiB           1       sleep(1)
   342                                         
   343     19.2 MiB      1.3 MiB           2       timeit('recursive_reverse_mem(123456789987456321123456789987456321231123456789987456321123456789987456321231123456789'
   344                                                    '9874563211234567899874563212311234567899874563211234567899321123456789932112345678998745632123'
   345                                                    '9874563211234567899874563212311234567899874563211234567899321123456789932112345678998745632123'
   346                                                    '9874563211234567899874563212311234567899874563211234567899321123456789932112345678998745632123'
   347                                                    '9874563211234567899874563212311234567899874563211234567899321123456789932112345678998745632123'
   348                                                    '1)',
   349     17.8 MiB      0.0 MiB           1           globals=globals(), number=100)
   350                                         
   351     19.4 MiB      0.3 MiB           2       timeit('recursive_reverse(123456789987456321123456789987456321231123456789987456321123456789987456321231123456789'
   352                                                    '9874563211234567899874563212311234567899874563211234567899321123456789932112345678998745632123'
   353                                                    '9874563211234567899874563212311234567899874563211234567899321123456789932112345678998745632123'
   354                                                    '9874563211234567899874563212311234567899874563211234567899321123456789932112345678998745632123'
   355                                                    '9874563211234567899874563212311234567899874563211234567899321123456789932112345678998745632123'
   356                                                    '1)',
   357     19.2 MiB      0.0 MiB           1              globals=globals(), number=100)
"""