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

import time
from memory_profiler import profile, memory_usage


def my_decorator(func):
    def inner(*args, **kwargs):
        t1 = time.process_time()
        m1 = memory_usage()
        func(*args, **kwargs)
        t2 = time.process_time()
        m2 = memory_usage()
        print(f'Выполнение заняло {t2 - t1} сек and {m2[0] - m1[0]} Mib')

    return inner()


"""
1. Для чисел в пределах от 20 до 10000 найти числа, кратные 20 или 21. 
Провести поиск по этому массиву и если элемент равен 210 вывести его.
"""


@my_decorator
def func_1():
    lst = list(range(20, 10000))
    new_lst = [
        number for number in lst if number % 20 == 0 or number % 21 == 0
    ]
    for i in new_lst:
        if i == 210:
            return i


@my_decorator
def func_2():
    lst = list(range(20, 10000))
    new_lst = (number for number in lst
               if number % 20 == 0 or number % 21 == 0)
    for i in new_lst:
        if i == 210:
            return i


@profile
def func_1_pr():
    lst = list(range(20, 10000))
    new_lst = [
        number for number in lst if number % 20 == 0 or number % 21 == 0
    ]
    for i in new_lst:
        if i == 210:
            return i


func_1_pr()
"""
для func_1() :
Выполнение заняло 0.0024246799999999985 сек and 0.26171875 Mib

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    68     20.2 MiB     20.2 MiB           1   @profile
    69                                         def func_1_pr():
    70     20.4 MiB      0.3 MiB           1       lst = list(range(20, 10000))
    71     20.4 MiB      0.0 MiB        9984       new_lst = [
    72     20.4 MiB      0.0 MiB       10933           number for number in lst
    73     20.4 MiB      0.0 MiB        9980           if number % 20 == 0 or number % 21 == 0
    74                                             ]
    75     20.4 MiB      0.0 MiB          20       for i in new_lst:
    76     20.4 MiB      0.0 MiB          20           if i == 210:
    77     20.4 MiB      0.0 MiB           1               return i

Для запуска было выделено 20.2 MiB и при создании списка еще 0.3 MiB

для func_2():
Выполнение заняло 0.00043816399999996314 сек and 0.0 Mib

Наглядно видно, что использование генератора во 2 случае, эффективно расходует память и увеличивает время.
"""
"""
2. Вывести на экран коды и символы таблицы ASCII, начиная с символа
под номером 32 и заканчивая 999-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
"""


@my_decorator
def func_3():
    def rec(count=1, i=32):
        if i == 1000:
            return
        elif count == 10:
            count = 1
            print(f'{i} - {chr(i)}', end='\n')
        elif count < 10:
            count += 1
            print(f'{i} - {chr(i)}', end=' ')
        return rec(count, i + 1)

    return rec(count=1, i=32)


@profile
def func_3_pr():
    def rec(count=1, i=32):
        if i == 1000:
            return
        elif count == 10:
            count = 1
            print(f'{i} - {chr(i)}', end='\n')
        elif count < 10:
            count += 1
            print(f'{i} - {chr(i)}', end=' ')
        return rec(count, i + 1)

    return rec(count=1, i=32)


func_3_pr()


@my_decorator
def func_4():
    count = 0
    for i in range(32, 1000):
        if count < 10:
            print(f'{i} - {chr(i)}', end=' ')
            count += 1
        if count == 10:
            count = 0
            print(f'{i} - {chr(i)}', end='\n')


"""
для func_3():
Выполнение заняло 0.005929686999999989 сек and 0.8359375 Mib

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
     4     19.8 MiB     19.8 MiB           1   @profile
     5                                         def func_3():
     6     21.1 MiB      1.1 MiB         970     def rec(count = 1, i=32):
     7     21.1 MiB      0.3 MiB         969         if i == 1000:
     8     21.1 MiB      0.0 MiB           1             return
     9     21.1 MiB      0.0 MiB         968         elif count == 10:
    10     21.1 MiB      0.0 MiB          96             count = 1
    11     21.1 MiB      0.0 MiB          96             print(f'{i} - {chr(i)}', end='\n')
    12     21.1 MiB      0.0 MiB         872         elif count < 10:
    13     21.1 MiB      0.0 MiB         872             count += 1
    14     21.1 MiB      0.0 MiB         872             print(f'{i} - {chr(i)}', end=' ')
    15     21.1 MiB      0.0 MiB         968         return rec(count, i + 1)
    16     21.1 MiB      0.0 MiB           1     return rec(count = 1, i=32)

для func_4():
Выполнение заняло 0.00406131500000001 сек and 0.0 Mib

Избавляясь от рекурсии во 2 функции значительно уменьшаем память,т.к при ее работе хранится стек, хотя время оказалось приблизительно одинаковое.
"""
"""
3. Приведен наивный алгоритм нахождения i-го по счёту простого числа (через перебор делителей).
Попробуйте решить эту же задачу, применив алгоритм "Решето эратосфена" 
"""


@my_decorator
def simple(i=1000):
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


@my_decorator
def eratosfen(i=1000):
    n = 2
    l = 10000
    sieve = [x for x in range(l)]
    sieve[1] = 0
    while n < l:
        if sieve[n] != 0:
            m = n * 2
            while m < l:
                sieve[m] = 0
                m += n
        n += 1
    return [p for p in sieve if p != 0][i - 1]


@profile
def eratosfen_pr(i=1000):
    n = 2
    l = 10000
    sieve = [x for x in range(l)]
    sieve[1] = 0
    while n < l:
        if sieve[n] != 0:
            m = n * 2
            while m < l:
                sieve[m] = 0
                m += n
        n += 1
    return [p for p in sieve if p != 0][i - 1]


print(eratosfen_pr())
"""
для simple():
Выполнение заняло 1.1142549419999999 сек and 0.0 Mib
для eratosfen():
Выполнение заняло 0.01147612099999984 сек and 0.26953125 Mib

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   218     20.1 MiB     20.1 MiB           1   @profile
   219                                         def eratosfen_pr(i=1000):
   220     20.1 MiB      0.0 MiB           1       n = 2
   221     20.1 MiB      0.0 MiB           1       l = 10000
   222     20.4 MiB      0.3 MiB       10003       sieve = [x for x in range(l)]
   223     20.4 MiB      0.0 MiB           1       sieve[1] = 0
   224     20.4 MiB      0.0 MiB        9999       while n < l:
   225     20.4 MiB      0.0 MiB        9998           if sieve[n] != 0:
   226     20.4 MiB      0.0 MiB        1229               m = n * 2
   227     20.4 MiB      0.0 MiB       24298               while m < l:
   228     20.4 MiB      0.0 MiB       23069                   sieve[m] = 0
   229     20.4 MiB      0.0 MiB       23069                   m += n
   230     20.4 MiB      0.0 MiB        9998           n += 1
   231     20.4 MiB      0.0 MiB       10003       return [p for p in sieve if p != 0][i - 1]

Несмотря на то, что время на выполнение постепенно выше у простого алгоритма, память расходуется эффективнее чем в алгоритме с применением решета.
В решете накапливается память за счет применения и перебора в списке.
"""